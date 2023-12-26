import sys
import httpx
import json
import argparse

class Sploitus:
    def __init__(self, query, qtype, sort, offset):
        self.query = query
        self.type = qtype
        self.sort = sort
        self.offset = offset
        self.url = 'https://sploitus.com/search'

    def _init_query(self):        
        json_data = {
            'type': self.type,
            'sort': self.sort,
            'query': self.query,
            'title': False,
            'offset': 0,
        }
        return json_data
    
    
    def _init_header(self):
        headers = {
            'authority': 'sploitus.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://sploitus.com',
            'referer': 'https://sploitus.com/?query='+self.query,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        return headers
    
    def _make_post_request(self, url, headers, data):
        with httpx.Client(http2=True) as client:
            response = client.post(url, headers=headers, json=data)
        return response
    
    def _process_response(self, response):
        if response.status_code == 200:
            print(f"Request successed with status code {response.status_code}")
            try:
                response_text = response.text
                response_data = json.loads(response_text)
                print(response_data.get("exploits_total"))

                # Ghi dữ liệu vào file tmp.json
                with open(self.type+"_"+self.query+".json", 'w', encoding='utf-8') as file:
                    json.dump(response_data, file, ensure_ascii=False, indent=4)

                print("Saved data")
            except json.JSONDecodeError as e:
                print(f"JSON Decode Error: {e}")
        else:
            print(f"Request failed with status code {response.status_code}")
        

    def exec_query(self):
        headers = self._init_header()
        json_data = self._init_query()

        response = self._make_post_request(url=self.url, headers=headers, data=json_data)

        self._process_response(response)

        return response



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query', type=str, help='search query', required=True)
    parser.add_argument('-t', '--type', type=str, default='exploits', choices=['exploits', 'tools'],
                        help='Search for either public exploits or tools')
    parser.add_argument('-s', '--sort', type=str, default='default', choices=['default', 'date', 'score'],
                        help='Sort the results by chosen option')
    parser.add_argument('-o', '--offset', type=int, default='0',
                        help='Offset')
    args = parser.parse_args()
    sploit = Sploitus(query=args.query, qtype=args.type, sort=args.sort, offset=args.offset)
    sploit.exec_query()

if __name__ == "__main__":
    main()
