import os
import pickle

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, 'ml_model/finelized_model.sav')

with open(MODEL_PATH) as f:
    ML_MODEL = pickle.load(f)
