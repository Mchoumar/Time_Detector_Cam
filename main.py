import streamlit as st
import cv2 as cv
from datetime import datetime

# Setup for the website
st.title("Motion Detector")
start = st.button("Start Camera")

# Once start button is pressed it starts the recording
if start:
    streamlit_image = st.image([])
    camera = cv.VideoCapture(0)
    while True:
        check, frame = camera.read()
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        now = datetime.now()

        cv.putText(img=frame, text=now.strftime("%A"), org=(50, 50),
                   fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 255, 255),
                   thickness=2, lineType=cv.LINE_AA)
        cv.putText(img=frame, text=now.strftime("%H:%M:%S"), org=(50, 75),
                   fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 0, 0),
                   thickness=2, lineType=cv.LINE_AA)
        streamlit_image.image(frame)
