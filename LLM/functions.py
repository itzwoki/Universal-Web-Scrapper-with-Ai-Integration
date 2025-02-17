from fastapi.responses import  FileResponse
from fastapi import HTTPException
import pandas as pd
from io import BytesIO
from docx import Document
import re

def generate_filename(prompt: str, output_format: str):
    """
    Generate a File name based on the prompt and and output format.
    """

    sanitized_prompt = re.sub(r'[^a-zA-Z0-9_]', '_', prompt[:50])  # Keep only alphanumeric & limit length
    return f"{sanitized_prompt}.{output_format}"


