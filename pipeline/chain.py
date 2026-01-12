import os
from llm.models import get_llm
from llm.parser import get_parser
from llm.prompt_template import get_prompt


def get_chain() :
    parser, format_instructions = get_parser()
    llm = get_llm()
    prompt = get_prompt()

# Chain
    chain = prompt | llm | parser    
    return chain, format_instructions