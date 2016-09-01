import json

with open('store_data.json', 'r') as data_file:    
    json_data = json.load(data_file)

prices = []

def most_expensive():

	for item in json_data:
		prices.append(item['price'])

	high_price = max(prices)

	for item in json_data:
		if item['price'] == high_price:
			print("Most Expensive Item: ", item['name'])
	
def least_expensive():
	
	low_price = min(prices)

	for item in json_data:
		if item['price'] == low_price:
			print("Least Expensive Item: ", item['name'])

def total_revenue():
	revenue = []
	
	for item in json_data:
		revenue.append(item['price'] * item['sold'])

	revenue_sum = round(sum(revenue),2)

	print("Total Revenue: $", revenue_sum)

def total_profit():
	profit = []

	for item in json_data:
		profit.append((item['price'] - item['cost_to_make']) * item['sold'])

	profit_sum = round(sum(profit),2)

	print("Total Profit: $", profit_sum)

def department_sales():
	departments = []

	for item in json_data:
		departments.append(item['department'])

	departments = list(set(departments))

	for i in departments:
		departments[i] = 

	print(departments)

#sold = []

#def best_sellers():

#	for item in json_data:
#		seller_sort = sorted

#	print(seller_sort)




most_expensive()
least_expensive()
total_revenue()
total_profit()
#best_sellers()
department_sales()