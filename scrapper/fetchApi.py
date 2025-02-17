from scrapper.functions import get_html, extract_data_from_html, extract_text_from_html

#FastApi Imports Imports
from fastapi import APIRouter, HTTPException,Query


router = APIRouter(prefix="/scrape")

@router.get("/get-html")
async def extract_html_from_url(url: str):
    """
    API endpoint to scrape a website and return:
    - `html` (raw HTML) (default)
    - `text` (clean text without tags)
    """
    html = await get_html(url)
    if not html:
        raise HTTPException(status_code=404, detail="Error fetching HTML")
    return {"Message": "Succesfully fetched HTML." ,"html":html}

@router.get("/get-text-from-html")
async def get_text(url: str):
    """
    API endpoint to scrape a website and return:
    - `text` (clean text from HTML without tags)
    """
    html = await get_html(url)
    if not html:
        raise HTTPException(status_code=404, detail="Error fetching HTML")
    text_from_html = extract_text_from_html(html)
    return {"Message": "Succesfully Cleaned HTML.", "text": text_from_html}

@router.get("/get-specific-selector")
async def get_data(url: str, selector: str):
    """
    API endpoint to scrape a website and return:
    - `selector` (specific elements based on a CSS selector)
    """
    html = await get_html(url)
    if not html:
        raise HTTPException(status_code=404, detail="Error fetching HTML")
    data_from_html = extract_data_from_html(html, selector)
    return {"Message": "Succesfully Fetched..", "text": data_from_html}


@router.get("/get-html-text-selectorText")
async def playwright_scrape(
    url: str,
    mode: str = Query("html", enum=["html", "text", "selector"]),
    selector: str = None
):
    """
    API endpoint to scrape a website and return either:
    - `html` (raw HTML) (default)
    - `text` (clean text without tags)
    - `selector` (specific elements based on a CSS selector)
    """
    html = await get_html(url)
    
    if not html:
        raise HTTPException(status_code=404, detail="Error fetching HTML")

    if mode == "text":
        return {"message": "Text Fetched", "Text from Html": extract_text_from_html(html)}
    
    elif mode == "selector":
        if not selector:
            raise HTTPException(status_code=400, detail="Selector is required for mode='selector'")
        return {"message": "Data Fetched", "data": extract_data_from_html(html, selector)}

    return {"message": "HTML Fetched", "html": html}

        
    

    