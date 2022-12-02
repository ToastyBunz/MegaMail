import pickle

def file_run_counter(file_name):
    number = 1
    file_name = file_name + '.pickle'
    try:
        with open(file_name, 'xb') as file:
            pickle.dump(number, file)
            return number
    except:
        # check if number in pickle == 24
        # if number != 24 add one and re-save file

        with open(file_name, 'rb+') as file:
            value = pickle.load(file)
            if value >= 24:
                file.seek(0)
                file.truncate()
                pickle.dump(number, file)
                return number
            else:
                new_value = value + 1
                file.seek(0)
                file.truncate()
                pickle.dump(new_value, file)
                return new_value


# if number == 24 delete token.pickle, and restart counter at 0