
import numpy as np
import pandas as pd
import pickle
import streamlit as st
import plotly.graph_objects as go
from sklearn.datasets import load_iris

def load_model(model_path="iris_model.pkl"):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model

def construct_sidebar_with_sliders(feature_ranges):
    st.sidebar.markdown(
        '<p class="header-style">Iris Data Classification</p>',
        unsafe_allow_html=True
    )
    inputs = []
    for feature, (min_val, max_val) in feature_ranges.items():
        value = st.sidebar.slider(
            label=f"{feature}",
            min_value=float(min_val),
            max_value=float(max_val),
            value=float((min_val + max_val) / 2),
            step=0.1
        )
        inputs.append(value)
    return inputs

def plot_pie_chart(probabilities, target_names):
    fig = go.Figure(
        data=[go.Pie(
                labels=list(target_names),
                values=probabilities[0]
        )]
    )
    fig = fig.update_traces(
        hoverinfo='label+percent',
        textinfo='value',
        textfont_size=15
    )
    return fig

def display_results(prediction, probabilities, target_names):
    prediction_str = target_names[prediction[0]]
    st.markdown('<p class="header-style">Iris Data Predictions</p>', unsafe_allow_html=True)
    column_1, column_2 = st.columns(2)
    column_1.markdown('<p class="font-style">Prediction</p>', unsafe_allow_html=True)
    column_1.write(prediction_str)

    column_2.markdown('<p class="font-style">Probability</p>', unsafe_allow_html=True)
    column_2.write(f"{probabilities[0][prediction[0]]:.3f}")

    fig = plot_pie_chart(probabilities, target_names)
    st.markdown('<p class="font-style">Probability Distribution</p>', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)

def main():
    st.set_page_config(page_title="Iris Data Classification", layout="centered")

    # Cargar datos y modelo
    iris_data = load_iris()
    features = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
    model = load_model()

    # Obtener rangos para sliders
    feature_ranges = {
        col: (features[col].min(), features[col].max())
        for col in features.columns
    }

    # Inputs del usuario
    user_inputs = construct_sidebar_with_sliders(feature_ranges)
    values_to_predict = np.array(user_inputs).reshape(1, -1)

    # Predicción
    prediction = model.predict(values_to_predict)
    probabilities = model.predict_proba(values_to_predict)

    # Mostrar resultados
    display_results(prediction, probabilities, iris_data.target_names)

if __name__ == "__main__":
    main()