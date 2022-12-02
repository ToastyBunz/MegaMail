from datetime import datetime

fifteeth = "30-11-2022"
# fifteeth_dt = datetime.strptime(fifteeth, '%d/%m/%Y')

today = datetime.today().strftime('%d-%m-%Y')
print(type(today))

if today == fifteeth:
    print('Today is the 15th')
else:
    print('YOU STUPID')