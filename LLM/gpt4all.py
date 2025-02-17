from fastapi import APIRouter, HTTPException, Query
from gpt4all import GPT4All

from LLM.functions import generate_filename

router = APIRouter(prefix="/LLM")

model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf", device='cpu') 


@router.get("/process-data")
async def process_with_llm(
    data: str, 
    prompt: str,
    ):
    """
    API Endpoint to process the Result of scrapped HTML
    - `data: The scrapped HTML of Text`
    - `prompt: The users instruction for processing the "data".`
    
    """
    
    full_prompt = f"""
        You are an AI assistant. Process the following data as per the given instructions.

        Instructions: {prompt}
        Data: {data}
        
        Ensure the output is structured properly.
        """
    try:
         with model.chat_session():
            response = model.generate(full_prompt, max_tokens=2048)
            
            return {"Message": "Successfully Processed", "Processed Data": response}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Error while Processing.")