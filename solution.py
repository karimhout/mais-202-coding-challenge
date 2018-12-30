import csv
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

f = open('data.csv')

csv_f = csv.reader(f)

class Purpose:
  def __init__(self, kind, per_loan_wf, tot_per_loan_wf, tot_loan, avg_rate):
    self.kind = kind
    self.per_loan_wf = per_loan_wf
    self.tot_per_loan_wf = tot_per_loan_wf
    self.tot_loan = tot_loan
    self.avg_rate = avg_rate

  def int_rate_calc( Purpose ):
	for row in csv_f:
		if row[16] == Purpose.kind:
			Purpose.per_loan_wf = float(row[2]) * float(row[5])/float(100)
			Purpose.tot_per_loan_wf += Purpose.per_loan_wf
			Purpose.tot_loan += float(row[2])
			Purpose.avg_rate = float(100) * Purpose.tot_per_loan_wf/Purpose.tot_loan
	f.seek(0) #to return to the top of the csv file after each function call
	return;

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

f.close()

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
  
plt.rcParams['figure.figsize'] = (25,10)

plt.rcParams['axes.facecolor'] = 'whitesmoke'

# plotting a bar chart 
plt.bar(left, rate, tick_label = tick_label, 
        width = 0.8, color = ['mediumaquamarine', 'lightsalmon', 'steelblue', 'plum', 'yellowgreen', 'gold', 'burlywood', 'lightslategray', 'orchid', 'deepskyblue', 'thistle', 'coral']) 
  
# naming the x-axis 
plt.xlabel('purpose') 
# naming the y-axis 
plt.ylabel('mean(int_rate)') 
# plot title 
plt.title('MAIS 202 Coding Challenge - Karim Hout') 

out_png = 'results.png'
plt.savefig(out_png, dpi=200)










