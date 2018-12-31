import csv
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open data file
f = open('data.csv')

# to read csv data from file
csv_f = csv.reader(f)

# class for each loan purpose
class Purpose:
  def __init__(self, kind, per_loan_rate, tot_per_loan_rate, count, avg_rate):
    self.kind = kind #type of loan
    self.per_loan_rate = per_loan_rate #per loan interest rate
    self.tot_per_loan_rate = tot_per_loan_rate #total per loan interest rate
    self.count = count #instances of this loan purpose
    self.avg_rate = avg_rate #avg interest rate

  # function to calculate average interest rate
  def int_rate_calc( Purpose ):
	for row in csv_f:
		if row[16] == Purpose.kind:
			Purpose.per_loan_rate = float(row[5])
			Purpose.tot_per_loan_rate += Purpose.per_loan_rate
			Purpose.count += 1
	Purpose.avg_rate += Purpose.tot_per_loan_rate/Purpose.count
	f.seek(0) #to return to the top of the csv file 
	return;

# initializing each Purpose object and calls to int_rate_calc function

debt_consolidation = Purpose("debt_consolidation",0.0,0.0,0.0,0.0)
debt_consolidation.int_rate_calc()

house = Purpose("house",0.0,0.0,0.0,0.0)
house.int_rate_calc()

car = Purpose("car",0.0,0.0,0.0,0.0)
car.int_rate_calc()

medical = Purpose("medical",0.0,0.0,0.0,0.0)
medical.int_rate_calc()

vacation = Purpose("vacation",0.0,0.0,0.0,0.0)
vacation.int_rate_calc()

credit_card = Purpose("credit_card",0.0,0.0,0.0,0.0)
credit_card.int_rate_calc()

other = Purpose("other",0.0,0.0,0.0,0.0)
other.int_rate_calc()

moving = Purpose("moving",0.0,0.0,0.0,0.0)
moving.int_rate_calc()

wedding = Purpose("wedding",0.0,0.0,0.0,0.0)
wedding.int_rate_calc()

small_business = Purpose("small_business",0.0,0.0,0.0,0.0)
small_business.int_rate_calc()

major_purchase = Purpose("major_purchase",0.0,0.0,0.0,0.0)
major_purchase.int_rate_calc()

home_improvement = Purpose("home_improvement",0.0,0.0,0.0,0.0)
home_improvement.int_rate_calc()

f.close() #close file

# dataframe to convert output data to csv file
data = {'purpose': ['car', 'credit_card', 'debt_consolidation', 'home_improvement', 'house', 'major_purchase', 'medical', 'moving', 'other', 'small_business', 'vacation', 'wedding'], 
        'avg_rate': [car.avg_rate, credit_card.avg_rate, debt_consolidation.avg_rate, home_improvement.avg_rate, house.avg_rate, major_purchase.avg_rate, medical.avg_rate, moving.avg_rate, other.avg_rate, small_business.avg_rate, vacation.avg_rate, wedding.avg_rate]}
df = pd.DataFrame(data, columns = ['purpose', 'avg_rate'])
df

df.to_csv('results.csv')

# x-coordinates of left sides of bars  
left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
  
# heights of bars 
rate = [car.avg_rate, credit_card.avg_rate, debt_consolidation.avg_rate, home_improvement.avg_rate, house.avg_rate, major_purchase.avg_rate, medical.avg_rate, moving.avg_rate, other.avg_rate, small_business.avg_rate, vacation.avg_rate, wedding.avg_rate] 
  
# labels for bars 
tick_label = ['car', 'credit_card', 'debt_consolidation', 'home_improvement', 'house', 'major_purchase', 'medical', 'moving', 'other', 'small_business', 'vacation', 'wedding'] 
  
# size of plot 
plt.rcParams['figure.figsize'] = (25,10)

# background plot color
plt.rcParams['axes.facecolor'] = 'whitesmoke'

# plotting bar graph 
plt.bar(left, rate, tick_label = tick_label, 
        width = 0.8, color = ['mediumaquamarine', 'lightsalmon', 'steelblue', 'plum', 'yellowgreen', 'gold', 'burlywood', 'lightslategray', 'orchid', 'deepskyblue', 'thistle', 'coral']) 
  
# x-axis label
plt.xlabel('purpose') 
# y-axis label
plt.ylabel('mean(int_rate)') 
# plot title 
plt.title('MAIS 202 Coding Challenge - Karim Hout') 

# output png file for plot
out_png = 'results.png'
plt.savefig(out_png, dpi=300)