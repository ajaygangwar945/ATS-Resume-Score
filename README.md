# 📄 ATS Resume Score

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Gemini AI](https://img.shields.io/badge/Google-Gemini%20AI-4285F4)

**ATS Resume Score** is a powerful Streamlit-based web application that leverages Google's **Gemini AI** to analyze resumes against job descriptions. It acts as an intelligent Applicant Tracking System (ATS) scorer, providing actionable insights to help candidates improve their profiles.

---

## 🚀 Live Demo

Try the live version of the app: [**ATS Resume Score**](https://ats-resume-score-945.streamlit.app/)

---

## 🖼️ App Preview

<p align="center">
  <img src="assests/app_preview.png" width="850"/>
</p>

---

## ✨ Features

- **📊 Resume Analysis**: Upload a PDF resume and get a detailed evaluation of alignment with the job description.
- **💡 Skill Improvement**: Receive personalized advice on how to enhance your skills.
- **🔑 Keyword Analysis**: Identify missing keywords and get a percentage match score.
- **📈 Percentage Match**: Understand how well your resume fits the job requirements.
- **🧮 ATS Score Output**: Generates a numerical ATS match score (0–100) with clear interpretation.

---

## 🛠️ How It Works

1. **Input**: Enter the job description and upload your resume (PDF).
2. **Processing**: The app converts the PDF to an image and prepares it for analysis.
3. **AI Analysis**: Google's **Gemini 2.5 Flash** model analyzes the content.
4. **Results**: View detailed feedback, strengths, weaknesses, and missing keywords.

---

## 🧪 Example Use Case

**Job Role**: Data Analyst  
**Resume Match Score**: 72%  

**Missing Keywords**:

- SQL Optimization
- Power BI DAX
- Statistical Modeling

**AI Suggestions**:

- Add measurable achievements using metrics
- Include project-based experience aligned with job description

---

## 📋 Requirements

- Python 3.7+
- Google API Key (for Gemini AI)
- Virtual environment (recommended)

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ATS-Resume-Score
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

- **Windows**: `venv\Scripts\activate`
- **macOS/Linux**: `source venv/bin/activate`

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

- Copy `.env.example` to `.env`:

    ```bash
    cp .env.example .env
    ```

- Edit `.env` and add your Google API Key:

    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

- **⚠️ IMPORTANT**: Never commit `.env` to Git! It's already in `.gitignore`.

### 6. Get Your Google Gemini API Key

1. Go to: [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and paste it in your `.env` file

---

## ▶️ Running the Application

1. Ensure your virtual environment is activated.
2. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

3. Open your browser and navigate to `http://localhost:8501`.

---

## 🚀 Deployment to Streamlit Cloud

### Prerequisites

- GitHub account with your repository pushed
- Streamlit Cloud account (free at <https://streamlit.io/cloud>)
- Google Gemini API Key

### Deployment Steps

#### Step 1: Push to GitHub

```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

**⚠️ IMPORTANT**: Verify `.env` is NOT committed to GitHub!

```bash
git status  # Should NOT show .env
```

#### Step 2: Deploy on Streamlit Cloud

1. **Go to**: [Streamlit Cloud](https://share.streamlit.io/)
2. **Sign in** with your GitHub account
3. **Click "New app"**
4. **Select your repository** from the dropdown
5. **Choose branch**: `main`
6. **Main file path**: `app.py`

#### Step 3: Add API Key as Secret

**Before clicking "Deploy":**

1. Click **"Advanced settings"** or **"Secrets"** tab
2. Add your secret in TOML format:

   ```toml
   GOOGLE_API_KEY = "your_actual_api_key_here"
   ```

3. Click **"Save"**
4. Click **"Deploy"**

**📦 Note**: The `packages.txt` file is included in the repository. It installs `poppler-utils` required for PDF processing. Streamlit Cloud will automatically install it.

#### Step 4: Verify Deployment

After deployment:

1. Your app will be available at: `https://your-app-name.streamlit.app`
2. Test all buttons to ensure API key works
3. Check logs if there are any errors

---

## 🔒 Security Best Practices

### API Key Management

- ✅ **DO**: Use `.env` file for local development
- ✅ **DO**: Use Streamlit secrets for production deployment
- ✅ **DO**: Keep `.env` in `.gitignore`
- ❌ **DON'T**: Commit API keys to GitHub
- ❌ **DON'T**: Share your API key publicly
- ❌ **DON'T**: Hardcode API keys in your code

### Before Pushing to GitHub

- [ ] Verify `.env` is in `.gitignore`
- [ ] Run `git status` to ensure `.env` is NOT tracked
- [ ] Ensure no API keys are in code files
- [ ] `.env.example` exists (without real keys)

### API Key Security Features

- **No Hardcoded Secrets**: API keys are managed via environment variables (`.env`) or Streamlit secrets
- **Local Processing**: Files are processed in memory and sent directly to the Gemini API
- **Git Ignore**: `.env` file is excluded from version control
- **Secure Deployment**: Streamlit secrets are encrypted

### Recommended Security Measures

1. **API Key Restrictions** (Google Cloud Console):
   - Restrict to specific APIs (Gemini API only)
   - Restrict to specific domains (your Streamlit app URL)
   - Set usage quotas

2. **Key Rotation**: Rotate API keys periodically

3. **Monitoring**: Monitor API usage at [Google Cloud Console](https://console.cloud.google.com)

### If Your Key is Compromised

1. **Immediately revoke** the exposed key at [Google AI Studio](https://makersuite.google.com/app/apikey)
2. **Generate new key** from Google Cloud Console
3. **Update** all environments (local `.env`, Streamlit secrets)
4. **Review** API usage logs for unauthorized access

---

## 🔧 Troubleshooting

### Error: "API Key not found"

- Check `.env` file has `GOOGLE_API_KEY` set
- For Streamlit Cloud: Verify secrets are set correctly
- Check the key name is exactly `GOOGLE_API_KEY`

### Error: "Invalid API Key"

- Verify your Gemini API key is valid
- Check if API key has proper permissions
- Regenerate key if needed at [Google AI Studio](https://makersuite.google.com/app/apikey)

### Error: "PDFInfoNotInstalledError" or "poppler not installed"

**For Streamlit Cloud**:

- ✅ The `packages.txt` file is included in the repository
- Streamlit Cloud automatically installs poppler

**For Local Development**:

- **Windows**: Download from [poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases)
- **macOS**: `brew install poppler`
- **Linux**: `sudo apt-get install poppler-utils`

### Error: "Model Not Found"

- Your API key doesn't have access to Gemini models
- Verify your API key at [Google AI Studio](https://makersuite.google.com/app/apikey)
- Make sure Gemini API access is enabled
- Try regenerating your API key

### App not updating on Streamlit Cloud

- Clear browser cache
- Check if latest code is pushed to GitHub
- Restart app in Streamlit dashboard

---

## 📦 Dependencies

- `streamlit`: Web interface
- `google-generativeai`: AI analysis
- `python-dotenv`: Environment management
- `pdf2image`: PDF processing
- `Pillow`: Image manipulation

---

## 📝 Notes

- The application currently processes the **first page** of the uploaded PDF.
- Ensure your Google API Key has access to the **Gemini API**.
- API calls are made directly to Google's Gemini API - no data is stored.

---

## 📄 License

This project is licensed under the MIT License.
