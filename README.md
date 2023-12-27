# sploitGET
Truy vấn đơn giản từ trang https://sploitus.com và xuất kết quả ra file dưới dạng file JSON

## Usage

```bash
>>> python3 sploitGET.py --help      

usage: main.py [-h] -q QUERY [-t {exploits,tools}] [-s {default,date,score}]

options:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        search query
  -t {exploits,tools}, --type {exploits,tools}
                        Search for either public exploits or tools
  -s {default,date,score}, --sort {default,date,score}
                        Sort the results by chosen option
```


### Example

Tìm kiếm mã khai thác với mã CVE-2023-32315 và sắp xếp theo điểm đánh giá
```bash
>>> python3 main.py -q "CVE-2023-32315" -s score

```

Tìm kiếm công cụ với tên công cụ gobuster 
```bash
>>> python3 main.py -q "gobuster" -t tools
```