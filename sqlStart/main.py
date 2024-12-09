import sqlite3

# try:
#     sql_connect = sqlite3.connect('my_first_DataBase.db')
#     cursor = sql_connect.cursor()
#     print('DB created and connected)))))')

#     sql_select_query = 'select sqlite_version()'
#     cursor.execute(sql_select_query)
#     record  =cursor.fetchall()
#     print('version of DB: ', record)
#     cursor.close()

# try:
#     sql_connect = sqlite3.connect('my_first_DataBase.db')
#     create_table = '''
#                 CREATE TABLE first_table(
#                 id INTEGER PRIMARY KEY,
#                 name TEXT NOT NULL,
#                 email TEXT NOT NULL UNIQUE,
#                 joining_date datetime,
#                 salary REAL NOT NULL)'''


#     cursor = sql_connect.cursor()
#     print('DB connected)))))')

#     cursor.execute(create_table)
#     sql_connect.commit()
#     print('Table created')

#     cursor.close()

# try:
#     sql_connect = sqlite3.connect('my_first_DataBase.db')
#     cursor = sql_connect.cursor()
#     print('DB connected)))))')
    
#     sql_insert = '''
#                 INSERT INTO first_table(
#                 name, email, joining_date, salary)
#                 VALUES
#                 ('John', 'iasudasid@gmail.com', '2024-12-09', 40000);
# '''
#     count = cursor.execute(sql_insert)
#     sql_connect.commit()
#     print('Inserted.', cursor.rowcount)
#     cursor.close()

def insert_vars_into_table(man_id, man_name, man_email, man_date, man_salary):
    try:
        sql_connect = sqlite3.connect('my_first_DataBase.db')
        cursor = sql_connect.cursor()
        print('DB connected)))))')

        sql_insert_vars = '''
        INSERT INTO first_table
        (id, name, email, joining_date, salary)
        VALUES (?, ?, ?, ?, ?);
        '''

        data_tuple = (man_id, man_name, man_email, man_date, man_salary)
        cursor.execute(sql_insert_vars, data_tuple)
        sql_connect.commit()
        print('ok')
        cursor.close()


    except sqlite3.Error as error:
        print('Error with connection ', error)
    finally:
        if sql_connect:
            sql_connect.close()
            print('connection closed')


insert_vars_into_table(2, 'Carl', 'asdas@dsfsd.cvsd', '2023-09-27', 34.56)