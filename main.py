# main.py
import argparse
from sploitus_search import SploitusSearch

def main():
    """
    Hàm chính của chương trình, xử lý đối số dòng lệnh và thực hiện tìm kiếm.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query', type=str, help='search query', required=True)
    parser.add_argument('-t', '--type', type=str, default='exploits', choices=['exploits', 'tools'],
                        help='Search for either public exploits or tools')
    parser.add_argument('-s', '--sort', type=str, default='default', choices=['default', 'date', 'score'],
                        help='Sort the results by chosen option')
    args = parser.parse_args()
    
    sploit_search = SploitusSearch(query=args.query, qtype=args.type, sort=args.sort)
    sploit_search.exec_query()

if __name__ == "__main__":
    main()
