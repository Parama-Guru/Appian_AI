import streamlit as st
import os 
import shutil 
import atexit
from utils import delete_previous_file
from services import model 


def main():
    st.markdown (
    """ 
        <style>
        .appview-container .main .block-container{{
            padding-top :{padding_top} rem 
            padding-bottom :{padding_bottom}rem 
            }}
        </style>""".format(padding_top=1,padding_bottom=1),unsafe_allow_html=True,
)
    st.markdown("""
    <h3 style = 'text-align:left; color : black; padding-top : 35px ; border-bottom : 5px solid red;'>
                 Document Summarization And Categorisation
    </h3>""",unsafe_allow_html=True)

    side_bar_message = (" Hi I am there to help you with the summarization and documentation\n"
                        "1. Upload your document in the using the Browse button\n"
                        "2. Press the submit buttton you will get your required output\n"
                        "3. After verifying the out presss confirm \n"
                        "4. the data will be ingested to the database\n")
    with st.sidebar:
        st.title ("Steps of the process")
        st.markdown(side_bar_message)

    save_dir ='temp'
    if not  os.path.exists(save_dir):
        os.makedirs(save_dir)

    def cleanup():
        if os.path.exists(save_dir):
            shutil.rmtree(save_dir)
    atexit.register(cleanup)

    if 'uploaded_file' not in st.session_state:
        st.session_state.uploaded_file = None
    if 'output' not in st.session_state:
        st.session_state.output = None
    if 'summarized' not in st.session_state:
        st.session_state.summarized = False
    if 'ingested' not in st.session_state:
        st.session_state.ingested = False
    
    uploaded_file = st.file_uploader("Choose a PDF...", type=["pdf"])

    if uploaded_file is not None:
        delete_previous_file(save_dir)  
        save_path = os.path.join(save_dir, uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.session_state.uploaded_file = save_path
        st.success(f"File saved successfully: {uploaded_file.name}")

    submit = st.button("Submit")

    if submit and st.session_state.uploaded_file:
        st.text("Summarizing and Categorizing the document...")
        st.session_state.output = model()
        st.session_state.summarized = True
        st.success("Document Summarized and Categorized Successfully")
    if st.session_state.summarized:
        st.write(st.session_state.output)
        confirm = st.button("Confirm")
        if confirm:
            st.text("Ingesting the data to the database...")
            st.session_state.ingested = True
    if st.session_state.ingested:
       st.success("Data Ingested to the database Successfully")
    
if __name__ == "__main__":
    main()