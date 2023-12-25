import requests
from http.cookiejar import CookieJar

def build_header():
    headers = {
        'Host': 'sploitus.com',
        'Content-Length': '15347',
        'Sec-Ch-Ua': '"Chromium";v="117", "Not;A=Brand";v="8"',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.63 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Origin': 'https://sploitus.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    return headers

def build_data(cve):
    return {
        "type": "exploits",
        "sort": "default",
        "query": cve,
        "title": False,
        "offset": 0,
    }

# Tạo một đối tượng CookieJar để lưu trữ cookie
cookie_jar = CookieJar()

# Tạo một đối tượng Session từ requests và gán CookieJar vào Session
session = requests.Session()
session.cookies = cookie_jar

# Gửi một yêu cầu GET để nhận các cookie từ trang web
url = "https://sploitus.com/cdn-cgi/challenge-platform/h/g/jsd/r/83983a199e607161"
response = session.get(url, headers=build_header())

# In ra các cookie đã nhận được
print("Cookies after GET request:")
print(response)
print(response.headers)
for cookie in cookie_jar:
    print(cookie)

# Gửi một yêu cầu POST với cookie đã nhận được
# payload = {"key": "value"}
# response_post = session.post(url, json=build_data("CVE-2023-32315"))
# print(response_post)

# # In ra nội dung trang web sau khi gửi yêu cầu POST
# print("Content after POST request:")
# print(response_post.text)
