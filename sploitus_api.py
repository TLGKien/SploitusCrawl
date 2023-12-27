# sploitus_api.py
import httpx
import json
import math

class SploitusAPI:
    def __init__(self, query, qtype='exploits', sort='default'):
        """
        Khởi tạo một đối tượng SploitusAPI.

        Parameters:
        - query (str): Từ khóa tìm kiếm.
        - qtype (str): Loại tìm kiếm, có thể là 'exploits' hoặc 'tools'. Giá trị mặc định là 'exploits'.
        - sort (str): Cách sắp xếp kết quả, có thể là 'default', 'date', hoặc 'score'. Giá trị mặc định là 'default'.
        """

        self.query = query
        self.type = qtype
        self.sort = sort
        self.offset = 0
        self.url = 'https://sploitus.com/search'

    def _init_query(self):
        """
        Khởi tạo dữ liệu JSON cho yêu cầu tìm kiếm.
        """

        json_data = {
            'type': self.type,
            'sort': self.sort,
            'query': self.query,
            'title': False,
            'offset': 0,
        }
        return json_data
    
    def _init_header(self):
        """
        Khởi tạo header cho yêu cầu HTTP.
        """

        headers = {
            'authority': 'sploitus.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://sploitus.com',
            'referer': 'https://sploitus.com/?query=' + self.query,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        return headers
    
    def _make_post_request(self, url, headers, data, timeout=5):
        """
        Thực hiện yêu cầu HTTP POST.
        """
        
        try:
            with httpx.Client(http2=True, timeout=timeout) as client:
                response = client.post(url, headers=headers, json=data)
                response.raise_for_status()  # Nếu có lỗi HTTP response status code, ngoại lệ sẽ được ném.
            return response        
        except httpx.TimeoutException as e:
            print(f"Timeout exception: {e}")
        except httpx.RequestError as e:
            print(f"Request error: {e}")
        except httpx.HTTPError as e:
            print(f"HTTP error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _get_data_total(self):
        """
        Truy vấn để lấy giá trị của trường exploits_total.
        """
        headers = self._init_header()
        json_data = self._init_query()

        response = self._make_post_request(url=self.url, headers=headers, data=json_data)

        if response.status_code == 200:
            try:
                response_data = response.json()
                print("total = ", response_data.get("exploits_total", 0))
                return response_data.get("exploits_total", 0)
            except json.JSONDecodeError as e:
                print(f"JSON Decode Error: {e}")

        return 0
