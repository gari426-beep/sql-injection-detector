import sqlite3

username = input("Username: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users WHERE username = ?", (username,))