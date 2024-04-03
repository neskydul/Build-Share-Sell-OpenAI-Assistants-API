import openai
import streamlit as st
import time
import os
import zipfile
import yaml
 
from inference_assistant import inference
from utils import create_assistant_from_config_file, upload_to_openai, export_assistant

st.set_page_config(
    page_title="Build, Share and Sell OpenAI Assistants API",
    page_icon="🤖",
    layout="wide",
    menu_items={
        'Get Help': 'mailto:servizi@intelligenzaartificialeitalia.net',
        'Report a bug': "https://github.com/IntelligenzaArtificiale/Build-Share-Sell-OpenAI-Assistants-API/issues",
        'About': "# This is a simple web app to build, share and sell OpenAI Assistants API\n\n"
    }
)

st.title("Build🚧, Share🤗 and Sell💸 OpenAI Assistants🤖")


openaiKey = "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"
if openaiKey:
    os.environ["OPENAI_API_KEY"] = openaiKey
    openai.api_key = openaiKey
    client = openai.OpenAI()
        # Inferenza con Assistente

id_assistente = "asst_5zyTh15pzTB7CCC5BOT4PVcS"
if id_assistente:
            try: 
                inference(id_assistente)
            except Exception as e:
                st.error("🛑 There was a problem with OpenAI Servers")
                st.error(e)
                if st.button("🔄 Restart"):
                    st.rerun()

html_chat = '<center><h6>🤗 Support the project with a donation for the development of new features 🤗</h6>'
html_chat += '<br><a href="https://rebrand.ly/SupportAUTOGPTfree"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" alt="PayPal donate button" /></a><center><br>'
st.markdown(html_chat, unsafe_allow_html=True)
st.write('Made with ❤️ by [Alessandro CIciarelli](https://intelligenzaartificialeitalia.net)')
