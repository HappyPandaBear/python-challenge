import csv

total_months = 0
total_change = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""
previous = 0.0
average_change = 0
    
with open('budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        current = float(row[1])
        if total_months == 0:
            greatest_increase = 0.0
            greatest_decrease = 0.0
            greatest_increase_date = row[0]
            greatest_decrease_date = row[0]
        else:
            timedelta = current - previous
            average_change += timedelta
            if timedelta > greatest_increase:
                greatest_increase = timedelta
                greatest_increase_date = row[0]
            elif timedelta < greatest_decrease:
                greatest_decrease = timedelta
                greatest_decrease_date = row[0]

        previous = current
        total_months += 1
        total_change += float(row[1])

average_change = average_change / (total_months-1)

print(f'Financial Analysis')
print(f'-------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${round(total_change)}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase_date} ${round(greatest_increase)}')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} ${round(greatest_decrease)}')

file = open('pybank.txt','a')
file.write('Financial Analysis\n')
file.write('-------------------------\n')
file.write(f'Total Months: {total_months}\n')
file.write(f'Total: ${round(total_change)}\n')
file.write(f'Average Change: ${average_change:.2f}\n')
file.write(f'Greatest Increase in Profits: {greatest_increase_date} ${round(greatest_increase)}\n')
file.write(f'Greatest Decrease in Profits: {greatest_decrease_date} ${round(greatest_decrease)}\n')
file.close()