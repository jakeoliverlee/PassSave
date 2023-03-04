import sqlite3
from random import choice, randint, shuffle

class PassSaveBE:
    def __init__(self):
        connect = sqlite3.connect("pass_data.db")
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Passwords (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT, Website TEXT,
                        Email TEXT, Password TEXT)""")
        connect.commit()
        connect.close()

    def save_data(self, website, email, password):
        connect = sqlite3.connect("pass_data.db")
        cursor = connect.cursor()
        cursor.execute("""INSERT INTO Passwords (Website, Email, Password)
                        VALUES (?, ?, ?)""", (website, email, password))
        connect.commit()
        connect.close()

    def search_password(self, website):
        connect = sqlite3.connect("pass_data.db")
        cursor = connect.cursor()
        cursor.execute("""SELECT * FROM Passwords WHERE website = ?""", website)
        result = cursor.fetchone()
        connect.commit()
        connect.close()
        return result

    def generate_pass(self):
        password = ""
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums = "1234567890"
        symbols = "-+=*&^%$@"
        for char in range(1, randint(8, 12)):
            password += choice(letters)
        for num in range(1, randint(3,5)):
            password += choice(nums)
        for symbol in range(1, randint(3,5)):
            password += choice(symbols)
        password_list = list(password)
        shuffle(password_list)
        password = "".join(password_list)
        return password

