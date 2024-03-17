import streamlit as st
import authenticate as authenticate
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

import json

import random
import mysql.connector
import time

st.set_page_config(
    page_title="SEHRA",
    page_icon="👋",
)
st.write("# SEHRA 👋")
st.markdown(
    """
    ### For clinicians, SEHRA is your one-stop solution for:
    - Real-time, automatic, reliable clinical note documentation
    - Seamless clinical AI support for generation of assessment and plan based on
      latest guidelines and standards-of-care
    - Reducing burnout related to documentation burden
    ### For hospitals/clinics, SEHRA is your one-stop solution for:
    - Improving patient outcomes by ensuring consistently high standards-of-care
    - Reducing potential legal exposure through safeguarding comprehensive
      clinical documentation
    - Increasing clinician efficiency and enhancing operational capacity
    - Bolstering clinician satisfaction and fostering a healthier work environment
"""
)

print("hello")

client = OpenAI(api_key='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')



def content1(transcript):

    revision = open("prompt_oneline.txt", "r")
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

    revision = open("prompt_hist.txt", "r")
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

    revision = open("prompt_key.txt", "r")
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

    revision = open("prompt_assessment.txt", "r")
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

    revision = open("prompt_plan.txt", "r")
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





def content1_style(transcript, user_email):

    revision = open(user_email + "_prompt_style_oneline.txt", "r")
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


def content2_style(transcript, user_email):

    revision = open(user_email + "_prompt_style_hist.txt", "r")
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

def content3_style(transcript, user_email):

    revision = open(user_email + "_prompt_style_key.txt", "r")
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


def content4_style(transcript, user_email):

    revision = open(user_email + "_prompt_style_assessment.txt", "r")
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


def content5_style(transcript, user_email):

    revision = open(user_email + "_prompt_style_plan.txt", "r")
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


def generate_transcription(query):

    revision = open("example_transcripts.txt", "r")
    revision_1 = revision.read()  

    completion5 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": revision_1},
        {"role": "user", "content":  query}
        ]
    )

    content_with_padding_05 = "\u200B\n\n" + completion5.choices[0].message.content

    return content_with_padding_05






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









# Check authentication when user lands on the home page.
authenticate.set_st_state_vars()
# Add login/logout buttons
if st.session_state["authenticated"]:






    db = mysql.connector.connect(
    host='45.79.3.82',user='dbuser',password='Abinav2016$',database='med_ai', port=3306
    )

    # db = mysql.connector.connect(
    # host='localhost',user='abinav',password='Tvzu[sNxjFM34)iQ',database='med_ai'
    # )
         
    # Create a cursor object
    cursor = db.cursor()
    cursor_prompt = db.cursor()


    #st.markdown('# SEHRA')
    bar = st.progress(0)


    # user_info = open("user_info.txt", "w")
    # user_info.write(str(st.session_state["user_cognito_groups"]))
    # user_info.write(str(st.session_state["user_email"]))
    # user_info.close()

    user_email = str(st.session_state["user_email"])
    user_role = str(st.session_state["user_cognito_groups"])



    #st.success(st.session_state["user_email"])
    authenticate.button_logout()


    tab1, tab2, tab3, tab4 = st.tabs(["Original", "Revisions", "Examples", "Edit"])

    # cursor.execute("SELECT * FROM examples ")
    # #cursor_prompt.execute("SELECT * FROM prompts") 

    # result_promptfile = cursor.fetchall()

    # if user_role != "['Admin']":

    #         user_prompt_style_oneline = open(user_email + "_prompt_style_oneline.txt","w+")
    #         user_prompt_style_hist = open(user_email + "_prompt_style_hist.txt","w+")
    #         user_prompt_style_key = open(user_email + "_prompt_style_key.txt","w+")
    #         user_prompt_style_assessment = open(user_email + "_prompt_style_assessment.txt","w+")
    #         user_prompt_style_plan = open(user_email + "_prompt_style_plan.txt","w+")
        


    sql_role_admin = "SELECT * FROM examples WHERE role = %s"
    user_role_admin = ["['Admin']"]
    cursor.execute(sql_role_admin, user_role_admin)
    admin_examples = cursor.fetchall()


    # sql_role_reg = "SELECT * FROM examples WHERE user = %s"
    # user_role_reg = [user_email]
    # cursor.execute(sql_role_reg, user_role_reg)
    # reg_examples = cursor.fetchall()

    #result_actual = cursor_prompt.fetchall()

    prompt1 = open("prompt1.txt", "r")
    prompt2 = open("prompt2.txt", "r")
    prompt3 = open("prompt3.txt", "r")
    prompt4 = open("prompt4.txt", "r")
    prompt5 = open("prompt5.txt", "r")

    prompt_1 = prompt1.read()
    prompt_2 = prompt2.read()
    prompt_3 = prompt3.read()
    prompt_4 = prompt4.read()
    prompt_5 = prompt5.read()
    prompt1.close()
    prompt2.close()
    prompt3.close()
    prompt4.close()
    prompt5.close()

    # user_prompt_style_oneline.write("Please generate the One Liner of Complaint in the style of the following examples" + '\n' + '\n')
    # user_prompt_style_hist.write("Please generate the History of Present Illness in the style of the following examples" + '\n' + '\n')
    # user_prompt_style_key.write("Please generate the Key Elements in the style of the following examples" + '\n' + '\n')
    # user_prompt_style_assessment.write("Please generate the Clinical Assessment in the style of the following examples" + '\n' + '\n')
    # user_prompt_style_plan.write("Please generate the Clinical Plan in the style of the following examples" + '\n' + '\n')


    prompt_oneline = open("prompt_oneline.txt", "w+")
    prompt_hist = open("prompt_hist.txt", "w+")
    prompt_key = open("prompt_key.txt", "w+")
    prompt_assessment = open("prompt_assessment.txt", "w+")
    prompt_plan = open("prompt_plan.txt", "w+")

    prompt_oneline.write(prompt_1 + '\n' + '\n')
    prompt_hist.write(prompt_2 + '\n' + '\n')
    prompt_key.write(prompt_3 + '\n' + '\n')
    prompt_assessment.write(prompt_4 + '\n' + '\n')
    prompt_plan.write(prompt_5 + '\n' + '\n')


    for row in admin_examples: 
        prompt_oneline.write("Example " + str(row[0]) + ":" + '\n' + '\n')
        prompt_oneline.write("Transcription: " + '\n' + '\n' + str(row[1]) + '\n'+ '\n')
        prompt_oneline.write('\n' + str(row[2]) + '\n'+ '\n')

    

    for row in admin_examples: 
        prompt_hist.write("Example " + str(row[0]) + ":" + '\n' + '\n')
        prompt_hist.write("Transcription: " + '\n' + '\n' + str(row[1]) + '\n'+ '\n')
        #prompt_hist.write("One Liner of Complaint: " + '\n' + '\n' + str(row[2]) + '\n'+ '\n')
        prompt_hist.write( '\n' + str(row[3]) + '\n'+ '\n')


    

    for row in admin_examples: 
        prompt_key.write("Example " + str(row[0]) + ":" + '\n' + '\n')
        prompt_key.write("Transcription: " + '\n' + '\n' + str(row[1]) + '\n'+ '\n')
        prompt_key.write( '\n' + str(row[2]) + '\n'+ '\n')
        prompt_key.write('\n' + str(row[3]) + '\n'+ '\n')
        prompt_key.write('\n' + str(row[4]) + '\n'+ '\n')


    


    for row in admin_examples: 
        prompt_assessment.write("Example " + str(row[0]) + ":" + '\n' + '\n')
        prompt_assessment.write("Transcription: " + '\n' + '\n' + str(row[1]) + '\n'+ '\n')
        prompt_assessment.write( '\n' + str(row[2]) + '\n'+ '\n')
        prompt_assessment.write( '\n' + str(row[3]) + '\n'+ '\n')
        prompt_assessment.write('\n' + str(row[4]) + '\n'+ '\n')
        prompt_assessment.write( '\n' + str(row[5]) + '\n'+ '\n')
        

    


    for row in admin_examples: 
        prompt_plan.write("Example " + str(row[0]) + ":" + '\n' + '\n')
        prompt_plan.write("Transcription: " + '\n' + '\n' + str(row[1]) + '\n'+ '\n')
        prompt_plan.write( '\n' + str(row[2]) + '\n'+ '\n')
        prompt_plan.write( '\n' + str(row[3]) + '\n'+ '\n')
        prompt_plan.write('\n' + str(row[4]) + '\n'+ '\n')
        prompt_plan.write('\n' + '\n' + str(row[5]) + '\n'+ '\n')
        prompt_plan.write('\n' + str(row[6]) + '\n'+ '\n')




    prompt_oneline.write("Example: {}"'\n' + '\n' + "One Liner of Complaint: ")
    prompt_hist.write("Example:{}"'\n' + '\n' + "History of Present Illness: ")
    prompt_key.write("Example: {}"'\n' + '\n' + "Key Elements: ")
    prompt_assessment.write("Example: {}"'\n' + '\n' + "Clinical Assessment: ")
    prompt_plan.write("Example: {}"'\n' + '\n' + "Clinical Plan: ")


    
    prompt_oneline.close()
    prompt_hist.close()
    prompt_key.close()
    prompt_plan.close()
    prompt_assessment.close()


    # for row in reg_examples: 
    #     user_prompt_style_oneline.write("Example " + ":" + '\n' + '\n')
    #     user_prompt_style_oneline.write(row[2] + '\n'+ '\n')


    # for row in reg_examples: 
    #     user_prompt_style_hist.write("Example " + ":" + '\n' + '\n')
    #     user_prompt_style_hist.write(row[3] + '\n'+ '\n')
        

    # for row in reg_examples: 
    #     user_prompt_style_key.write("Example " + ":" + '\n' + '\n')
    #     user_prompt_style_key.write(row[4] + '\n'+ '\n')


    # for row in reg_examples: 
    #     user_prompt_style_assessment.write("Example " + ":" + '\n' + '\n')
    #     user_prompt_style_assessment.write(row[5] + '\n'+ '\n')


    # for row in reg_examples: 
    #     user_prompt_style_plan.write("Example " + ":" + '\n' + '\n')
    #     user_prompt_style_plan.write(row[6] + '\n'+ '\n') 


    # user_prompt_style_oneline.close()
    # user_prompt_style_hist.close()
    # user_prompt_style_key.close()
    # user_prompt_style_assessment.close()
    # user_prompt_style_plan.close()


    with tab1:

        with st.sidebar.form(key='my_form'):
            #episode_id = st.text_input('Insert Episode ID:')
            #bbc965b98747439abf0fe5c1a5ddfe5c
            #e9baa9118e654cd09baff7ac4b67228f
            uploaded_file = st.file_uploader("Choose a file")
            submit_button = st.form_submit_button(label='Submit')
            if user_role == "['Admin']":

                st.success("Administrator")
                st.write(user_email)
            else:
                st.write(user_email)



        example_transcripts = open("example_transcripts.txt", "w+")

        example_transcripts.write("Please generate a conversation between the Patient and Physician with extreme detail and make sure it imitates the following examples." + '\n' + '\n')

        sql_role_admin = "SELECT * FROM examples WHERE role = %s"
        user_role_admin = ["['Admin']"]
        cursor.execute(sql_role_admin, user_role_admin)
        admin_examples = cursor.fetchall()


        for row in admin_examples: 
            example_transcripts.write("Example " + str(row[0]) + ":" + '\n' + '\n')
            example_transcripts.write("Transcription: " + '\n' + '\n' + str(row[1]) + '\n'+ '\n')

        





        if submit_button:

            #audio_file = bytes_data
            #audio_file = open(audio_file, "rb")
            transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=uploaded_file, 
            response_format="text"
            )



            if user_role == "['Admin']":

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
                f_1 = open("demofile1.txt", "w+")
                f_2 = open("demofile2.txt", "w+")
                f_3 = open("demofile3.txt", "w+")
                f_4 = open("demofile4.txt", "w+")
                f_5 = open("demofile5.txt", "w+")
                trans = open("trans.txt", "w+")
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



                    


                st.header('Transcription')
                st.success(transcription)
                st.header('One Liner with Chief Complaint:')
                st.success(content1)
                st.header('History of Present Illness (HPI)')
                st.success(content2)
                st.header('Key Elements')
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




            else: 


                user_prompt_style_oneline = open(user_email + "_prompt_style_oneline.txt","w+")
                user_prompt_style_hist = open(user_email + "_prompt_style_hist.txt","w+")
                user_prompt_style_key = open(user_email + "_prompt_style_key.txt","w+")
                user_prompt_style_assessment = open(user_email + "_prompt_style_assessment.txt","w+")
                user_prompt_style_plan = open(user_email + "_prompt_style_plan.txt","w+")

                user_prompt_style_oneline.write("Please generate the One Liner of Complaint in the style of the following examples" + '\n' + '\n')
                user_prompt_style_hist.write("Please generate the History of Present Illness in the style of the following examples" + '\n' + '\n')
                user_prompt_style_key.write("Please generate the Key Elements in the style of the following examples" + '\n' + '\n')
                user_prompt_style_assessment.write("Please generate the Clinical Assessment in the style of the following examples" + '\n' + '\n')
                user_prompt_style_plan.write("Please generate the Clinical Plan in the style of the following examples" + '\n' + '\n')

                sql_role_reg = "SELECT * FROM examples WHERE user = %s"
                user_role_reg = [user_email]
                cursor.execute(sql_role_reg, user_role_reg)
                reg_examples = cursor.fetchall()


                for row in reg_examples: 
                    user_prompt_style_oneline.write("Example " + ":" + '\n' + '\n')
                    user_prompt_style_oneline.write(row[2] + '\n'+ '\n')


                for row in reg_examples: 
                    user_prompt_style_hist.write("Example " + ":" + '\n' + '\n')
                    user_prompt_style_hist.write(row[3] + '\n'+ '\n')
                    

                for row in reg_examples: 
                    user_prompt_style_key.write("Example " + ":" + '\n' + '\n')
                    user_prompt_style_key.write(row[4] + '\n'+ '\n')


                for row in reg_examples: 
                    user_prompt_style_assessment.write("Example " + ":" + '\n' + '\n')
                    user_prompt_style_assessment.write(row[5] + '\n'+ '\n')


                for row in reg_examples: 
                    user_prompt_style_plan.write("Example " + ":" + '\n' + '\n')
                    user_prompt_style_plan.write(row[6] + '\n'+ '\n') 


                user_prompt_style_oneline.close()
                user_prompt_style_hist.close()
                user_prompt_style_key.close()
                user_prompt_style_assessment.close()
                user_prompt_style_plan.close()



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

                content1_style = content1_style(content1, user_email)
                content2_style = content2_style(content2, user_email)
                content3_style = content3_style(content3, user_email)
                content4_style = content4_style(content4, user_email)
                content5_style = content5_style(content5, user_email)

                summary = summary(content1_style, content2_style, content3_style, content4_style, content5_style)
                f_1 = open("demofile1.txt", "w+")
                f_2 = open("demofile2.txt", "w+")
                f_3 = open("demofile3.txt", "w+")
                f_4 = open("demofile4.txt", "w+")
                f_5 = open("demofile5.txt", "w+")
                trans = open("trans.txt", "w+")
                trans.write(transcription)
                trans.close()
                f_1.write(content1_style)
                f_1.close()
                f_2.write(content2_style)
                f_2.close()
                f_3.write(content3_style)
                f_3.close()        
                f_4.write(content4_style)
                f_4.close()
                f_5.write(content5_style)
                f_5.close()



                    


                st.header('Transcription')
                st.success(transcription)
                st.header('One Liner with Chief Complaint:')
                st.success(content1_style)
                st.header('History of Present Illness (HPI)')
                st.success(content2_style)
                st.header('Key Elements')
                st.success(content3_style)
                st.header('Clinical Assessment:')
                st.success(content4_style)
                st.header('Clinical Plan:')
                st.success(content5_style)
                save_files(transcription,summary)
                with open("final.zip", "rb") as zip_download:
                    btn = st.download_button(
                        label="Download",
                        data=zip_download,
                        file_name="final.zip",
                        mime="application/zip"
                    )


        

        gen_trans = st.text_area(
        "Describe a patient encounter to generate conversation",
        height=100
        )


        gen_transcript = generate_transcription(gen_trans)
        st.header('Generated Transcription')
        st.success(gen_transcript)

        if st.button("Generate Clinical Note with this Transcription", type="primary"):

            content_with_padding_01 = content1(gen_transcript)
            content_with_padding_02 = content2(gen_transcript)

            content_1_2 = content_with_padding_01 + content_with_padding_02

            content_with_padding_03 = content3(content_1_2)

            content_1_2_3 = content_1_2 + content_with_padding_03
            content_with_padding_04 = content4(content_1_2_3)
            content_1_2_3_4 = content_1_2_3 + content_with_padding_04
            content_with_padding_05 = content5(content_1_2_3_4)
            
            # step 3 - transcription and summary
            
            transcription = gen_transcript
            
            content1 = content_with_padding_01  
            content2 = content_with_padding_02
            content3 = content_with_padding_03
            content4 = content_with_padding_04
            content5 = content_with_padding_05

            summary = summary(content1, content2, content3, content4, content5)
            f_1 = open("demofile1.txt", "w+")
            f_2 = open("demofile2.txt", "w+")
            f_3 = open("demofile3.txt", "w+")
            f_4 = open("demofile4.txt", "w+")
            f_5 = open("demofile5.txt", "w+")
            trans = open("trans.txt", "w+")
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



                


            st.header('Transcription')
            st.success(transcription)
            st.header('One Liner with Chief Complaint:')
            st.success(content1)
            st.header('History of Present Illness (HPI)')
            st.success(content2)
            st.header('Key Elements')
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
        # with open('sample.json', 'r') as file:
        # # Load JSON data from file
        #     data = json.load(file)

        summary = content_1 + content_2 + content_3 + content_4 + content_5

        trans = transcription_1
        complaint = content_1
        hist = content_2
        emergency = content_3
        assessment = content_4
        plan = content_5



        st.header('Transcription')
        st.success(trans)

        st.header('Casename')

        txt_0 = st.text_area(
        "Add a casename to this note",
        height=100
        )


        st.header('One Liner with Chief Complaint:')
        st.success(complaint)
        rev = open("revisions.txt", "r")
        placeholder = rev.read()



        txt_1 = st.text_area(
        "Add Revisions for One Liner with Chief Complaint",
        complaint,height=400
        )

        st.header('History of Present Illness (HPI)')
        st.success(hist)

        txt_2 = st.text_area(
        "Add Revisions for HPI",
        hist,height=400
        )

        st.header('Key Elements')
        st.success(emergency)

        txt_3 = st.text_area(
        "Add Revisions for ED",
        emergency,height=400
        )
        

        st.header('Clinical Assessment')
        st.success(assessment)

        txt_4 = st.text_area(
        "Add Revisions for assessment",
        assessment,height=400
        )


        st.header('Clinical Plan')
        st.success(plan)

        txt_5 = st.text_area(
        "Add Revisions for plan",
        plan,height=400
        )


        if st.button("Add Example", type="primary"):

            sql = "INSERT INTO examples (trans, complaint, hist, emergency, assessment, plan, user, role, casename) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)"
            values = (transcription_1, txt_1, txt_2, txt_3, txt_4, txt_5, user_email, user_role, txt_0)
             
            # Execute the query
            cursor.execute(sql, values)
             
            # Commit the changes
            db.commit()
            st.success("Successfully Added Example")

            #content_with_padding_01 = revise(transcription_1, txt_1)
            #rev = open("revisions.txt", "w")
            #rev.write(txt_1)
            #rev.close()

            #st.header('Revised Note')
            #st.success(content_with_padding_01)






    with tab3:


        



        cursor.execute("SELECT * FROM examples") 

        #print(db)

        result = cursor.fetchall() 
        a = random.randint(0,10000)
          
        # loop through the rows 
        df = pd.DataFrame(result)
        for row in result:


            with st.expander(" CaseID "  + str(row[0]) + ": " + str(row[9])  ):

                st.header('Transcription')
                st.success(row[1])
                st.header('One Liner with Chief Complaint:')
                st.success(row[2])


                #txt_1 = st.text_area("Edit One Liner with Chief Complaint",row[2],   height=200)
                #time.sleep(1)

                st.header('History of Present Illness (HPI)')
                st.success(row[3])


                #txt_2 = st.text_area("Edit Revisions for HPI", row[3],  height=200)
                #time.sleep(1)

                st.header('Key Elements')
                st.success(row[4])

                #txt_3 = st.text_area("Edit Revisions for Key Elements", row[4],  height=200)
                #time.sleep(1)
                

                st.header('Clinical Assessment')
                st.success(row[5])

                #txt_4 = st.text_area("Edit Revisions for Assessment", row[5],  height=200)
                time.sleep(1)


                st.header('Clinical Plan')
                st.success(row[6])
        


        #st.write(df)


        #number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
        edit_num = st.text_area("Enter ID of Example",  placeholder= "Please enter the ID of the example you want to edit", height=20)
        if st.button("Edit Example",  type="primary", key = 54):
            
            # edit_id = int(number)
            # sql = "SELECT * FROM examples WHERE id = %s"
            # value_id = [(edit_id)]
            # cursor.execute(sql, value_id)
            # result_edit = cursor.fetchall() 

            # for row in result_edit:

            edit_open = open("edit.txt", "w+")
            edit_open.write(edit_num)
            edit_open.close() 
            st.success("Edit this example in the Edit tab")


        delete_num = st.text_area("Enter ID of Example",  placeholder= "Please enter the ID of the example you want to delete", height=20)
        if st.button("Delete Example",  type="primary", key = 50):
            
            # edit_id = int(number)
            # sql = "SELECT * FROM examples WHERE id = %s"
            # value_id = [(edit_id)]
            # cursor.execute(sql, value_id)
            # result_edit = cursor.fetchall() 

            # for row in result_edit:

            # delete_open = open("delete.txt", "w+")
            # delete_open.write(delete_num)
            # delete_open.close() 
            


            # # edit_txt = open("edit.txt", "r")
            # # edit_id = edit_txt.read()


            # delete_txt = open("delete.txt", "r")
            # delete_id = delete_txt.read()



            delete_id = int(delete_num)
            sql = "DELETE FROM examples WHERE id = %s"
            value_id = [(delete_id)]
            cursor.execute(sql, value_id)
            #   sresult_edit = cursor.fetchall()
            db.commit()

            st.success("Successfully Deleted Example")
        




    with tab4:



        # edit_txt = open("edit.txt", "r")
        # edit_id = edit_txt.read()

        # sql_complaint = "SELECT complaint FROM examples WHERE id = %s"
        # value_id = [(edit_id)]
        # cursor.execute(sql_complaint, value_id)
        # result_complaint = cursor.fetchall()

        # sql_trans = "SELECT trans FROM examples WHERE id = %s"
        # #value_id = [(edit_id)]
        # cursor.execute(sql_trans, value_id)
        # result_trans = cursor.fetchall()

        # st.success(result_complaint[0])
        # st.success(result_trans[0])

        # txt_1 = st.text_area("Edit One Liner with Chief Complaint",  height=200)



        edit_txt = open("edit.txt", "r")
        edit_id = edit_txt.read()

        sql = "SELECT * FROM examples WHERE id = %s"
        value_id = [(edit_id)]
        cursor.execute(sql, value_id)
        result_edit = cursor.fetchall()

        for row in result_edit:

            st.header('Casename')
            st.success(row[9])

            txt_0 = st.text_area(
            "Edit casename for this note",
            height=100
            )
            st.header('Transcription')
            st.success(row[1])
            st.header('One Liner with Chief Complaint:')
            st.success(row[2])


            txt_1 = st.text_area("Edit One Liner with Chief Complaint",row[2],   height=200)
            time.sleep(1)

            st.header('History of Present Illness (HPI)')
            st.success(row[3])


            txt_2 = st.text_area("Edit Revisions for HPI", row[3],  height=200)
            time.sleep(1)

            st.header('Key Elements')
            st.success(row[4])

            txt_3 = st.text_area("Edit Revisions for Key Elements", row[4],  height=200)
            time.sleep(1)
            

            st.header('Clinical Assessment')
            st.success(row[5])

            txt_4 = st.text_area("Edit Revisions for Assessment", row[5],  height=200)
            time.sleep(1)


            st.header('Clinical Plan')
            st.success(row[6])

            txt_5 = st.text_area("Edit Revisions for Plan", row[6], height=200)
            time.sleep(1)

            if st.button("Revise Example", type="primary"):

                time.sleep(1)

                sql = "UPDATE examples SET trans = %s, complaint = %s, hist = %s, emergency = %s, assessment = %s, plan = %s, casename = %s WHERE id = %s"
                val = (row[1], txt_1, txt_2, txt_3, txt_4, txt_5, txt_0, row[0])

                cursor.execute(sql, val)

                db.commit()
                st.success("Successfully Edited Example")  






    


else:
    authenticate.button_login()























