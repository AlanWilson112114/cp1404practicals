import wikipedia


def main():
    query = input("Search Wikipedia: ").strip()
    while query != "":
        try:
            page_result = wikipedia.page(query, auto_suggest=False)
            print(page_result.title)
            print(page_result.url)
            print(page_result.summary)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options[:10])  # limit output for readability
        except wikipedia.exceptions.PageError:
            print(f'Page id "{query}" does not match any pages. Try another id!')
        except Exception as exc:
            print(f"Unexpected error: {exc}")
        finally:
            query = input("Search Wikipedia: ").strip()


if __name__ == "__main__":
    main()
