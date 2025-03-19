import streamlit as st
import pickle
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

#sidebar contents
with st.sidebar:
    st.title('💬😃 Talk2PDF...')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com)
    - [OprnAI](https://platform.openai.com/docs/models) LLM Model
                
    ''')
    add_vertical_space(3)
    st.write('Made with ❤️ by [Avishka Shehan](https://portfolio-avishka-shehan.vercel.app/)')


def main():
    st.write("Chat with PDF 💭")

    #load env variables for the project
    load_dotenv()

    # upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type='pdf')

    #read the pdf content
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        #use text splitter to split the whole text
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

        chunks = text_splitter.split_text(text=text)

        #embeddings
        embeddings = OpenAIEmbeddings()

        VectorStore = FAISS.from_texts(chunks,embedding=embeddings)
        store_name = pdf.name[:-4]
        with open(f"{store_name}.pkl","wb") as f:
            pickle.dump(VectorStore,f)



if __name__ == '__main__':
    main()