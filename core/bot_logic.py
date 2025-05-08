from intents.classifier import detect_intent
from ner.extractor import extract_entities
from conversation.state import update_state
from core.data_loader import load_and_clean_data  # assuming you already have this

df = load_and_clean_data('data/cars.csv')

def find_answers(question, conversation_state):
    intent = detect_intent(question)
    entities = extract_entities(question)
    conversation_state = update_state(conversation_state, entities)

    if intent == "get_price":
        if "CarType" in conversation_state and "CarModel" in conversation_state:
            results = df[
                (df['CarType'].str.lower() == conversation_state['CarType'].lower()) &
                (df['CarModel'].str.lower() == conversation_state['CarModel'].lower())
            ]
            if not results.empty:
                return {"price": results.iloc[0]["Price"]}
            else:
                return {"message": "I couldn't find the price for that model."}
        else:
            return {"message": "Please provide both the brand and model to get the price."}
    
    elif intent == "get_problems":
        # Add problem logic similarly
        return {"message": "I can help with problems. Please tell me the car model."}

    elif intent == "greeting":
        return {"message": "Hello! How can I assist you with car info today?"}

    return {"message": "I didn't understand that. Could you rephrase?"}
