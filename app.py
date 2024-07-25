import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

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
    st.write("Talk to PDF")
    st.write("Ask any question in your PDF")


if __name__ == '__main__':
    main()