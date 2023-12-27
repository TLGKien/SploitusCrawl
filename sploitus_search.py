# sploitus_search.py
import json
import math
from sploitus_api import SploitusAPI

class SploitusSearch(SploitusAPI):
    def __init__(self, query, qtype='exploits', sort='default'):
        """
        Khởi tạo một đối tượng SploitusSearch.

        Parameters:
        - query (str): Từ khóa tìm kiếm.
        - qtype (str): Loại tìm kiếm, có thể là 'exploits' hoặc 'tools'. Giá trị mặc định là 'exploits'.
        - sort (str): Cách sắp xếp kết quả, có thể là 'default', 'date', hoặc 'score'. Giá trị mặc định là 'default'.
        """

        super().__init__(query, qtype, sort)

    def exec_query(self):
        """
        Thực hiện yêu cầu tìm kiếm và xử lý kết quả.
        """
        headers = self._init_header()
        json_data = self._init_query()

        exploits_total = self._get_data_total()

        if exploits_total > 0:
            total_pages = math.ceil(exploits_total / 10)
            all_results = []

            for page in range(total_pages):
                json_data['offset'] = page * 10
                response = self._make_post_request(url=self.url, headers=headers, data=json_data)

                if response.status_code == 200:
                    try:
                        response_data = response.json()
                        results_on_page = response_data.get("exploits", [])
                        all_results.extend(results_on_page)
                    except json.JSONDecodeError as e:
                        print(f"JSON Decode Error: {e}")
                else:
                    print(f"Request failed with status code {response.status_code}")

            self.dump_to_file(all_results, exploits_total)
        else:
            print("No exploits found.")

    def dump_to_file(self, data, exploits_total):
        """
        Ghi dữ liệu vào một tệp JSON.
        """
        filename = f"{self.type}_{self.query}_all.json"
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump({"exploits": data, "exploits_total": exploits_total}, file, ensure_ascii=False, indent=4)
        print(f"Data dumped to file: {filename}")
