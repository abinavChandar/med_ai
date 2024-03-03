import streamlit as st
import requests
import zipfile 
import json
from time import sleep
import os
import urllib.request
from openai import OpenAI
from contextlib import redirect_stdout
import aiofiles

import pandas as pd






print("hello")

client = OpenAI(api_key='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')



def content1(transcript):

    completion1 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "Provide a concise one liner including key elements of patient's past medical history and ending with their chief clinical complaint and the duration of the the chief complaint:"},
        {"role": "user", "content": transcript}
        ]

    )

    content_with_padding_01 = "\u200B\n\n" + completion1.choices[0].message.content

    return content_with_padding_01


def content2(transcript):

    completion2 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "Provide the History of Present Illness, including how and when patient initially started to experience signs and symptoms, what prompted them to present to the hospital, as well as what diagnostics and initial treatments provided by EMS or the emergency department, if applicable. End with a report of how the patient's signs and symptoms are currently. "},
        {"role": "user", "content":  transcript}
        ]
    )

    content_with_padding_02 = "\u200B\n\n" + completion2.choices[0].message.content

    return content_with_padding_02

def content3(transcript):

    completion3 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "Provide a short summmary of the key elements of the patients past medical history and history of present illness that you think would be the most helpful in generating differential clinical diagnoses. This list should be no longer than 10 items.:"},
        {"role": "user", "content": transcript}
        ]
    )

    content_with_padding_03 = "\u200B\n\n" + completion3.choices[0].message.content

    return content_with_padding_03


def content4(transcript):

    completion4 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "Provide a clinical assessment based on the past medical history and history of present illness. This assessment should include a number of top clinical differentials in descending order of probability. It should also provide a preliminary assessment of the clinical prognosis for the patient and comment on their current clinical stability.:"},
        {"role": "user", "content": transcript}
        ]
    )

    content_with_padding_04 = "\u200B\n\n" + completion4.choices[0].message.content

    return content_with_padding_04


def content5(transcript):

    completion5 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "Provide a Clinical Plan according to the clinical assessment above. The plan should be organized by clinical problem, in descending order of clinical significance and each problem's clincial plan should include several elements: a summary of the problem based on key elements of the history, consultant services that need to be contacted, specific diagnostics tests, imaging, and cultures that need to be ordered, and finally specific treatments, including surgical procedures, medications and calculate the specific dosages typically indicated for the condition. IF the dosaage is non-standard, please provide a weight-based dosage recommendation according to clinical and pharmacological guidelines."},
        {"role": "user", "content":  transcript}
        ]
    )

    content_with_padding_05 = "\u200B\n\n" + completion5.choices[0].message.content

    return content_with_padding_05


def summary(content1, content2, content3, content4, content5):

    summary = content1 + content2 + content3 + content4 + content5

    return summary


def revise(summary_txt, revisions):

    completion6 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": revisions},
        {"role": "user", "content":  summary_txt}
        ]
    )

    content_with_padding_06 = "\u200B\n\n" + completion6.choices[0].message.content

    return content_with_padding_06




def save_files(transcription,summary):

    with open('transcript.txt', 'w') as f:
        f.write(transcription)
        f.close()
    with open('summary.txt', 'w') as f:
        f.write(summary)
        f.close()    
    list_files = ['transcript.txt','summary.txt']
    with zipfile.ZipFile('final.zip', 'w') as zipF:
      for file in list_files:
         zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)
      zipF.close()




# title of web app


st.markdown('# **SmartEHR SEHRA MediNoti**')
bar = st.progress(0)

#st.sidebar.header('Input parameter')

tab1, tab2 = st.tabs(["Original", "Revisions"])


with tab1:

    with st.sidebar.form(key='my_form'):
        #episode_id = st.text_input('Insert Episode ID:')
        #bbc965b98747439abf0fe5c1a5ddfe5c
        #e9baa9118e654cd09baff7ac4b67228f
        uploaded_file = st.file_uploader("Choose a file")
        submit_button = st.form_submit_button(label='Submit')
        





    if submit_button:

        #audio_file = bytes_data
        #audio_file = open(audio_file, "rb")
        transcript = client.audio.transcriptions.create(
        model="whisper-1", 
        file=uploaded_file, 
        response_format="text"
        )


        content_with_padding_01 = content1(transcript)
        content_with_padding_02 = content2(transcript)
        content_with_padding_03 = content3(transcript)
        content_with_padding_04 = content4(transcript)
        content_with_padding_05 = content5(transcript)
        
        # step 3 - transcription and summary
        
        transcription = transcript
        
        content1 = content_with_padding_01  
        content2 = content_with_padding_02
        content3 = content_with_padding_03
        content4 = content_with_padding_04
        content5 = content_with_padding_05

        summary = summary(content1, content2, content3, content4, content5)
        f = open("demofile3.txt", "w")
        f.write(summary)
        f.close()
        

        #bar.progress(100)

            


        st.header('Transcription')
        st.success(transcription)
        st.header('One Liner with Chief Complaint:')
        st.success(content1)
        st.header('History of Present Illness (HPI)')
        st.success(content2)
        st.header('Emergency Department Course (ED Course)')
        st.success(content3)
        st.header('Clinical Assessment:')
        st.success(content4)
        st.header('Clinical Plan:')
        st.success(content5)
        save_files(transcription,summary)
        with open("final.zip", "rb") as zip_download:
            btn = st.download_button(
                label="Download",
                data=zip_download,
                file_name="final.zip",
                mime="application/zip"
            )

with tab2:

    txt = st.text_area(
    "Add Revisions",
    "",
    )

    



    f = open("demofile3.txt", "r")
 
    summary_txt = f.read()
    #txt = "Please Change the patient name to Abinav"

    if st.button("Revise", type="primary"):

        content_with_padding_06 = revise(summary_txt, txt)

        st.header('Revised Note')
        st.success(content_with_padding_06)


    st.success(summary)

    









    

    