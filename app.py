import streamlit as st
from google import genai
from google.genai import types
from io import BytesIO
from PIL import Image

##AIzaSyA5Tk-ApYxVils7bEk4ZD9usbLLeol8wm8

myrobo = genai.Client(api_key="AIzaSyA5Tk-ApYxVils7bEk4ZD9usbLLeol8wm8")

col1,col2=st.columns(2)

with col1:
    st.title("Describe Your Image...")
    user_data=st.text_area(" ")
    if st.button("Visualize"):
        response=myrobo.models.generate_content(model="gemini-2.5-flash-preview-image-generation",
                                contents=user_data,
                                config=types.GenerateContentConfig(
                                response_modalities=['TEXT','IMAGE']))
        for part in response.candidates[0].content.parts:
            if part.text is not None:
                print(part.text)
            elif part.inline_data is not None:
                image=Image.open(BytesIO((part.inline_data.data)))
                image.save("MyImage.png")
with col2:
    if st.image("MyImage.png"):
        st.write("Your Image is now Generated")
    else:
        st.write("Waiting for your response..")
