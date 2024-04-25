import pickle

def predict(user_input):
    # Load the model using pickle
    with open("ecom.pkl", "rb") as f:
        rf = pickle.load(f)
    
    # Make predictions
    prediction = rf.predict([user_input])
    
    return prediction