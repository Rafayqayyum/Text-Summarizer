import openai
import docx
import PyPDF2
import os
max_words=2000
openai.api_key = os.getenv('OPENAI_API_KEY')
def generate_summary(prompt):
  tokens_discarded=0
  words=prompt.split()
  if len(words)>max_words:
    prompt = " ".join(words[:max_words])
    tokens_discarded=len(words)-max_words
  try:
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Summarize : {prompt}",
      temperature=0.91,
      max_tokens=400,
      top_p=1.0,
      frequency_penalty=0.2,
      presence_penalty=0.2)
  except:
    return False,0,0
  return True,response.choices[0].text.strip(),tokens_discarded

def read_docx(filename):
  try:
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return True,' '.join(fullText).strip().replace('\n','')
  except:
    return False,0

def save_docx(text,filename):
  document = docx.Document()
  document.add_heading("Summary")
  document.add_paragraph(text)
  try:
    document.save(filename)
    document
    return True
  except:
    return False

def read_pdf(filename):
  try:
    pdf = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf)
    text=''
    for i in range(0,len(pdf_reader.pages)):
      page = pdf_reader.pages[i]
      text=text+ ' '+page.extract_text().strip().replace('\n', '')
    return True,text
  except:
    return False,0
