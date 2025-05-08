import pandas as pd
from flask import Flask, request, jsonify
from intents.classifier import detect_intent
from ner.extractor import extract_entities
from conversation.state import update_state

app = Flask(__name__)


car_data_df = pd.read_csv("data/cars.csv")
known_pairs = list(zip(car_data_df["CarType"], car_data_df["CarModel"]))

def query_car_data(car_type, car_model):
    car_data_df = pd.read_csv("data/cars.csv")

    car_type = str(car_type) if car_type else ""
    car_model = str(car_model) if car_model else ""

    matched_car_data = car_data_df[
        (car_data_df['CarType'].str.contains(car_type, case=False, na=False)) & 
        (car_data_df['CarModel'].str.contains(car_model, case=False, na=False))
    ]

    if not matched_car_data.empty:
        car_info = matched_car_data.iloc[0]
        return {
            "CarType": car_info["CarType"],
            "CarModel": car_info["CarModel"],
            "Problem": car_info["Problem"],
            "Year": car_info.get("Year", ""),
            "Kilometrage": car_info.get("Kilometrage", ""),
            "Price": car_info.get("Price", "")
        }
    else:
        return None

@app.route("/chat", methods=["POST"])
def chat():
    global state

    data = request.get_json()
    question = data.get("question", "")
    
    entities = extract_entities(question, known_pairs)
    car_type = entities.get('CarType', '')
    car_model = entities.get('CarModel', '')
    
    intent = detect_intent(question)
    
    car_data = query_car_data(car_type, car_model)
    print("Extracted car_type:", car_type)
    print("Extracted car_model:", car_model)
    
    if car_data:
        if intent == "get_price":
            response_message = f"The price of the {car_data['CarType']} {car_data['CarModel']} is {car_data['Price']}."
        elif intent == "get_problems":
            clean_car_type = ''.join(filter(str.isalpha, car_data['CarType']))
            response_message = f"Some common problems with the {clean_car_type} {car_data['CarModel']} are: {car_data['Problem']}."
        elif intent == "greeting":
            response_message = "Hello! How can I assist you today?"
        elif intent == "thanks":
            response_message = "You're welcome! Let me know if you need anything else."
        else:
            response_message = "Sorry, I couldn't find the car information you're asking about. Please check the car model or try another one."

    state = update_state({}, entities)
    state = update_state(state, {'Intent': intent})
    
    return jsonify({"message": response_message, "state": state})

if __name__ == "__main__":
    app.run(debug=True)
