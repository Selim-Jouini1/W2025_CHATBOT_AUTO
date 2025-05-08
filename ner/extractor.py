import pandas as pd
import spacy
import re

nlp = spacy.load("en_core_web_sm")

# Load car data once at app startup
car_df = pd.read_csv("data/cars.csv")

def extract_entities(question, known_pairs):
    question_lower = question.lower()
    matched_brand = None
    matched_model = None

    for brand, model in known_pairs:
        # Extract plain brand without number (e.g., "volvo" from "volvo1")
        brand_base = ''.join(filter(str.isalpha, brand)).lower()
        model_lower = model.lower()

        if brand_base in question_lower and model_lower in question_lower:
            matched_brand = brand
            matched_model = model
            break

    return {
        "CarType": matched_brand,
        "CarModel": matched_model
    }
