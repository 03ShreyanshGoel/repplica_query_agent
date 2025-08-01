import logging
from validator import is_query_valid
from memory import search_similar, add_to_memory
from searcher import get_search_results, extract_text_from_url
from summarizer import summarize

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG for detailed trace; change to INFO in production
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main():
    logging.info("Starting Ripplica Web Query Agent CLI")
    print("Welcome to the Ripplica Web Query Agent CLI!")

    while True:
        try:
            query = input("\nEnter your query (or type 'exit' to quit): ").strip()
            logging.debug(f"User input received: '{query}'")

            if query.lower() == "exit":
                logging.info("User requested exit. Exiting CLI.")
                break

            if not query:
                logging.debug("Empty input received. Prompting again.")
                continue

            if not is_query_valid(query):
                logging.info(f"Invalid query detected: '{query}'")
                print("This is not a valid query.")
                continue

            logging.info(f"Valid query received: '{query}'")

            cached_summary = search_similar(query)
            if cached_summary:
                logging.info("Cache hit: summary found for query.")
                print("\n[Cached Result]\n")
                print(cached_summary)
                continue
            else:
                logging.info("Cache miss: no existing summary found.")

            logging.info("Performing web search...")
            urls = get_search_results(query)
            logging.debug(f"Search results URLs: {urls}")

            contents = []
            for url in urls:
                logging.debug(f"Extracting text from URL: {url}")
                text = extract_text_from_url(url)
                if text:
                    contents.append(text)
                    logging.debug(f"Extracted {len(text)} characters of text")
                else:
                    logging.warning(f"No text extracted from URL: {url}")

            if not contents:
                logging.warning("No content extracted from any URLs, skipping summarization.")
                print("Sorry, no content could be retrieved from the search results.")
                continue

            logging.info("Summarizing individual page contents.")
            page_summaries = [summarize(c) for c in contents if c]
            logging.debug(f"Page summaries count: {len(page_summaries)}")

            combined_text = "\n\n".join(page_summaries)
            if not combined_text.strip():
                logging.warning("Combined summary text is empty after summarization.")
                print("Unable to generate a summary from the extracted contents.")
                continue

            logging.info("Generating combined summary of all pages.")
            combined_summary = summarize(combined_text)

            print("\n[Summary]:\n")
            print(combined_summary)

            logging.info("Adding query and summary to memory cache.")
            add_to_memory(query, combined_summary)

        except Exception as e:
            logging.error(f"Exception occurred in main loop: {e}", exc_info=True)
            print("An error occurred. Please try again.")

if __name__ == "__main__":
    main()
