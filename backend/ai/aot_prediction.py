import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import joblib
from datetime import datetime

def create_model(input_shape):
    model = Sequential([
        LSTM(50, activation='relu', input_shape=input_shape),
        Dense(25, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

loaded_model = create_model((1, 5))
loaded_model.load_weights('backend/ai/riyadh_aot_lstm_v2.weights.h5')
loaded_scaler = joblib.load('backend/ai/riyadh_aot_scaler_v2.pkl')

def predict_aot_batch(input_array, prediction_date):
    # Prepare input data
    processed_inputs = []
    for row in input_array:
        date, latitude, longitude, current_aot = row
        day_of_year = prediction_date.timetuple().tm_yday
        month = prediction_date.month
        processed_inputs.append([latitude, longitude, current_aot, day_of_year, month])

    processed_inputs = np.array(processed_inputs)

    # Scale the inputs
    inputs_scaled = loaded_scaler.transform(processed_inputs)
    inputs_reshaped = np.reshape(inputs_scaled, (inputs_scaled.shape[0], 1, 5))

    # Make predictions
    predictions = loaded_model.predict(inputs_reshaped)

    return predictions.flatten()


if __name__ == "__main__":
    # Example input array
    input_array = np.array([
        [24.7136, 46.6753, 0.5, datetime(2024, 10, 15)],
        [24.7136, 46.6753, 0.6, datetime(2024, 10, 16)],
        [24.7136, 46.6753, 0.4, datetime(2024, 10, 17)]
    ])

    predicted_aots = predict_aot_batch(input_array)

    for i, prediction in enumerate(predicted_aots):
        print(f"Prediction {i+1}: {prediction:.4f}")