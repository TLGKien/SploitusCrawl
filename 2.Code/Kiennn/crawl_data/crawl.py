import requests
import sys

def build_headers():
    return {
        "Host": "sploitus.com",
        "Cookie": "_ym_uid=1702692995328423413; _ym_d=1702692995; _ym_isad=2; _gid=GA1.2.1839175796.1703206948; cf_clearance=8kS0GQINisa6BPuMQ1mIBhGZSl2LnM4tvAGwRlEaj84-1703246664-0-2-f6c4f1aa.ccc4806.a1c5ae4a-0.2.1703246664; _ga_MEMT0D846W=GS1.1.1703232587.4.1.1703232922.60.0.0; _ga=GA1.2.1566257637.1702692995; _gat_gtag_UA_125861816_1=1",
        "Sec-Ch-Ua": '"Chromium";v="117", "Not;A=Brand";v="8"',
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.63 Safari/537.36",
        "Sec-Ch-Ua-Platform": '"Linux"',
        "Origin": "https://sploitus.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://sploitus.com/?query=CVE-2023-32315",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
    }

def build_data(cve):
    return {
        # "type": "exploits",
        # "sort": "default",
        # "query": cve,
        # "title": False,
        # "offset": 0,
    }

def make_request(url, headers, data):
    response = requests.post(url, headers=headers, json=data)
    # response = requests.get(url)
    print(response)
    return response

def process_response(response):
    if response.status_code == 200:
        print("headers:")
        print(response.headers)
        print("----------------------------------\nbody")
        print(response.text)
        json_response = response.json()
        exploits = json_response.get("exploits", [])
        for exploit in exploits:
            title = exploit.get("title", "")
            score = exploit.get("score", "")
            href = exploit.get("href", "")
            print(f"Title: {title}, Score: {score}, Href: {href}")
    else:
        print(f"Request failed with status code {response.status_code}")

def search_exploits_by_cve(cve):
    url = "https://sploitus.com/"
    headers = build_headers()
    data = build_data(cve)

    response = make_request(url, headers, data)
    process_response(response)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 crawl.py <CVE-Number>")
        sys.exit(1)

    cve_to_search = sys.argv[1]
    search_exploits_by_cve(cve_to_search)

if __name__ == "__main__":
    main()