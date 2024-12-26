import streamlit as st
import os 
import shutil 
import atexit

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
    side_bar_message = """ hi i am there to help u with the summarization and documentation 
    """
    with st.sidebar:
        st.title ("side_bar_message")
        st.markdown(side_bar_message)

    save_dir ='temp'
    if not  os.path.exists(save_dir):
        os.makedirs(save_dir)

    def cleanup():
        if os.path.exists(save_dir):
            shutil.rmtree(save_dir)
    atexit.register(cleanup)

    upload_file = st.file_uploader("Upload the Document",type=["txt","pdf"])



if __name__ == "__main__":
    main()