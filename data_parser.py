import json
import sys
import os

def main():
	if len(sys.argv) == 3:
		filepath = sys.argv[1]
		date = sys.argv[2]
	else:
		print("usage: python data_parser.py raw_data/data_filename.txt yyyy-mm-dd")
		sys.exit()

	if not os.path.isfile(filepath):
		print("File path {} does not exist".format(filepath))
		sys.exit()

	with open(filepath, 'r') as data_file:
		#skip header
		for i in range(0,14):
			data_file.readline()
			i += 1
		data_str = data_file.read()

	tmp = json.loads(data_str)
	del tmp['Meta Data']
	data = tmp['Time Series (Daily)']

	if date in data:
		first_node = data[date]
		print(date)
		print("open: {}".format(first_node['1. open']))
		print("high: {}".format(first_node['2. high']))
		print("low: {}".format(first_node['3. low']))
		print("close: {}".format(first_node['4. close']))
		print("volume: {}".format(first_node['5. volume']))
	else:
		print("date not in data")

if __name__ == '__main__':
	main()