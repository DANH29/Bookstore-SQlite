# program to create table containing book data

import sqlite3

db = sqlite3.connect('T48/Task Files/Data/books')
cursor = db.cursor()
cursor.execute('''CREATE TABLE bookstore(id INTEGER PRIMARY KEY,
    Title TEXT, Author TEXT, Qty INTEGER)''')

library = [(3001, "A Tale of Two Cities", "Charles Dickens", 30),
           (3002, "Harry Potter and the Philosophers Stone", "J.K. Rowling", 40),
           (3003, "The Lion the Witch and the Wardrobe", "C.S Lewis", 25),
           (3004, "The Lord of the Rings", "J.R.R Tolkein", 37),
           (3005, "Alice in Wonderland", "Lewis Carroll", 12)]

cursor.executemany('''INSERT INTO bookstore(id, Title, Author, Qty) VALUES(?,?,?,?)''', library)

db.commit()
db.close()
