from dotenv import load_dotenv
load_dotenv()
import io
import os
import streamlit as st
from PIL import Image
import pdf2image
import google.generativeai as genai
import base64

# Get API key from environment variable or Streamlit secrets (for deployment)
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    try:
        api_key = st.secrets.get("GOOGLE_API_KEY")
    except (AttributeError, FileNotFoundError, KeyError):
        pass
if not api_key:
    st.error("⚠️ API Key not found! Please set GOOGLE_API_KEY in your .env file or Streamlit secrets.")
    st.stop()
genai.configure(api_key=api_key)


def get_gemini_response(input,pdf_content,prompt):
    # Try models in order of preference (all support vision/image inputs)
    models_to_try = [
        "gemini-1.5-pro",      # Best quality, supports vision
        "gemini-1.5-flash",     # Faster, cheaper, supports vision
        "gemini-pro-vision",    # Older but stable vision model
        "gemini-pro"            # Fallback (may not support images)
    ]
    
    last_error = None
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content([input,pdf_content[0],prompt])
            return response.text
        except Exception as e:
            last_error = e
            # Try next model
            continue
    
    # If all models failed, show error
    error_msg = str(last_error) if last_error else "Unknown error"
    if "NotFound" in error_msg or "404" in error_msg:
        st.error("""
        ⚠️ **Model Not Found Error**: No Gemini model is available.
        
        **Possible causes:**
        1. Your API key doesn't have access to Gemini models
        2. Your API key might be invalid or expired
        3. Gemini API might be temporarily unavailable
        
        **Solutions:**
        - Verify your API key at: https://makersuite.google.com/app/apikey
        - Make sure your API key has Gemini API access enabled
        - Check Streamlit secrets if deployed
        - Try regenerating your API key
        """)
    else:
        st.error(f"⚠️ **API Error**: {error_msg}\n\nPlease check your API key and try again.")
    st.stop()
    return ""

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            image = pdf2image.convert_from_bytes(uploaded_file.read())
            if not image or len(image) == 0:
                raise ValueError("Failed to convert PDF to image. The PDF might be corrupted.")
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
        except pdf2image.exceptions.PDFInfoNotInstalledError:
            st.error("""
            ⚠️ **PDF Processing Error**: Poppler is not installed.
            
            **For Streamlit Cloud**: Make sure `packages.txt` with `poppler-utils` is in your repository.
            **For Local Development**: Install poppler:
            - Windows: Download from https://github.com/oschwartz10612/poppler-windows/releases
            - macOS: `brew install poppler`
            - Linux: `sudo apt-get install poppler-utils`
            """)
            st.stop()
        except Exception as e:
            st.error(f"Error processing PDF: {str(e)}")
            st.stop()
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
        with st.spinner("Analyzing your resume..."):
            pdf_parts = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_text, pdf_parts, input_prompt1)
            st.write(response)
    else:
        st.warning("Please enter a job description and upload a resume.")

if Submit2:
    if input_text and uploaded_file:
        with st.spinner("Generating skill improvement suggestions..."):
            pdf_parts = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_text, pdf_parts, input_prompt2)
            st.write(response)
    else:
        st.warning("Please enter a job description and upload a resume.")

if Submit3:
    if input_text and uploaded_file:
        with st.spinner("Analyzing keywords..."):
            pdf_parts = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_text, pdf_parts, input_prompt3)
            st.write(response)
    else:
        st.warning("Please enter a job description and upload a resume.")

if submit4:
    if input_text and uploaded_file:
        with st.spinner("Calculating match percentage..."):
            pdf_parts = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_text, pdf_parts, input_prompt3)
            st.write(response)
    else:
        st.warning("Please enter a job description and upload a resume.")