#!/usr/bin/env python

import os
import pandas as pd
import requests
import json

from sklearn.metrics import mean_absolute_error

LOCAL_SERVER_URL = 'http://127.0.0.1:8000/api/v1/predict'
EXTERNAL_SERVER_URL = 'http://mlengineerassigment-env.eu-central-1.elasticbeanstalk.com/api/v1/predict'

# Change to True to execute the script in the online server
EXTERNAL = False

DATA_PATH = '../data'
TRAIN_PATH = os.path.join(DATA_PATH, 'train.csv')
VALID_PATH = os.path.join(DATA_PATH, 'valid.csv')
TEST_PATH = os.path.join(DATA_PATH, 'test.csv')

DATE_COLUMNS = ['join_date']

BLOCK_SIZE = 1000

PRED_COLUMN = 'pred'
TARGET_COLUMN = 'target'


def predict_request(url, body):
    response = requests.post(url=url, json=body)
    if response.ok:
        return response.json()
    else:
        raise Exception('There was an error in server call: ', response.reason)


def calculate_mae(data, predictions, file):
    log_filename = file+'.mae.txt'
    print('Calculating MAE and saving results into', log_filename)
    log_file = open(log_filename, 'w')

    if TARGET_COLUMN in data.columns:
        copy = data.copy()
        # Add prediction to dataset
        copy[PRED_COLUMN] = predictions

        # Truncate join_date column by day/month/year
        copy['join_date'] = copy['join_date'] \
            .apply(lambda x: pd.to_datetime(x).replace(hour=0, minute=0, second=0, microsecond=0))

        # Aggregate dataset
        data_aggregated = copy.groupby(['join_date', 'country_segment', 'hidden',
                                        'credit_card_level', 'is_lp',
                                        'aff_type', 'is_cancelled'], as_index=False)\
                              .agg({TARGET_COLUMN: 'sum', PRED_COLUMN: 'sum'})

        country_segment = 'country_segment'
        # Calculate MAE for each country
        for country in data_aggregated[country_segment].unique():
            pred = data_aggregated[data_aggregated[country_segment] == country][PRED_COLUMN]
            valid_target = data_aggregated[data_aggregated[country_segment] == country][TARGET_COLUMN]

            if not pred.empty:
                print("The model's metrics for country", country, "are:", file=log_file)
                print('MAE = ', mean_absolute_error(pred, valid_target), file=log_file)
                print('', file=log_file)
    else:
        print('Data does not have the target column', file=log_file)

    log_file.close()


def get_server_url():
    if EXTERNAL:
        return EXTERNAL_SERVER_URL
    return LOCAL_SERVER_URL


if __name__ == '__main__':
    server_url = get_server_url()
    print('Using', server_url, 'server')

    for file in [VALID_PATH, TEST_PATH]:
        print('Reading file', file, '...')
        data = pd.read_csv(file)

        total_size = len(data)
        total_iterations = int(total_size / BLOCK_SIZE)

        predictions = []

        for block in range(0, total_iterations+1):
            start = BLOCK_SIZE*block
            end = start + BLOCK_SIZE
            print('start:', start, '- end:', end, '- total:', len(data[start:end]))

            print('Converting csv to json...')
            json_data = json.loads(data[start:end].to_json(orient='records'))

            print('Sending predict request...')
            predict = predict_request(server_url, json_data)
            predictions.extend(predict)

        calculate_mae(data, predictions, file)
