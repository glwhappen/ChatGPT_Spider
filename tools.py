import re

def get_id_from_url(url):
    """
    Extracts the ID from a given OpenAI Chat URL.

    Parameters:
    - url (str): The URL from which to extract the ID.

    Returns:
    - str: The extracted ID or a message indicating that no ID was found.
    """
    # Regular expression to match the ID in the URL
    match = re.search(r"https://chat.openai.com/c/([a-z0-9\-]+)", url)
    # Extract and return the ID if found, otherwise return a message
    return match.group(1) if match else "No ID found"


if __name__ == '__main__':
    print(get_id_from_url("https://chat.openai.com/c/5e66cd70-5a60-4692-9c94-bb64856c4e31"))