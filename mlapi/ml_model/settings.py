import os
import pickle
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, 'ml_model/finalized_model.sav')
ML_MODEL = pickle.load(open(MODEL_PATH, 'rb'))

CREDIT_CARD_COLUMN = 'credit_card_level'
AFF_TYPE_COLUMN = 'aff_type'
COUNTRY_SEGMENT_COLUMN = 'country_segment'

CATEGORY_COLUMNS = ['credit_card_level', 'aff_type', 'country_segment']
DATE_COLUMNS = ['join_date']
NUMBER_COLUMNS = ['hidden', 'STV', 'is_lp', 'is_cancelled']

FEATURES_COLUMNS = ['join_date', 'hidden', 'STV', 'credit_card_level',
                    'is_lp', 'aff_type', 'is_cancelled', 'country_segment']
TARGET_COLUMN = 'target'

NULL_CATEGORY_KEY = 'Unknown'
NULL_CATEGORY_VALUE = -1

NULL_NUMBER_VALUE = -1
NULL_DATE_VALUE = datetime.date(1000, 1, 1)
