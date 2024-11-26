import requests
import pandas as pd

def fetch_google_results(query, api_key, cse_id, num_results=10, output_file="search_results.csv"):
    """
    Fetches search results from Google Custom Search JSON API and saves them to a CSV file.

    Args:
        query (str): The search query.
        api_key (str): Your Google API key.
        cse_id (str): Your custom search engine ID.
        num_results (int): Number of results to fetch (default is 10).
        output_file (str): File name to save the results (default is 'search_results.csv').
    """
    # Base URL for Google Custom Search API
    base_url = "https://www.googleapis.com/customsearch/v1"
    
    # Construct request parameters
    params = {
        "q": query,
        "key": api_key,
        "cx": cse_id,
        "num": min(num_results, 10)  # API limits results to 10 per request
    }

    # Make the GET request
    response = requests.get(base_url, params=params)

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        results = []

        # Extract and format the search results
        for item in data.get("items", []):
            results.append({
                "Title": item.get("title"),
                "Link": item.get("link"),
                "Description": item.get("snippet")
            })

        # Save results to a CSV file
        if results:
            df = pd.DataFrame(results)
            df.to_csv(output_file, index=False)
            print(f"Results saved to '{output_file}'")
        else:
            print("No results found.")
    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    # Replace with your actual Google API Key and CSE ID
    API_KEY = "YOUR_GOOGLE_API_KEY"
    CSE_ID = "YOUR_CUSTOM_SEARCH_ENGINE_ID"

    # Input query from user
    search_query = input("Enter your search query: ")

    # Fetch and save search results
    fetch_google_results(search_query, API_KEY, CSE_ID)
