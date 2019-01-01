# Author: Karim Hout 
import csv
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import collections

# open csv file and read data
f = open('data.csv')
csv_f = csv.reader(f)

# class for each loan purpose
class Purpose:
  def __init__(self, name, sum_loan_rate, count, avg_rate):
    self.name = name # name of purpose
    self.sum_loan_rate = sum_loan_rate # sum of loan interest rate
    self.count = count # count of purpose
    self.avg_rate = avg_rate # avg interest rate 

  # function to calculate average interest rate
  def int_rate_calc( Purpose, purpose_col, rate_col ):
    for row in csv_f:
        if row[purpose_col] == Purpose.name:
            Purpose.sum_loan_rate += float(row[rate_col])
            Purpose.count += 1
    Purpose.avg_rate += Purpose.sum_loan_rate/Purpose.count
    f.seek(0) # return to top of csv file
    return;

row_index = 0
col_index = 0
rate_col = 0
purpose_col = 0
names = [] # list of unique purposes
purposes = [] # list of purpose objects
purposes_rates = collections.OrderedDict() # ordered dictionary of purpose:avg_rate pairs

# loop through csv file to determine int_rate column and purpose column
# populate names
for row in csv_f:
    if row_index == 0:
        for cell in row:
            if cell == "int_rate":
                rate_col = col_index
            elif cell == "purpose":
                purpose_col = col_index
            col_index += 1
        row_index += 1
    else:
        if row[purpose_col] not in names:
            names.append(row[purpose_col])
f.seek(0) # return to top of csv file

# populate purposes with new purpose objects
for name in names:
    purposes.append(Purpose(name,0.0,0.0,0.0))

# sort purposes alphabetically
purposes.sort(key=lambda purpose: purpose.name, reverse=False)

# populate purposes_rates with purpose:avg_rate pairs
for purpose in purposes:
    purpose.int_rate_calc(purpose_col, rate_col)
    purposes_rates[purpose.name] = purpose.avg_rate

f.close() #close file

# convert output data to csv file
data = {'purpose': purposes_rates.keys(), 
        'avg_rate': purposes_rates.values()}
df = pd.DataFrame(data, columns = ['purpose', 'avg_rate'])
df
df.to_csv('results.csv')

# generate bar graph 
# x-coordinates of left sides of bars
left = []
index = 0
for pair in purposes_rates:
    left.append(index)
    index += 1

rate = purposes_rates.values()
tick_label = purposes_rates.keys() 
plt.rcParams['figure.figsize'] = (25,10)
plt.rcParams['axes.facecolor'] = 'whitesmoke'
plt.bar(left, rate, tick_label = tick_label, 
        width = 0.8, color = ['mediumaquamarine', 'lightsalmon', 'steelblue', 'plum', 'yellowgreen', 'gold', 'burlywood', 'lightslategray', 'orchid', 'deepskyblue', 'thistle', 'coral'])  
plt.xlabel('purpose') 
plt.ylabel('mean(int_rate)')  
out_png = 'results.png'
plt.savefig(out_png, dpi=300)






