import requests

def check_security_headers(url):
    security_headers=[
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy",
        "Permissions-Policy"
    ]

    try:
        res=requests.get(url, timeout=5)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error:",e)
        return

    print(f"\n Security header report for: {url} \n {'-'*40}")

    for header in security_headers:
        if header in res.headers:
            print(f" {header}")
        else:
            print(f"N/A {header}")


if __name__ == "__main__":
     target="https://jsonplaceholder.typicode.com/users"
     check_security_headers(target)

