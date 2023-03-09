# bookstore program

# allows users to
# add books to prepopulated table
# update current stored books
# delete stored books
# search stored book data

import sqlite3

db = sqlite3.connect('/Users/djhod/Documents/HyperionDev/T48/books')
cursor = db.cursor()

# menu giving user each program option

while True:

    menu = input("""
Please select the option you would like to choose:
Enter a new book - n
Update a book - u
Delete a book - d
Search a book - s
Exit - e
Enter here: """)

    # option to enter data for a new book

    if menu.lower() == "n":
        while True:
            try:
                # prompt user for new book id
                new_id = int(input("\nEnter book id: "))
                # has to be 4 numbers long
                if len(str(new_id)) != 4:
                    print("Id needs to be 4 numbers long")
                # cannot be an existing id
                elif cursor.execute('''SELECT id FROM bookstore WHERE id = ?''', (new_id,)).fetchone() is not None:
                    print("Book already exists")
                else:
                    break
            # book id has to be an integer
            except ValueError:
                print("Invalid id entered")

        # prompt user for title of new book
        new_title = input("\nEnter book Title: ")

        # prompt user for author of new book
        new_author = input("\nEnter book Author: ")

        while True:
            try:
                # prompt user for quantity of new book
                new_qty = int(input("\nEnter book quantity: "))
                break
            except ValueError:
                print("Invalid quantity entered")

        # insert new book details into books table
        cursor.execute('''INSERT INTO bookstore(id, Title, Author, Qty) VALUES(?,?,?,?)''',
                       (new_id,new_title,new_author,new_qty))
        db.commit()
        print("\nBook successfully added to system!")

    # option to update an existing books record
    elif menu.lower() == "u":
        update = True
        while update:
            # prompt user for the id of the book they would like to update
            select = input("\nEnter the id for the book you would like to update: ")
            # id has to be 4 numbers long
            if len(select) != 4:
                print("Invalid id entered")

            # checks if id exists in books table
            elif cursor.execute('''SELECT id FROM bookstore WHERE id = ?''', (select,)).fetchone() is None:
                print("No book with id found")

            else:
                # if id is valid print out book data
                print("\nYou have selected: ")
                print(cursor.execute('''SELECT * FROM bookstore WHERE id = ?''', (select,)).fetchone())

                # prompt user for which field they would like to update or return to menu
                while update:
                    record_update = input("\nChoose a field to update:\n"
                                          "Id - \"i\"\n"
                                          "Title - \"t\"\n"
                                          "Author - \"a\"\n"
                                          "Quantity - \"q\"\n"
                                          "Return to menu - \"m\"\n"
                                          "Enter here: ")

                    # if the user chooses to update the id
                    if record_update.lower() == "i":
                        while True:
                            try:
                                # prompt for new id
                                updated_id = int(input("\nEnter new id for book: "))
                                # id must be 4 numbers long
                                if len(str(updated_id)) != 4:
                                    print("Id must be 4 numbers long")

                                # id cannot already exist in books table
                                elif cursor.execute('''SELECT id FROM bookstore WHERE id = ?''',
                                                    (updated_id,)).fetchone() is not None:
                                    print("Id already exists in system")

                                else:
                                    # update book with new id
                                    cursor.execute('''UPDATE bookstore SET id = ? WHERE id = ?''', (updated_id,select))
                                    db.commit()
                                    update = False
                                    print("\nId successfully updated!")
                                    break
                            # book id has to be an integer
                            except ValueError:
                                print("Invalid id entered")

                    # if user chooses to update the title
                    elif record_update.lower() == "t":
                        while True:
                            # prompt for new title
                            updated_title = input("\nEnter new title for book: ")
                            # update book title in books table
                            cursor.execute('''UPDATE bookstore SET title = ? WHERE id = ?''', (updated_title, select))
                            db.commit()
                            print("\nTitle successfully updated!")
                            update = False
                            break

                    # if user chooses to update author
                    elif record_update.lower() == "a":
                        # prompt for new author
                        updated_author = input("\nEnter new author for book: ")
                        # update book author in books table
                        cursor.execute('''UPDATE bookstore SET author = ? WHERE id = ?''', (updated_author, select))
                        db.commit()
                        print("\nAuthor successfully updated!")
                        update = False
                        break

                    # if user chooses to update quantity
                    elif record_update.lower() == "q":
                        while True:
                            try:
                                # prompt for new quantity
                                updated_qty = int(input("\nEnter new quantity for book: "))
                                # update book quantity in books table
                                cursor.execute('''UPDATE bookstore SET qty = ? WHERE id = ?''', (updated_qty, select))
                                db.commit()
                                print("\nQuantity successfully updated!")
                                update = False
                                break
                            # quantity has to be an integer
                            except ValueError:
                                print("Invalid quantity entered")

                    # if user chooses to return to menu
                    elif record_update.lower() == "m":
                        update = False
                        break

                    # if user enters an invalid option
                    else:
                        print("Invalid option entered")

    # option to delete book record from books table
    elif menu.lower() == "d":
        delete = True
        while delete:
            try:
                # prompt for id of book to be deleted
                delete_book = int(input("\nEnter the id for the book you would like to delete: "))
                # check if book id exists in books table
                if cursor.execute('''SELECT id FROM bookstore WHERE id = ?''', (delete_book,)).fetchone() is None:
                    print("No book with id found")

                else:
                    # print out book data
                    print("\nYou have selected to delete: ")
                    print(cursor.execute('''SELECT * FROM bookstore WHERE id = ?''', (delete_book,)).fetchone())

                    # check if user would like to delete record or to return to menu
                    while True:
                        confirm = input("\nIf you would like to continue and delete this book enter \"y\"\n"
                                        "Or enter \"m\" to return to menu\n"
                                        "Enter here: ")
                        # if user chooses to return to menu
                        if confirm.lower() == "m":
                            delete = False
                            break

                        # if user chooses to delete book record
                        elif confirm.lower() == "y":
                            cursor.execute('''DELETE FROM bookstore WHERE id = ?''', (delete_book,))
                            db.commit()
                            print("\nBook deleted!")
                            delete = False
                            break

                    # if user enters an invalid option
                    else:
                        print("Invalid option entered")

            # book id has to be an integer
            except ValueError:
                print("Invalid id entered")

    # option for user to search book records
    elif menu.lower() == "s":
        while True:
            # prompt user for which field they would like to search with or to return to menu
            search_book = input("\nChoose an option to search:\n"
                                "Id - i\n"
                                "Title - t\n"
                                "Author - a\n"
                                "Return to menu - m\n"
                                "Enter here: ")
            # if user chooses to return to menu
            if search_book.lower() == "m":
                break

            # if user chooses to search via id
            elif search_book.lower() == "i":
                while True:
                    try:
                        # prompt user for id
                        search_id = input("\nEnter book id number: ")
                        search_result = cursor.execute('''SELECT * FROM bookstore WHERE id = ?''', (search_id,)).fetchone()
                        # check if id exists in books table
                        if search_result is None:
                            print("Invalid id entered")

                        else:
                            # print search result
                            print("\nThe book you searched for is:")
                            print(search_result)
                            break
                    except ValueError:
                        print("Invalid id entered")

            # if user chooses to search via title
            elif search_book.lower() == "t":
                # prompt for book title
                search_title = input("\nEnter book title: ")
                search_result = cursor.execute('''SELECT * FROM bookstore WHERE title = ?''', (search_title,)).fetchone()
                # check if title exists in books table
                if search_result is None:
                    print("Invalid title entered")

                else:
                    # print search result
                    print("\nThe book you searched for:")
                    print(search_result)
                    break

            # if user chooses to search via author
            elif search_book.lower() == "a":
                # prompt for author
                search_author = input("\nEnter the author you would like to search for: ")
                search_result = cursor.execute('''SELECT * FROM bookstore WHERE author = ?''', (search_author,)).fetchone()
                # check if author exists in books table
                if search_result is None:
                    print("Invalid author entered")

                else:
                    # print out result
                    print("\nThe stored books written by author: ")
                    print(search_result)
                    break
            else:
                print("Invalid option entered")

    # option to terminate program
    # closes the database
    elif menu.lower() == "e":
        db.close()
        print("Goodbye!!!")
        exit()
