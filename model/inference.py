import tensorflow as tf
import pickle
from preprocess import preprocess_input

class AIModel:
    def __init__(self, model_path='model/model.pkl'):
        """Load the trained model"""
        try:
            # Try loading as SavedModel first
            self.model = tf.keras.models.load_model(model_path.replace('.pkl', '.h5'))
        except:
            # Fall back to pickle
            with open(model_path, 'rb') as f:
                self.model = pickle.load(f)
    
    def predict(self, input_data):
        """Make predictions on new data"""
        processed_data = preprocess_input(input_data)
        return self.model.predict(processed_data).tolist()

# Example usage:
# model = AIModel()
# prediction = model.predict([[0.1, 0.2, ..., 0.2]])  # 20 features
