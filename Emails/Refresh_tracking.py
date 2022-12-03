import pickle
from datetime import datetime

def file_run_counter(file_name):
    number = 1
    file_name = file_name + '.pickle'
    try:
        with open(file_name, 'xb') as file:
            pickle.dump(number, file)
            return 0
    except:
        # check if number in pickle == 24
        # if number != 24 add one and re-save file
        # if number == 24 delete token.pickle, and restart counter at 0

        with open(file_name, 'rb+') as file:
            value = pickle.load(file)
            if value >= 24:
                file.seek(0)
                file.truncate()
                pickle.dump(number, file)
                print('hit 24')
                return 0
            else:
                new_value = value + 1
                file.seek(0)
                file.truncate()
                pickle.dump(new_value, file)
                return 1


def current_date(file_name):
    # returns 1 if creates new date file or date is same as date file, else 0
    today = datetime.today().strftime('%d-%m-%Y')
    file_name = file_name + '.pickle'
    try:
        with open(file_name, 'xb') as file:
            pickle.dump(today, file)
            return 0
    except:
        # check today '%d-%m-%Y' is the same as in date file
        # if number != 24 add one and re-save file

        with open(file_name, 'rb+') as file:
            saved_date = pickle.load(file)
            if saved_date != datetime.today().strftime('%d-%m-%Y'):
                file.seek(0)
                file.truncate()
                pickle.dump(today, file)
                print('wrong date')
                return 0
            else:
                return 1


# x = file_run_counter('run_counter')
# y = current_date('date_counter')
#
# print(x)
# print(y)