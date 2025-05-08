import joblib
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Train and save the model (you can call this function to train and save)
def train_and_save_model():
    X = [
        "Price of Volvo S80", "How much is the Kia Rio?", "Tell me about problems in Ford Focus",
        "Is BMW X5 reliable?", "What are the common problems with Volvo XC90?", "Tell me about the problems with a BMW 3 Series",
        "What is the price of a Toyota Corolla?", "I want to know the problems with a Ford Mustang",
        "Thanks", "Hello", "Hi", "Hey, how are you?", "How's it going?", "I'm fine, thanks!", "Good morning!"
    ]

    y = ["get_price", "get_price", "get_problems", "get_reliability", "get_problems", "get_problems", 
        "get_price", "get_problems", "thanks", "greeting", "greeting", "greeting", "greeting", "greeting", "greeting"]

    model = make_pipeline(TfidfVectorizer(), LogisticRegression())
    model.fit(X, y)
    joblib.dump(model, 'models/intent_model.pkl')

# Load the trained model
def load_model():
    try:
        # Attempt to load the model from the file
        return joblib.load('models/intent_model.pkl')
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Detect the intent of a question
def detect_intent(question):
    model = load_model()
    intent = model.predict([question])[0]
    print(f"Detected intent: {intent} for question: {question}")  # Debugging line
    return intent

