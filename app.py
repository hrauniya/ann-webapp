# flake8:noqa
import streamlit as st


st.header("Artificial Neural Network for Classification(Single Layer)")
data_set = st.file_uploader("Upload a suitable dataset!")
number_neurons = st.slider("Pick the number of neurons that you want to have in the hidden layer",0,50)
learning_rate = st.slider("Pick learning rate",0.000, 1.000)
training_percentage = st.slider("What percentage of the dataset do you want to use for training?",0,100)
train_model =st.button("Train Model!")


