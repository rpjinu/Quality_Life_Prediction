# Quality_Life_Prediction
"This project involves building a Streamlit app that takes user inputs for various quality-of-life metrics, processes them through a pre-trained machine learning pipeline, and predicts the Quality of Life Value."

<img src="">

# Quality of Life Prediction Web App

This project is a **Streamlit-based web application** that predicts the `Quality of Life Value` based on various metrics such as purchasing power, safety, healthcare, climate, and more. Users input the metrics through an interactive interface, and a pre-trained machine learning model predicts the quality of life value based on their inputs.

---

## Features

- **User-Friendly Interface**: Built with Streamlit, allowing users to input 17 metrics easily.
- **Real-Time Predictions**: Provides immediate predictions for `Quality of Life Value`.
- **Pre-Trained Model**: Uses a machine learning pipeline trained on a dataset with quality-of-life metrics.
- **Scalable and Modular**: Can be extended for additional metrics or categories.

---

## Input Metrics

The app takes the following 17 inputs:

1. **Purchasing Power Value** (Numeric)
2. **Purchasing Power Category** (Categorical: Very Low, Low, Moderate, High, Very High)
3. **Safety Value** (Numeric)
4. **Safety Category** (Categorical: Very Low, Low, Moderate, High, Very High)
5. **Health Care Value** (Numeric)
6. **Health Care Category** (Categorical: Very Low, Low, Moderate, High, Very High)
7. **Climate Value** (Numeric)
8. **Climate Category** (Categorical: Very Low, Low, Moderate, High, Very High)
9. **Cost of Living Value** (Numeric)
10. **Cost of Living Category** (Categorical: Very Low, Low, Moderate, High, Very High)
11. **Property Price to Income Value** (Numeric)
12. **Property Price to Income Category** (Categorical: Very Low, Low, Moderate, High, Very High)
13. **Traffic Commute Time Value** (Numeric)
14. **Traffic Commute Time Category** (Categorical: Very Low, Low, Moderate, High, Very High)
15. **Pollution Value** (Numeric)
16. **Pollution Category** (Categorical: Very Low, Low, Moderate, High, Very High)
17. **Quality of Life Category** (Categorical: Very Low, Low, Moderate, High, Very High)

---

## Prediction Target

The application predicts the **Quality of Life Value**, which represents a numeric score associated with the overall quality of life based on the input metrics.

---

## Technologies Used

- **Python**: For backend logic and model integration.
- **Streamlit**: To create an interactive and user-friendly web interface.
- **Machine Learning**: A pre-trained pipeline model (scikit-learn or similar) for prediction.
- **pandas**: For data processing and formatting.
- **joblib**: For loading the saved ML pipeline model.

---

## How It Works

1. **User Input**: The user provides inputs for all 17 metrics via the Streamlit interface.
2. **Data Preprocessing**: The app processes the input data to match the model's expected format.
3. **Model Prediction**: The pre-trained pipeline model predicts the `Quality of Life Value`.
4. **Result Display**: The app displays the predicted value on the screen.

---

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/quality-of-life-prediction.git
   cd quality-of-life-prediction
