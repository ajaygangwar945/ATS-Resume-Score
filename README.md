# ATS Resume Score

This is a Streamlit-based web application that uses Google's Gemini AI to analyze resumes against job descriptions. It acts as an Applicant Tracking System (ATS) scorer, providing insights on resume suitability, skill improvement suggestions, missing keywords, and percentage match with job requirements.

## Features

- **Resume Analysis**: Upload a PDF resume and enter a job description to get a detailed evaluation of how well the candidate's profile aligns with the job.
- **Skill Improvement Advice**: Receive personalized recommendations on how to enhance skills to better match the job description.
- **Keyword Analysis**: Identify missing keywords in the resume that are present in the job description, along with a percentage match score.
- **Percentage Match**: Get an overall percentage match between the resume and job description.

## How It Works

1. **Input Processing**:
   - Users enter a job description in a text area.
   - Users upload a PDF resume file.
   - The PDF is converted to an image (first page only) using `pdf2image`.
   - The image is encoded in base64 format for processing.

2. **AI Analysis**:
   - The application uses Google's Gemini 1.5 Flash model to analyze the resume image and job description text.
   - Different prompts are used for various analysis types:
     - Detailed resume evaluation
     - Skill improvement suggestions
     - Keyword and percentage match analysis

3. **Output**:
   - Results are displayed directly in the Streamlit interface.
   - Analysis includes strengths, weaknesses, missing keywords, and match percentages.

## Requirements

- Python 3.7+
- Google API Key (for Gemini AI)
- Virtual environment (recommended)

## Installation

1. Clone or download this repository.

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up your Google API Key:
   - Create a `.env` file in the project root.
   - Add your Google API Key: `GOOGLE_API_KEY=your_api_key_here`

## Running the Application

1. Ensure the virtual environment is activated.

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Open your browser and navigate to the provided local URL (usually http://localhost:8501).

## Usage

1. Enter the job description in the text area.
2. Upload your resume as a PDF file.
3. Click on one of the analysis buttons:
   - "Tell me about my resume"
   - "How can I improve my skills?"
   - "What are the keywords missing in my resume?"
   - "Percentage match with job description"
4. View the AI-generated analysis in the app.

## Dependencies

- streamlit: For the web interface
- google-generativeai: For AI-powered analysis
- python-dotenv: For environment variable management
- pdf2image: For PDF to image conversion
- dotenv: Additional environment variable support
- PIL (Pillow): For image processing

## Notes

- The application processes only the first page of the uploaded PDF.
- Ensure your Google API Key has access to the Gemini API.
- The app requires an active internet connection for AI processing.

## Known Issues

- The "Percentage match with job description" button currently provides skill improvement advice instead of percentage match. This appears to be a code bug where the wrong prompt is used.
