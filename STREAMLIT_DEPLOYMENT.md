# 🚀 Streamlit Deployment Guide

## Step-by-Step Deployment to Streamlit Cloud

### Prerequisites
1. GitHub account with your repository pushed
2. Streamlit Cloud account (free at https://streamlit.io/cloud)
3. Google Gemini API Key

### Deployment Steps

#### 1. Push Your Code to GitHub
```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

**⚠️ IMPORTANT**: Make sure `.env` file is NOT committed to GitHub!
- Check `.gitignore` includes `.env`
- Verify with: `git status` (should NOT show .env)

#### 2. Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**: https://share.streamlit.io/
2. **Sign in** with your GitHub account
3. **Click "New app"**
4. **Select your repository** from the dropdown
5. **Choose branch**: `main` (or your default branch)
6. **Main file path**: `app.py`

#### 3. Add Your API Key as Secret

**Before clicking "Deploy":**

1. Click **"Advanced settings"** or **"Secrets"** tab
2. Add your secrets in this format:
   ```toml
   GOOGLE_API_KEY = "your_actual_api_key_here"
   ```
3. Click **"Save"**
4. Click **"Deploy"**

#### 4. Alternative: Using Streamlit Secrets File

You can also create `.streamlit/secrets.toml` locally (but DON'T commit it):

```toml
GOOGLE_API_KEY = "your_actual_api_key_here"
```

Then add `.streamlit/secrets.toml` to `.gitignore`

### ✅ Verification

After deployment:
1. Your app will be available at: `https://your-app-name.streamlit.app`
2. Test all buttons to ensure API key works
3. Check logs if there are any errors

### 🔒 Security Best Practices

- ✅ **DO**: Use Streamlit secrets for API keys
- ✅ **DO**: Keep `.env` in `.gitignore`
- ❌ **DON'T**: Commit API keys to GitHub
- ❌ **DON'T**: Share your API key publicly
- ❌ **DON'T**: Hardcode API keys in your code

### Troubleshooting

**Error: "API Key not found"**
- Check Streamlit secrets are set correctly
- Verify the key name is `GOOGLE_API_KEY`
- Check app logs in Streamlit dashboard

**Error: "Invalid API Key"**
- Verify your Gemini API key is valid
- Check if API key has proper permissions
- Regenerate key if needed

**App not updating**
- Clear browser cache
- Check if latest code is pushed to GitHub
- Restart app in Streamlit dashboard
