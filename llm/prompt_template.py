import os
from langchain_core.prompts import ChatPromptTemplate


def get_prompt() :
    return ChatPromptTemplate.from_messages([
        ("system", "You are ScamGuard, an expert spam detector. Return ONLY a JSON object. \n {format_instructions}"),
        ("system","{format_instructions}"),
        ("human","Classify this message: \n\"{user_query}\"")
    ])
    