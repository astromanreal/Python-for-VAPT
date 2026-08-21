import requests

def load_wordlist(filepath):
    with open(filepath, "r") as f:
        return [line.strip() for line in f if line.strip()]

def build_url(base_url, word):
    return f"{base_url.rstrip('/')}/{word}"

def check_url(url, timeout=5):
    try:
        res = requests.get(url, timeout=timeout, allow_redirects=False)
        return res.status_code
    except requests.exceptions.RequestException:
        return None

def enumerate_directories(base_url, wordlist_path):
    words = load_wordlist(wordlist_path)
    interesting_codes = {200, 301, 302, 403}

    for word in words:
        url = build_url(base_url, word)
        status = check_url(url)

        if status is None:
            continue

        if status in interesting_codes:
            print(f"{status} -> {url}")


if __name__ == "__main__":
    enumerate_directories("https://httpbin.org", "wordlist.txt")