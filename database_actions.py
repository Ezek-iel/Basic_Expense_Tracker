import sqlite3

sql_file = open("sql/add_record.sql","r").read()
sql_file2 = open("sql/fetchall.sql","r").read()
sql_file3 = open("sql/delete_last_record.sql","r").read()

connection = sqlite3.connect("expense.db")

cursor = connection.cursor()

def add_record(date : str, time : str, description : str, amount : int, income_or_expense : int, satisfied : int) -> None:
    cursor.executemany(sql_file,[(date, time, description, amount, income_or_expense, satisfied)])
    print("Command Executed Succesfully")
    connection.commit()


def get_all_records() -> list[tuple]:
    cursor.execute(sql_file2)
    return cursor.fetchall()


def delete_last_record():
    record_length  = len(get_all_records())
    print(record_length)
    cursor.execute(sql_file3,str(record_length))
    connection.commit()


delete_last_record()
print(get_all_records())