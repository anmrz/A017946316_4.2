"""Calculate total amount."""
import sys
import time
import json


startTime = time.time()

if len(sys.argv) != 3:
    print("Provide the file n_ame as a command line argument.")
    sys.exit()

PROD_FILE = str(sys.argv[1])
SALES_RECORDS = str(sys.argv[2])

with open(PROD_FILE, 'r') as f:
    prod_data = json.load(f)

with open(SALES_RECORDS, 'r') as g:
    sales_data = json.load(g)


def get_quantities_prod(sales_info):
    """Computes quantity saled by product"""
    quantities_by_prod = {}
    for sale_entry in sales_info:
        if sale_entry["Product"] in quantities_by_prod.keys():
            quantities_by_prod[sale_entry['Product']] += sale_entry['Quantity']
        else:
            quantities_by_prod[sale_entry["Product"]] = sale_entry['Quantity']
    return quantities_by_prod


def compute_total(quantities_by_prod, prod_info):
    """Consults price for each product and sum total amount"""
    total_amount = 0
    for prod_entry in prod_info:
        if prod_entry['title'] in quantities_by_prod:
            subtotal_am = (prod_entry['price'] *
                           quantities_by_prod[prod_entry['title']])
            total_amount += subtotal_am
    return round(total_amount, 2)


dict_quantities_by_prod = get_quantities_prod(sales_data)
sales_amount = compute_total(dict_quantities_by_prod, prod_data)

time_elapsed = time.time() - startTime
print("--- %s seconds elapsed" % time_elapsed)

with open('SalesResults.txt', 'a') as f:
    f.write(SALES_RECORDS + ' total:\n')
    f.write(str(sales_amount) + '\n')
    f.write('Execution time:' + str(time_elapsed) + ' seconds\n')
    f.write('--------------------------------------------------\n')
