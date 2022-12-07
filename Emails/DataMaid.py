# make tk pretty agian https://github.com/TomSchimansky/CustomTkinter

import pandas as pd

excel_file = "S:/Python/Code/MegaMail/Emails/Testing_Tools/EmailTesting.xlsx"
# email = 'email'
# name = 'name'
#
# df = pd.DataFrame(pd.read_excel(excel_file))
# df[email] = df[email].astype('string')

class MyError(Exception):
    def __int__(self, message):
        self.message = message


unknown_file = MyError('Unknown filetype, please enter CSV or Excel')


def contacts_processing(outreach_file):
    if outreach_file.endswith('.xlsx'):
        df = pd.DataFrame(pd.read_excel(outreach_file))
    elif outreach_file.endswith('.csv'):
        df = pd.DataFrame(pd.read_csv(outreach_file))
    else:
        raise unknown_file

    df['email'] = df['email'].astype('string')

    df = df.dropna(axis=0, subset=['email'])
    df = df.fillna(0, axis=0)
    df = df.drop_duplicates(subset='email')
    df = df.reset_index()
    del df['index']
    return df


def detect_email_column(dataframe):
    for index, name in enumerate(dataframe.loc[0]):
        if type(name) is not str:
            pass
        else:
            if '@' and '.com' in name:
                column = index
    return column


def get_email_column(dataframe):
    email_column = detect_email_column(dataframe)
    return dataframe.iloc[:, email_column]


def get_email_in_column(dataframe, index):
    # UNNECESSARY MEGA MAIL ALREADY DOES: This function is meant to be paired with a loop to return emails one at a time
    email_column = dataframe.columns.get_loc('email')
    return dataframe.iloc[index, email_column]

print(contacts_processing("S:/Python/Code/MegaMail/Emails/Testing_Tools/EmailTesting.xlsx"))