# 'r' means read only
file_for_reading = open('reading_file.txt', 'r')

# 'w' is write-will destroy the file if it already exists!
file_for_writing = open('writing_file.txt', 'w')

# 'a' is append-for adding to the end of the file
file_for_appending = open('appending_file.txt', 'a')

# don't forget to close your files when you're done
file_for_writing.close()

with open(filename, 'r') as f:
    data = function_that_gets_data_from(f)

# at this point f has already been closed, so don't try to use it
process(data)

starts_with_hash = 0

with open('input.txt', 'r') as f:
    for line in file:              # look at each line in the file
        if re.match('^#', line):   # use a regex to see if it starts with '#'
            starts_with_hash += 1  # if it does, add 1 to the count

def get_domain(email_address):
    """split on '@' and return the last piece"""
    return email_address.lower().split('@')[-1]

with open('email_addresses.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.split())
                            for line in f
                            if '@' in line)

# Delimited files

import csv

with open('tab_delimited_stock_prices.txt', 'rb') as f:
    reader = csv.reader(f, delimeter='\t')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        process(date, symbol, closing_price)

with open('colon_delimited_stock_prices.txt', 'rb') as f:
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        date = row['date']
        symbol = row['symbol']
        closing_price = float(row['closing_price'])
        process(date, symbol, closing_price)

today_prices = { 'AAPL': 90.91, 'MSFT': 41.68, 'FB': 64.5 }

with open('comma_delimited_stock_prices.txt', 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])

results = [['test1', 'success', 'Monday'],
           ['test2', 'success, kind of', 'Tuesday'],
           ['test3', 'failure, kind of', 'Wednesday'],
           ['test4', 'failure, utter', 'Thursday']]

# don't do this!
with open('bad_csv.txt', 'wb') as f:
    for row in results:
        f.write(','.join(map(str, row)))   # might have too many commas in it!
        f.write('\n')                      # row might have newlines as well!

