import streamlit as st
from utils import read_pdf,read_docx,save_docx,generate_summary, max_response
import random
st.set_page_config(page_title="Text Summarizer",page_icon='assets/logo.png',layout='wide')

# convert ByteIO to file
def convert_to_file(file):
    with open(file.name, "wb") as f:
        f.write(file.getbuffer())
    return file.name

# function to create a random file name
def get_random_filename():
    return "".join([chr(random.randint(97,122)) for i in range(7)])+".docx"

# create a function to take and process input
def take_input(file,text):
    # process input
    if file is not None and text!="" and not text.isspace() and text!=None:
        st.error("Please upload a file or paste the text, not both.")
        return False,0
    elif file is not None:
        if file.name.endswith('.docx'):
            success,text=read_docx(convert_to_file(file))
            if not success:
                st.error("Error reading file")
                return False,0
        elif file.name.endswith('.pdf'):
            success,text=read_pdf(convert_to_file(file))
            if not success:
                st.error("Error reading file")
                return False,0
        if len(text.split()) < 10:
            st.error("The Format of the file is not supported or file is empty")
            return False, 0
        return True,text
    elif text!="" and text!=" " and text!=None:
        return True,text
    else:
        st.error("Please upload a file or paste the text.")
        return False,0



with st.sidebar:
    st.image('assets/logo.png',width=270,use_column_width=False)
    st.title("About Me:")
    st.subheader("Hi, I am Rafay :wave:")
    st.write("I am a software engineer and a ML enthusiast. I am passionate about building products and solving problems.")
    st.write("Find me on [Github](https://github.com/rafayqayyum) and [LinkedIn](https://www.linkedin.com/in/rafayqayyum/)")
    st.write("This is a simple text summarizer app built using [OpenAI](https://openai.com/) and [Streamlit](https://streamlit.io/).")
    st.write("You can find the source code [here](https://github.com/Rafayqayyum/Text-Summarizer)")

with st.container():
    # add status text
    st.title("Text Summarizer")
    st.subheader("You can either upload a Docx, Pdf file or paste the text in the text area below.")
    st.write("Only the first 2500 words will be summarized.")
    # take open ai api key
    api_key = st.text_input("Enter your OpenAI API Key",type='password')
    # take input
    file = st.file_uploader("Upload a docx or pdf file",type=['docx','pdf'],accept_multiple_files=False)
    text = st.text_area("Paste the text here",height=320,key='inputText')
    # take input
    status,read_input=take_input(file,text)
    random_filename = get_random_filename()
    if status and api_key!="" and api_key!=None:
        # create show summary text area
        summary = st.empty()
        # create a button to generate summary
        if st.button("Generate Summary"):
            progress_bar = st.progress(10)
            status,summary,tokens_discarded=generate_summary(read_input,api_key)
            progress_bar.progress(50)
            if status:
                success = save_docx(summary, random_filename)
                if success:
                    progress_bar.progress(100)
                    st.success(f"Summary generated successfully. {tokens_discarded} tokens discarded.")
                    # show summary
                    st.text_area("Summary",summary,height=200,disabled=True)
                    file=open(random_filename,'rb')
                    # download summary
                    if st.download_button(label="Download Summary", data=file, file_name=random_filename, mime='docx'):
                        st.write('Thanks for downloading!')
                    file.close()
                else:
                    st.error("Error Creating Docx file")
            else:
                progress_bar.progress(100)
                st.error("Error generating summary")
