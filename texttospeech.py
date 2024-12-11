import streamlit as st
from gtts import gTTS
import os

def text_to_speech(text, lang='en', slow=False):
    # Generate speech
    tts = gTTS(text=text, lang=lang, slow=slow)
    # Save to a file
    tts.save("output.mp3")
    return "output.mp3"

# Streamlit app
st.title("Text-to-Speech Generator")

# Text input
text = st.text_area("Enter the text you want to convert to speech:")

# Language selection
lang = st.selectbox("Select language:", ["en", "es", "fr", "de", "hi"])

# Speed selection
slow = st.checkbox("Slow speech")

if st.button("Convert"):
    if text:
        file_path = text_to_speech(text, lang, slow)
        with open(file_path, 'rb') as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
        os.remove(file_path)
    else:
        st.error("Please enter some text to convert.")






# import streamlit as st
# from gtts import gTTS
# import os

# def text_to_speech(text, lang='en', slow=False):
#     # Generate speech
#     tts = gTTS(text=text, lang=lang, slow=slow)
#     # Save to a file
#     tts.save("output.mp3")
#     return "output.mp3"

# # Streamlit app
# st.title("Text-to-Speech Generator")

# # Sidebar for additional features
# st.sidebar.header("Settings")

# # Text input
# text = st.text_area("Enter the text you want to convert to speech:")

# # Language selection
# lang = st.selectbox("Select language:", ["en", "hi", "mr", "es", "fr", "de"])

# # Speed selection
# slow = st.checkbox("Slow speech")

# # Pitch control
# pitch = st.sidebar.slider("Pitch", 0.5, 2.0, 1.0, 0.1)

# # Volume control
# volume = st.sidebar.slider("Volume", 0.0, 1.0, 1.0, 0.1)

# if st.button("Convert"):
#     if text:
#         file_path = text_to_speech(text, lang, slow)
#         with open(file_path, 'rb') as audio_file:
#             audio_bytes = audio_file.read()
#             st.audio(audio_bytes, format='audio/mp3')
            
#             # Download button
#             st.sidebar.download_button(
#                 label="Download audio",
#                 data=audio_bytes,
#                 file_name="output.mp3",
#                 mime="audio/mp3"
#             )

#         # Remove the file after the download button is created
#         os.remove(file_path)
#     else:
#         st.error("Please enter some text to convert.")
