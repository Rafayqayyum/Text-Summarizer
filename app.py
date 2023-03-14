import streamlit as st
from utils import read_pdf,read_docx,save_docx,generate_summary
st.set_page_config(page_title="Text Summarizer",page_icon='assets/logo.png',layout='wide')


# create a function to take and process input
def take_input(file,text):
    # process input
    if file is not None:
        if file.name.endswith('.docx'):
            success,text=read_docx(file)
        if not success:
            st.error("Error reading file")
            return False,0
        elif file.name.endswith('.pdf'):
            success,text=read_pdf(file)
        if not success:
            st.error("Error reading file")
            return False,0
    if text=='':
        st.error("Please enter some text")
        return False,0
    return True,text


with st.sidebar:
    st.image('assets/logo.png',width=200,use_column_width=False)
    st.title("About Me:")
    st.subheader("Hi, I am Rafay :wave:")
    st.write("I am a software engineer and a ML enthusiast. I am passionate about building products and solving problems.")
    st.write("Find me on [Github](https://github.com/rafayqayyum) and [LinkedIn](https://www.linkedin.com/in/rafayqayyum/)")
    st.write("This is a simple text summarizer app built using [OpenAI](https://openai.com/) and [Streamlit](https://streamlit.io/).")
    st.write("You can find the source code [here]()")

with st.container():
    # add status text
    st.title("Text Summarizer")
    st.subheader("You can either upload a docx or pdf file or paste the text in the text area below.")
    # take input
    file = st.file_uploader("Upload a docx or pdf file",type=['docx','pdf'])
    text = st.text_area("Paste the text here",height=400,key='inputText')
    # create show summary text area
    summary = st.empty()
    # create a button to generate summary
    if st.button("Generate Summary"):
        progress_bar = st.progress(10)
        status,summary,tokens_discarded=generate_summary(text)
        progress_bar.progress(50)
        if not status:
            st.error("Error generating summary")
        success = save_docx(summary, 'summary.docx')
        if not success:
            st.error("Error Creating Docx file")
        else:
            progress_bar.progress(100)
            st.success(f"Summary generated successfully. {tokens_discarded} tokens discarded.")
            # show summary
            st.text_area("Summary",summary,height=200,disabled=True)
            file=open('summary.docx','rb')
            # download summary
            if st.download_button(label="Download Summary", data=file, file_name='summary.docx', mime='docx'):
                st.write('Thanks for downloading!')
            file.close()



