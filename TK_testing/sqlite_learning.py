import sqlite3
from pathlib import Path

import pandas as pd

Path('S:/Python/Code/MegaMail/contact_data/my_data.db').touch()
conn = sqlite3.connect('S:/Python/Code/MegaMail/contact_data/my_data.db')
c = conn.cursor()

# c.execute('''CREATE TABLE users (user_id int, username text)''')
user_path = 'S:/Python/Code/MegaMail/contact_data/users.csv'

users = pd.read_csv(user_path)
users.to_sql('users', conn, if_exists='append', index=False)


demo = c.execute('''SELECT * FROM users''').fetchall()
print(demo)