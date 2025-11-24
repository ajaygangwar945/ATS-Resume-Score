from dotenv import load_dotenv
load_dotenv()
import io
import os
import streamlit as st
from PIL import Image
import pdf2image
import google.generativeai as genai
import base64
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input,pdf_content,prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:      
        image = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = image[0]
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')    
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type":"image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode('utf-8')
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("File not found. Please upload a PDF file.")
        


st.set_page_config(page_title="ATS Resume Score", page_icon=":guardsman:", layout="wide")
st.header("ATS Resume Score")
input_text = st.text_area("Enter your job description here:", key="input")
uploaded_file = st.file_uploader("Upload your resume here:", type=["pdf"])
if uploaded_file is not None:
    st.write("PDF file uploaded successfully!")

Submit1 = st.button("Tell me about my resume")
Submit2 = st.button("How can i improve my skills?")
Submit3 = st.button("What are the keywords missing in my resume?")
submit4 = st.button("Percentage match with job description")

input_prompt1 = """
    You are an experienced HR with a lot of experience in hiring candidates in the field of Data Science, Full stack
    web development, Big Data and machine learning.
    your task is to analyze the resume and job description and give a detailed analysis of the resume.
    please share your professional evaluation on whether the candidate's profile aligns with the job description.
    Highlight the strengths and weaknesses of the applicant in relation to the job description.
"""

input_prompt2 ="""
    You are an technical HR with a lot of experience in hiring candidates in the field of Data Science, Full stack and other domains of CSE,
    your role is to scrutinize the resume in light of the job description and provide a comprehensive analysis of the resume.
    Share your insights on the candidate's suitability for the role from an HR perspective.
    Additionally, offer advice on how the candidate can enhance their skills to better align with the job description.
"""
input_prompt3 = """
    You are an skilled ATS (application tracking system) with deep knowledge of hiring candidates in the field of Data Science, Full stack and other domains of CSE and ATS functionality." \
    your task is to analyze the resume and job description and give a detailed analysis of the resume." \
    GIve me the percentage match of the resume with the job description and also provide the keywords missing in the resume." \" \
    First the output should be the percentage match and then the keywords missing in the resume."""
if Submit1:
    if input_text and uploaded_file:
        pdf_parts = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text,pdf_parts,input_prompt1)
        st.write(response)
    else:
        st.warning("Please enter a job description and upload a resume.")
if submit4:
    if input_text and uploaded_file:
        pdf_parts = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text,pdf_parts,input_prompt2)
        st.write(response)
    else:
        st.warning("Please enter a job description and upload a resume.")