import streamlit as st
import pandas as pd
import pickle



def predict_crop_yield(parameters):
    # Prepare the input data for prediction
    data = pd.DataFrame(parameters, index=[0])

    # Make the prediction
    prediction = model.predict(data)

    return prediction[0]

def main():
    st.title("Crop Yield Prediction")
    st.write("Enter the following parameters to predict the crop yield:")

    # Get user input for parameters
    temperature = st.number_input("Temperature (in Celsius)", value=25.0, step=1.0)
    rainfall = st.number_input("Rainfall (in mm)", value=100.0, step=1.0)
    humidity = st.number_input("Humidity (in %)", value=50.0, step=1.0)
    ph = st.number_input("pH level", value=6.5, step=0.1)
    crop = st.text_input("Crop")

    parameters = {
        'Temperature': temperature,
        'Rainfall': rainfall,
        'Humidity': humidity,
        'pH': ph,
        'Crop': crop
    }

    if st.button("Predict"):
        # Check for valid crop name
        if not crop:
            st.warning("Please enter the crop name.")
        else:
            # Call the prediction function
            prediction = predict_crop_yield(parameters)

            # Display the prediction
            st.success(f"Predicted crop yield for {crop}: {prediction:.2f} tons/ha")

            # Show model evaluation metrics (you can replace these with your actual evaluation metrics)
            st.write("Model Evaluation Metrics:")
            st.write("Mean Absolute Error (MAE): 2.3")
            st.write("Mean Squared Error (MSE): 8.7")
            st.write("R-squared Score (R2): 0.85")

if __name__ == '__main__':
    main()
