from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

# fucntion to get the raw HTML from a given site url
async def get_html(url: str):
    async with async_playwright() as p:
        
        browser = await p.chromium.launch(headless=False, slow_mo=50)
        page = await browser.new_page()
        # Set headers to mimic a real browser
        await page.set_extra_http_headers({"User-Agent": "Mozilla/5.0"})
        await page.goto(url, timeout=60000, wait_until="domcontentloaded")
        #grabbing the page elements
        content = await page.content()  
        await browser.close()
        return content

# function to extract text form HTMl removing tags
def extract_text_from_html(html: str):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "meta", "noscript", "iframe"]):
        tag.extract()
    return soup.get_text(separator=" ", strip=True)

#function to extract data of given selectors
def extract_data_from_html(html: str, selector: str):
    soup = BeautifulSoup(html, "html.parser")
    elements = soup.select(selector)
    return [element.get_text(strip=True) for element in elements]