import pickle

def predict(user_input):
    try:
        # Load the model using pickle
        with open("ecom.pkl", "rb") as f:
            rf = pickle.load(f)
        
        print("Model loaded successfully!")
        
        # Make predictions
        prediction = rf.predict([user_input])
        
        return prediction
    
    except Exception as e:
        print(f"Error loading the model: {e}")
        return None