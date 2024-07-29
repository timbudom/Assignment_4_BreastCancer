# Breast Cancer Data Analysis and Prediction

This project involves the analysis of a breast cancer dataset, implementation of an Artificial Neural Network (ANN) model, and building an interactive web application using Streamlit.

## Steps

1. **Data Preparation, Feature Selection, and Model Training**: Run the `main.py` script.
2. **Prediction on New Data**: Use the `predict.py` script to make predictions.
3. **Streamlit App**: Run the `app.py` script to interact with the dataset and make predictions.

## How to Run

1. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the main script for data preparation, feature selection, and model training:
    ```sh
    python main.py
    ```

4. Use the prediction script to make predictions on new data:
    ```sh
    python predict.py
    ```

5. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

## Project Structure

- `main.py`: Script for data preparation, feature selection, and model training.
- `predict.py`: Script for making predictions on new data.
- `app.py`: Streamlit app for making predictions.
- `requirements.txt`: List of dependencies.
- `README.md`: Documentation of the project.

## Dataset

The dataset used in this project is the Breast Cancer dataset, which can be downloaded from the UCI Machine Learning Repository, Kaggle, or obtained from sklearn.
