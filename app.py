import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

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
    st.write('Made with ❤️ by Avishka Shehan')

