# Text Summarizer using GPT-3 and Streamlit

## Introduction
This is a simple text summarizer using GPT-3 and Streamlit. It is a simple web app that takes in PDF, DOCX or text and returns a summary of the text which can be downloaded as DOCX. The app is deployed on Streamlit and can be accessed [here](https://textsummarizer.streamlit.app/).

# Installation
1. Clone the repository
```git clone https://github.com/Rafayqayyum/youtube-summarizer```
2. Install the requirements
```pip install -r requirements.txt```
3. Sign up for an OpenAI API key [here](https://platform.openai.com/signup/)
4. Add your OpenAI API key to the environment variable by exporting it in your terminal:
``` export OPENAI_API_KEY='YOUR_API_KEY'```

# Usage
1. Run the app
```streamlit run app.py```
2. Enter the URL of the YouTube video you want to summarize.
3. Click the "Summarize" button.
4. Wait for the app to process the video and generate the summary.
5. The summary will be displayed on the screen.
