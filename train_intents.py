# train_intents.py

from intents.classifier import train_and_save_model

if __name__ == "__main__":
    train_and_save_model()  # Train the model and save it to 'models/intent_model.pkl'
    print("Model trained and saved successfully!")
