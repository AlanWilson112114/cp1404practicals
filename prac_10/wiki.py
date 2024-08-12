import wikipedia  # Importing the wikipedia module to interact with the Wikipedia API

query = input("Search Wikipedia: ")  # Prompt the user to enter a search query
while query != "":  # Continue to loop as long as the user provides input
    page_result = wikipedia.page(query)  # Search for the Wikipedia page with the query
    print(page_result.title)  # Print the title of the found Wikipedia page
    print(page_result.url)  # Print the URL of the found Wikipedia page
    print(page_result.summary)  # Print the summary of the found Wikipedia page
    query = input("Search Wikipedia: ")  # Prompt the user to search for another term
