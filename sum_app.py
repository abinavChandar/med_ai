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

    revision = open("revisions.txt", "r")
    revision_1 = revision.read()

    completion1 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": revision_1},
        {"role": "user", "content": transcript}
        ]

    )

    content_with_padding_01 = "\u200B\n\n" + completion1.choices[0].message.content

    return content_with_padding_01


def content2(transcript):

    revision = open("revisions2.txt", "r")
    revision_1 = revision.read()

    completion2 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": revision_1},
        {"role": "user", "content":  transcript}
        ]
    )

    content_with_padding_02 = "\u200B\n\n" + completion2.choices[0].message.content

    return content_with_padding_02

def content3(transcript):

    revision = open("revisions3.txt", "r")
    revision_1 = revision.read()   

    completion3 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": revision_1},
        {"role": "user", "content": transcript}
        ]
    )

    content_with_padding_03 = "\u200B\n\n" + completion3.choices[0].message.content

    return content_with_padding_03


def content4(transcript):

    revision = open("revisions4.txt", "r")
    revision_1 = revision.read()   

    completion4 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": revision_1},
        {"role": "user", "content": transcript}
        ]
    )

    content_with_padding_04 = "\u200B\n\n" + completion4.choices[0].message.content

    return content_with_padding_04


def content5(transcript):

    revision = open("revisions5.txt", "r")
    revision_1 = revision.read()   

    completion5 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": revision_1},
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

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Original", "Complaint", "History", "Emergency", "Assessment", "Plan"])


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

        # temp_dir = tempfile.mkdtemp()
        # path = os.path.join(temp_dir, uploaded_file.name)
        # with open(path, "wb") as f:
        #         f.write(uploaded_file.getvalue())


        content_with_padding_01 = content1(transcript)
        content_with_padding_02 = content2(transcript)

        content_1_2 = content_with_padding_01 + content_with_padding_02

        content_with_padding_03 = content3(content_1_2)

        content_1_2_3 = content_1_2 + content_with_padding_03
        content_with_padding_04 = content4(content_1_2_3)
        content_1_2_3_4 = content_1_2_3 + content_with_padding_04
        content_with_padding_05 = content5(content_1_2_3_4)
        
        # step 3 - transcription and summary
        
        transcription = transcript
        
        content1 = content_with_padding_01  
        content2 = content_with_padding_02
        content3 = content_with_padding_03
        content4 = content_with_padding_04
        content5 = content_with_padding_05

        summary = summary(content1, content2, content3, content4, content5)
        f_1 = open("demofile1.txt", "w")
        f_2 = open("demofile2.txt", "w")
        f_3 = open("demofile3.txt", "w")
        f_4 = open("demofile4.txt", "w")
        f_5 = open("demofile5.txt", "w")
        trans = open("trans.txt", "w")
        trans.write(transcription)
        trans.close()
        f_1.write(content1)
        f_1.close()
        f_2.write(content2)
        f_2.close()
        f_3.write(content3)
        f_3.close()        
        f_4.write(content4)
        f_4.close()
        f_5.write(content5)
        f_5.close()
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


    



    f_1 = open("demofile1.txt", "r")
    f_2 = open("demofile2.txt", "r")
    f_3 = open("demofile3.txt", "r")
    f_4 = open("demofile4.txt", "r")
    f_5 = open("demofile5.txt", "r")
    trans = open("trans.txt", "r")
 
    content_1 = f_1.read()
    content_2 = f_2.read()
    content_3 = f_3.read()
    content_4 = f_4.read()
    content_5 = f_5.read()
    transcription_1 = trans.read()
    #txt = "Please Change the patient name to Abinav"

    summary = content_1 + content_2 + content_3 + content_4 + content_5




    st.header('One Liner with Chief Complaint:')
    st.success(content_1)
    rev = open("revisions.txt", "r")
    placeholder = rev.read()

    txt = st.text_area(
    "Add Revisions for One Liner with Chief Complaint",
    placeholder,
    )


    if st.button("Revise Chief Complaint Note", type="primary"):

        content_with_padding_01 = revise(transcription_1, txt)
        rev = open("revisions.txt", "w")
        rev.write(txt)
        rev.close()

        st.header('Revised Note')
        st.success(content_with_padding_01)





with tab3:


    



    f_1 = open("demofile1.txt", "r")
    f_2 = open("demofile2.txt", "r")
    f_3 = open("demofile3.txt", "r")
    f_4 = open("demofile4.txt", "r")
    f_5 = open("demofile5.txt", "r")
    trans = open("trans.txt", "r")
 
    content_1 = f_1.read()
    content_2 = f_2.read()
    content_3 = f_3.read()
    content_4 = f_4.read()
    content_5 = f_5.read()
    transcription_1 = trans.read()
    summary = content_1 + content_2 + content_3 + content_4 + content_5
    #txt = "Please Change the patient name to Abinav"




    st.header('History of Present Illness (HPI)')
    st.success(content_2)
    rev = open("revisions2.txt", "r")
    placeholder = rev.read()

    txt = st.text_area(
    "Add Revisions for HPI",
    placeholder,
    )


    if st.button("Revise HPI Note", type="primary"):

        content_with_padding_01 = revise(transcription_1, txt)
        rev = open("revisions2.txt", "w")
        rev.write(txt)
        rev.close()

        st.header('Revised Note')
        st.success(content_with_padding_01)




with tab4:



    f_1 = open("demofile1.txt", "r")
    f_2 = open("demofile2.txt", "r")
    f_3 = open("demofile3.txt", "r")
    f_4 = open("demofile4.txt", "r")
    f_5 = open("demofile5.txt", "r")
    trans = open("trans.txt", "r")
 
    content_1 = f_1.read()
    content_2 = f_2.read()
    content_3 = f_3.read()
    content_4 = f_4.read()
    content_5 = f_5.read()
    transcription_1 = trans.read()
    summary = content_1 + content_2 
    #txt = "Please Change the patient name to Abinav"




    st.header('Emergency Department Course (ED Course)')
    st.success(content_3)
    rev = open("revisions3.txt", "r")
    placeholder = rev.read()

    txt = st.text_area(
    "Add Revisions for ED",
    placeholder,
    )


    if st.button("Revise ED Note", type="primary"):

        content_with_padding_01 = revise(summary, txt)
        rev = open("revisions3.txt", "w")
        rev.write(txt)
        rev.close()

        st.header('Revised Note')
        st.success(content_with_padding_01)


with tab5:



    f_1 = open("demofile1.txt", "r")
    f_2 = open("demofile2.txt", "r")
    f_3 = open("demofile3.txt", "r")
    f_4 = open("demofile4.txt", "r")
    f_5 = open("demofile5.txt", "r")
    trans = open("trans.txt", "r")
 
    content_1 = f_1.read()
    content_2 = f_2.read()
    content_3 = f_3.read()
    content_4 = f_4.read()
    content_5 = f_5.read()
    transcription_1 = trans.read()
    summary = content_1 + content_2 + content_3 
    #txt = "Please Change the patient name to Abinav"




    st.header('Clinical Assessment:')
    st.success(content_4)
    rev = open("revisions4.txt", "r")
    placeholder = rev.read()

    txt = st.text_area(
    "Add Revisions for Assessment",
    placeholder,
    )


    if st.button("Revise Assessment Note", type="primary"):

        content_with_padding_01 = revise(summary, txt)
        rev = open("revisions4.txt", "w")
        rev.write(txt)
        rev.close()

        st.header('Revised Note')
        st.success(content_with_padding_01)


with tab6:



    f_1 = open("demofile1.txt", "r")
    f_2 = open("demofile2.txt", "r")
    f_3 = open("demofile3.txt", "r")
    f_4 = open("demofile4.txt", "r")
    f_5 = open("demofile5.txt", "r")
    trans = open("trans.txt", "r")
 
    content_1 = f_1.read()
    content_2 = f_2.read()
    content_3 = f_3.read()
    content_4 = f_4.read()
    content_5 = f_5.read()
    transcription_1 = trans.read()
    summary = content_1 + content_2 + content_3 + content_4 
    #txt = "Please Change the patient name to Abinav"




    st.header('Clinical Plan:')
    st.success(content_5)
    rev = open("revisions5.txt", "r")
    placeholder = rev.read()

    txt = st.text_area(
    "Add Revisions for Plan",
    placeholder,
    )


    if st.button("Revise Plan Note", type="primary"):

        content_with_padding_01 = revise(summary, txt)
        rev = open("revisions5.txt", "w")
        rev.write(txt)
        rev.close()

        st.header('Revised Note')
        st.success(content_with_padding_01)






    # st.header('History of Present Illness (HPI)')
    # st.success(content_2)

    # txt3 = st.text_area(
    # "Add Revisions",
    # "",
    # )


    # if st.button("Revise", type="primary"):

    #     content_with_padding_02 = revise(content_2, txt3)
    #     rev = open("revisions.txt", "w")
    #     rev.write(txt3)
    #     rev.close()

    #     st.header('Revised Note')
    #     st.success(content_with_padding_02)

    # st.header('Emergency Department Course (ED Course)')
    # st.success(content_3)


    # txt3 = st.text_area(
    # "Add Revisions",
    # "",
    # )

    # if st.button("Revise", type="primary"):

    #     content_with_padding_03 = revise(content_3, txt3)
    #     rev = open("revisions.txt", "w")
    #     rev.write(txt3)
    #     rev.close()

    #     st.header('Revised Note')
    #     st.success(content_with_padding_03)

    # st.header('Clinical Assessment:')
    # st.success(content_4)

    # txt4 = st.text_area(
    # "Add Revisions",
    # "",
    # )



    # if st.button("Revise", type="primary"):

    #     content_with_padding_04 = revise(content_4, txt4)
    #     rev = open("revisions.txt", "w")
    #     rev.write(txt4)
    #     rev.close()

    #     st.header('Revised Note')
    #     st.success(content_with_padding_04)



    # st.header('Clinical Plan:')
    # st.success(content_5)


    # txt5 = st.text_area(
    # "Add Revisions",
    # "",
    # )


    # if st.button("Revise", type="primary"):

    #     content_with_padding_05 = revise(content_5, txt5)
    #     rev = open("revisions.txt", "w")
    #     rev.write(txt5)
    #     rev.close()

    #     st.header('Revised Note')
    #     st.success(content_with_padding_05)    









    

    