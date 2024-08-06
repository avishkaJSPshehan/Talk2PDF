import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter


with st.sidebar:
    st.title('🤗💬 LLM Chat App')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
 
    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ by [Developer](https://portfolio-avishka-shehan-5dwot0xnv-avishka-shehans-projects.vercel.app/)')

def main():
    st.write("Talk to PDF 💭")
    
    
    #file uppload Box
    pdf = st.file_uploader("Upload your PDF", type='pdf')

    text = ""
    if pdf is not None:
        pdf_reader = PdfReader(pdf)

        
        for page in pdf_reader.pages:
            text += page.extract_text()
        
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text=text)

    st.write(chunks)




if __name__ == '__main__':
    main()