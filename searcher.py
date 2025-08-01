import trafilatura
from playwright.sync_api import sync_playwright
from urllib.parse import quote_plus
import logging

def get_search_results(query, max_results=5):
    logging.info(f"Starting DuckDuckGo search for: {query}")
    links = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Disable headless to debug visually
        page = browser.new_page()
        encoded_query = quote_plus(query)
        page.goto(f"https://duckduckgo.com/?q={encoded_query}", wait_until="domcontentloaded")

        page.wait_for_selector('a[data-testid="result-title-a"]', timeout=30000)
        link_elements = page.query_selector_all('a[data-testid="result-title-a"]')

        for elem in link_elements:
            href = elem.get_attribute('href')
            if href and href.startswith(('http://', 'https://')):
                links.append(href)
                if len(links) == max_results:
                    break

        browser.close()
    logging.info(f"Collected {len(links)} URLs.")
    return links



def extract_text_from_url(url):
    """
    Extract text content from a given URL using trafilatura.
    """
    try:
        logging.debug(f"Fetching and extracting text from URL: {url}")
        downloaded = trafilatura.fetch_url(url)
        if not downloaded:
            logging.warning(f"No content downloaded from {url}")
            return ""

        text = trafilatura.extract(downloaded)
        if not text:
            logging.warning(f"No extractable text from {url}")
            return ""

        logging.debug(f"Extracted {len(text)} characters of text from {url}")
        return text

    except Exception as e:
        logging.error(f"Extraction failed for {url}: {e}", exc_info=True)
        return ""
