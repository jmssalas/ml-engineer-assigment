#!/usr/bin/env python

import os
import pandas as pd
import requests
import json

DATA_PATH = '../data'
TRAIN_PATH = os.path.join(DATA_PATH, 'train.csv')
VALID_PATH = os.path.join(DATA_PATH, 'valid.csv')
TEST_PATH = os.path.join(DATA_PATH, 'test.csv')

SERVER_URL = 'http://127.0.0.1:8000/api/v1/predict'


def predict_request(url, body):
    response = requests.post(url=url, json=body)
    if response.ok:
        return response.json()
    else:
        return None


if __name__ == '__main__':
    print('Reading csv...')
    data = pd.read_csv(TEST_PATH)

    block_size = 400
    total_size = len(data)
    total_iterations = int(total_size / block_size)

    predictions = []

    for block in range(0, total_iterations+1):
        start = block_size*block
        end = start + block_size
        print('start:', start, '- end:', end, '- total:', len(data[start:end]))

        print('Converting csv to json..')
        json_data = json.loads(data[start:end].to_json(orient='records'))

        print('Sending predict request...')
        predict = predict_request(SERVER_URL, json_data)
        if predict is not None:
            predictions.extend(predict)

    print(predictions, len(predictions))
