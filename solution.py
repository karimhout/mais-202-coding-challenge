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
  def __init__(self, name, avg_rate):
    self.name = name # name of purpose
    self.avg_rate = avg_rate # avg interest rate of purpose

  # function to calculate average interest rate
  def int_rate_calc( self, purpose_col, rate_col ):
    sum_loan_rate = 0
    count = 0
    for row in csv_f:
        if row[purpose_col] == self.name:
            sum_loan_rate += float(row[rate_col])
            count += 1
    self.avg_rate = sum_loan_rate/count
    f.seek(0) # return to top of csv file
    return;

row_index = 0
col_index = 0
rate_col = 0
purpose_col = 0
purposes = [] # list of Purpose objects
purposes_rates = collections.OrderedDict() # ordered dictionary of purpose name - avg_rate pairs

# loop through csv file to determine int_rate column and purpose column
# append purposes with new Purpose object if name is unique
for row in csv_f:
    if row_index == 0:
        for cell in row:
            if cell == "int_rate":
                rate_col = col_index
            elif cell == "purpose":
                purpose_col = col_index
            col_index += 1
        row_index += 1
    elif not any(purpose.name == row[purpose_col] for purpose in purposes):
        purposes.append(Purpose(row[purpose_col],0.0))
f.seek(0) # return to top of csv file

# sort purposes by name 
purposes.sort(key=lambda purpose: purpose.name, reverse=False)

# populate purposes_rates with purpose name - avg_rate pairs
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
