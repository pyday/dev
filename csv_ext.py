import csv

with open('/Users/wangcl/Documents/files/pre_data.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)
    print your_list[0][0].decode('utf8')