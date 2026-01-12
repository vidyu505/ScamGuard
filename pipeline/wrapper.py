import os 
import pandas as pd

from pipeline.chain import get_chain
def classify_message(message):
    chain, format_instructions = get_chain()
    result = chain.invoke({
        "format_instructions": format_instructions,
        "user_query": message
    })





def classify_message_batch(messages : list[str]) -> pd.DataFrame:
    """
    Simple batch classification using LangChain's .batch().
    Returns a DataFrame with one row per message.
    """
    chain, format_instructions = get_chain()

    inputs = [
        {"format_instructions" : format_instructions, "user_query" : msg}
        for msg in messages
    ]

    # Run batch
    outputs = chain.batch(inputs)

    # Build DataFrame
    results = []
    for i, (msg,out) in enumerate(zip(messages, outputs), start=1):
            results.append({
                "Message #": i,
                "Message": msg,
                "Label": out.label,
                "Risk Score": out.risk_score,
                "Reasons": "; ".join(out.reasons),
                "Red Flags": "; ".join(out.red_flags),
                "Suggested Action": out.suggested_action
            })
    return pd.DataFrame(results)    

