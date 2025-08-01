# import trafilatura
# # from playwright.sync_api import sync_playwright
# from playwright.async_api import async_playwright

# from urllib.parse import quote_plus
# import logging

# # uvicorn app:app --reload --host 0.0.0.0 --port 8000   

# async def get_search_results(query, max_results=5):
#     logging.info(f"Starting DuckDuckGo search for: {query}")
#     links = []
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)  # Headless=False for debugging visually
#         page = await browser.new_page()
#         encoded_query = quote_plus(query)
#         await page.goto(f"https://duckduckgo.com/?q={encoded_query}", wait_until="domcontentloaded")

#         await page.wait_for_selector('a[data-testid="result-title-a"]', timeout=30000)
#         link_elements = await page.query_selector_all('a[data-testid="result-title-a"]')

#         for elem in link_elements:
#             href = await elem.get_attribute('href')
#             if href and href.startswith(('http://', 'https://')):
#                 links.append(href)
#                 if len(links) == max_results:
#                     break

#         await browser.close()
#     logging.info(f"Collected {len(links)} URLs.")
#     return links




# def extract_text_from_url(url):
#     """
#     Extract text content from a given URL using trafilatura.
#     """
#     try:
#         logging.debug(f"Fetching and extracting text from URL: {url}")
#         downloaded = trafilatura.fetch_url(url)
#         if not downloaded:
#             logging.warning(f"No content downloaded from {url}")
#             return ""

#         text = trafilatura.extract(downloaded)
#         if not text:
#             logging.warning(f"No extractable text from {url}")
#             return ""

#         logging.debug(f"Extracted {len(text)} characters of text from {url}")
#         return text

#     except Exception as e:
#         logging.error(f"Extraction failed for {url}: {e}", exc_info=True)
#         return ""


import logging
import trafilatura
from playwright.async_api import async_playwright
from urllib.parse import quote_plus

logger = logging.getLogger("searcher")

async def get_search_results(query, max_results=5):
    logger.info(f"Starting DuckDuckGo search for query: {query}")
    links = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        encoded_query = quote_plus(query)
        await page.goto(f"https://duckduckgo.com/?q={encoded_query}", wait_until="domcontentloaded")

        await page.wait_for_selector('a[data-testid="result-title-a"]', timeout=30000)
        link_elements = await page.query_selector_all('a[data-testid="result-title-a"]')

        for elem in link_elements:
            href = await elem.get_attribute('href')
            if href and href.startswith(('http://', 'https://')):
                logger.debug(f"Found URL: {href}")
                links.append(href)
                if len(links) == max_results:
                    break

        await browser.close()
    logger.info(f"Collected {len(links)} URLs.")
    return links

def extract_text_from_url(url):
    logger.debug(f"Fetching and extracting text from URL: {url}")
    try:
        downloaded = trafilatura.fetch_url(url)
        if not downloaded:
            logger.warning(f"No content downloaded from {url}")
            return ""
        text = trafilatura.extract(downloaded)
        if not text:
            logger.warning(f"No extractable text from {url}")
            return ""
        logger.debug(f"Extracted {len(text)} characters of text from {url}")
        return text
    except Exception as e:
        logger.error(f"Extraction failed for {url}: {e}", exc_info=True)
        return ""
