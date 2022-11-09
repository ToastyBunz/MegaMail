# make tk pretty agian https://github.com/TomSchimansky/CustomTkinter

import pandas as pd

excel_file = "E:/EmailTesting.xlsx"
email = 'email'
name = 'name'

df = pd.DataFrame(pd.read_excel(excel_file))
df[email] = df[email].astype('string')

print(df)
df = df.dropna(axis=0, subset=[email])
df = df.fillna(0, axis=0)
df = df.drop_duplicates(subset=email)
df = df.reset_index()
del df['index']
print(df)

print('there are now {} emails after cleaning'.format(len(df)))


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
    return df.iloc[:, email_column]

