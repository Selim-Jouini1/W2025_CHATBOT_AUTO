from flask import Flask, request, jsonify
from chatbot.data_loader import load_data
from chatbot.bot_logic import find_answers

app = Flask(__name__)
df = load_data("data/cars.csv")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('question')
    response = find_answers(df, user_input)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
