from bs4 import BeautifulSoup
import requests

zimmo_url: str = "https://www.zimmo.be/nl/gent-9000/te-huur/appartement"

def get_soup(url) -> str:
    """Gets all html from the page and returns it in a string."""
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html")
    return soup



if __name__ == "__main__":
    pass