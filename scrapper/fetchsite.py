
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from fastapi import APIRouter, HTTPException




router = APIRouter()
async def get_html(url: str):
    async with async_playwright() as p:
        
        browser = await p.chromium.launch(headless=False, slow_mo=50)
        page = await browser.new_page()
        # Set headers to mimic a real browser
        await page.set_extra_http_headers({"User-Agent": "Mozilla/5.0"})

        await page.goto(url, timeout=60000, wait_until="domcontentloaded")

        content = await page.content()  
        await browser.close()
        
        soup = BeautifulSoup(content, "html.parser")
        for tag in soup(["scripts", "style", "meta", "nonscript", "iframe"]):
            tag.extract()
        clean_hml = soup.get_text(separator="", strip=True)
        return clean_hml  


@router.get("/get-html-of-Site")
async def playwright_scrape(url: str):
    """API endpoint to scrape Sites Code"""
    html_cleaned = await get_html(url)  
    if not html_cleaned:
        raise HTTPException(status_code=404, detail={"details": "Error fetching HTML"}) 
    print(html_cleaned)
    return {"Message": "HTML Fetched","title": html_cleaned}

        
    

    