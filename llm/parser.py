import os
from typing import List, Literal
from pydantic import BaseModel, Field, ValidationError
from langchain_core.output_parsers import PydanticOutputParser

# --------------------------------------
# 1 Define Schema
# -------------------------------------

class SpamClassification(BaseModel):
    label: Literal["Spam", "Not Spam", "Uncertain"] = "Uncertain"
    reasons: List[str] = Field(default_factory=list)
    risk_score: int = Field(default=0, ge=0, le=100)
    red_flags: List[str] = Field(default_factory=list)
    suggested_action: str = "No action available"



def get_parser() :
    parser = PydanticOutputParser(pydantic_object=SpamClassification)
    format_instructions = parser.get_format_instructions()
    return parser, format_instructions    