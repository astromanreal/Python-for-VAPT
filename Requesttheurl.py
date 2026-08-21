import requests

try:
    url="https://www.youtube.com/"
    response=requests.get(url, timeout=5)
    response.raise_for_status()
    


    print(response.status_code)

    if response.headers:
        print(response.headers.get("server", "not found"))
    
    print(response.text[:100])


except requests.exceptions.RequestException as e:
    print("Error", e)