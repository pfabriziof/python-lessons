import requests
from pathlib import Path

def square(x: float) -> float:
    return x**2

def getssh():
    """Simple function to return expanded homedir ssh path."""
    return Path.home() / ".ssh"

def get_json(url: str):
    """Takes a URL, and returns the JSON."""
    r = requests.get(url)
    return r.json()

if __name__ == "__main__":
    print(getssh())
