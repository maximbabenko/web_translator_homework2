from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_model():
    model = pipeline('translation_ru_to_en', 'Helsinki-NLP/opus-mt-ru-en')
    return model

model = load_model()

st.title('Переводчик с русского на английский')

text = st.text_input('Введите текст')

translate = st.button('Перевести')

if translate:
    out = model(text)
    st.write('Результат')
    st.success(out)
