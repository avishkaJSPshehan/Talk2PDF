import streamlit as st
import pickle 
import os
from dotenv import load_dotenv
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS


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
    load_dotenv()
    
    #file uppload Box
    pdf = 'TestSample.pdf'
    pdf = st.file_uploader("", type='pdf')

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

    #get pdf file name
    store_name = pdf.name[:-4]

    #add exsisting embediings
    if os.path.exists(f"{store_name}.pkl"):
        with open(f"{store_name}.pkl", "rb") as f:
            VectorStore = pickle.load(f)
        st.write("Embeddings Loaded From the Disk")
    else:
        embeddings = OpenAIEmbeddings()
        VectorStore = FAISS.from_texts(chunks,embedding=embeddings)
        with open(f"{store_name}.pkl","wb") as f:
            pickle.dump(VectorStore,f)
        st.write("Embeddings Computation Completed")

    query = st.text_input("Ask questions about your PDF:")
    st.write(query)
    




if __name__ == '__main__':
    main()