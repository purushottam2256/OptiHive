from flask import Flask, request, jsonify
import joblib
import logging
import os
from typing import List, Dict, Any

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Load model
try:
    model = joblib.load('../models/battery_check_model.pkl')
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    raise

@app.route('/api/predict', methods=['POST'])
def predict():
    """Predict next battery check interval."""
    try:
        # Get and validate input
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        required_fields = ['battery_percentage', 'voltage', 'full_charge_capacity']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {missing_fields}"}), 400
        
        # Prepare features (matching model requirements)
        features = [
            data.get('battery_percentage', 0),
            data.get('voltage', 0),
            data.get('full_charge_capacity', 0),
        ]
        
        # Make prediction
        prediction = model.predict([features])
        logger.info(f"Prediction made: {prediction[0]}")
        
        return jsonify({'next_check_interval': float(prediction[0])})
    
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return jsonify({"error": "Prediction failed"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)