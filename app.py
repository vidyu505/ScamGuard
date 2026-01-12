import os
import streamlit as st
#from pipeline.chain import get_chain

from pydantic import ValidationError
from pipeline.wrapper import classify_message, classify_message_batch
import pandas as pd

#print(classify_message("You won 5000 in lottery. click to claim"))

#print(get_chain())
# from llm.models import get_llm
# from llm.parser import get_parser
# from llm.prompt_template import get_prompt

# parser, format_ins = get_parser()

# print(get_llm())
# print(format_ins)
# print(get_prompt())




#from config import gemini_api_key, DEFAULT_MODEL

#print(gemini_api_key)
#print(DEFAULT_MODEL)


## Streamlit app
st.set_page_config(page_title="Spam Detactor",page_icon="0")
st.title("Spam Detector (Gemini + Langchain)")

tab1, tab2 = st.tabs(["Single Message", "Batch CSV upload"])

with tab1 :
    st.subheader("paste an email or message and detect if its a ** Spam / Not Spam / Uncertain**.")

    user_input = st.text_area("Message to classify :", height=150)
    
    if st.button("Classify:") :
        if not user_input.strip():
            st.warning("Please enter a message.")
        else :
            try:
                result = classify_message(user_input)
                st.subheader("Classification Result")
                st.write("**Label:**", result.label)
                st.write("**Risk Score:**", result.risk_score)
                st.write("**Reason:**", result.reasons)
                st.write("**Red Flags:**", result.red_flags)
                st.write("**SuggestedAction:**",result.suggested_action)
    
                with st.expander("Raw JSON"):
                    st.json(result.model_dump())
    
            except ValidationError as e :
                    st.error(f"Validation Failed: {e}")

with tab2:
    st.subheader("Upload CSV file")
    uploaded = st.file_uploader("Upload from directory",type = "csv")
    if(uploaded):
        df = pd.read_csv(uploaded)
        if(st.button("Run Batch Classification", key='batch')):
              results_df = classify_message_batch(df.iloc[:,0].tolist())
              st.dataframe(results_df,use_container_width = True)
