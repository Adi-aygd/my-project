import mysql.connector
import random
import tkinter as tk
from tkinter import ttk
from tabulate import tabulate
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ADISHMA",
    database="admin"
)

mycursor = mydb.cursor()


def add_record(cursor, connection, table_name):
    while True:
        choice = int(input("ENTER THE NUMBER FOR THE PASSENGER: "))
        flight_no = int(input("Enter Flight Number: "))
        airlines = input("Enter Airlines: ")
        origin = input("Enter Origin: ")
        destination = input("Enter Destination: ")
        departure_time = input("Enter Departure Time (YYYY-MM-DD): ")
        arrival_time = input("Enter Arrival Time (YYYY-MM-DD): ")
        fare = int(input("Enter Fare: "))
        
        insert_query = "INSERT INTO {} (CHOICE, FLIGHT_NO, AIRLINES, ORIGIN, DESTINATION, DEPARTURE_TIME, ARRIVAL_TIME, FARE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)".format(table_name)
        values = (choice, flight_no, airlines, origin, destination, departure_time, arrival_time, fare)

        try:
            mycursor.execute(insert_query, values)
            connection.commit()
            print("Record inserted successfully.")
        except Exception as e:
            print("Error:", e)
            connection.rollback()

        more_records = input("ENTER MORE RECORDS? (y/n): ")
        if more_records.lower() not in ["y", "yes"]:
            break

def update_record(cursor, connection, table_name):
    while True:
        choice = int(input("Enter the number from the table which must be updated: "))
        origin = input("Enter new origin: ")
        destination = input("Enter new destination: ")
        departure_time = input("Enter new departure time (YYYY-MM-DD): ")
        arrival_time = input("Enter new arrival time (YYYY-MM-DD): ")
        fare = int(input("Enter new fare: "))
        
        update_sql = "UPDATE {} SET ORIGIN = %s, DESTINATION = %s, DEPARTURE_TIME = %s, ARRIVAL_TIME = %s, FARE = %s WHERE CHOICE = %s".format(table_name)
        values = (origin, destination, departure_time, arrival_time, fare, choice)

        try:
            mycursor.execute(update_sql, values)
            connection.commit()
            print(mycursor.rowcount, "record(s) updated")
        except Exception as e:
            print("Error:", e)
            connection.rollback()

        more_updates = input("Do you want to add more updates? (y/n): ")
        if more_updates.lower() not in ["y", "yes"]:
            break

def delete_record(cursor, connection, table_name):
    cursor.execute("SELECT * FROM {}".format(table_name))
    result = cursor.fetchall()

    if not result:
        print("No records found.")
    else:
        column_names = [desc[0] for desc in cursor.description]
        table = [column_names] + result
        print(tabulate(table, headers="firstrow", tablefmt="grid"))

    while True:
        delete_choice = int(input("ENTER THE NUMBER FROM THE ABOVE TABLE TO DELETE THE RECORD: "))
        sql = "DELETE FROM {} WHERE CHOICE = %s".format(table_name)
        ch = (delete_choice,)

        cursor.execute(sql, ch)
        if cursor.rowcount > 0:
            connection.commit()
            print(cursor.rowcount, "record(s) deleted")
        else:
            print("No matching records found.")

        more_deletes = input("DELETE MORE RECORDS? (y/n): ")
        if more_deletes.lower() not in ["y", "yes"]:
            print("EXITING FROM DELETE RECORDS IN {}".format(table_name))
            break

def search_records(cursor, connection, table_name):
    while True:
        search_origin = input("Enter the place of origin: ")
        search_destination = input("Enter the place of destination: ")
        search_departure_time = input("Enter Departure Time (YYYY-MM-DD): ")
        sql = "SELECT * FROM {} WHERE ORIGIN = %s AND DESTINATION = %s AND DEPARTURE_TIME = %s".format(table_name)
        values = (search_origin, search_destination, search_departure_time)
        cursor.execute(sql, values)
        result = cursor.fetchall()
        if not result:
            print("No records found.")
        else:
            column_names = [desc[0] for desc in cursor.description]
            table = [column_names] + result
            print(tabulate(table, headers="firstrow", tablefmt="grid"))

        more_searches = input("Search for more records? (y/n): ")
        if more_searches.lower() not in ["y", "yes"]:
            print("EXITING FROM SEARCH RECORDS IN {}".format(table_name))
            break


tickets_label = None  # Define tickets_label here

def search_flights(table, origin, destination, departure_time):
    try:
        cursor = mydb.cursor()
        cursor.execute(f"SELECT * FROM {table} WHERE ORIGIN = %s AND DESTINATION = %s AND DEPARTURE_TIME = %s", (origin, destination, departure_time))
        result = cursor.fetchall()
        cursor.close()
        return result
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return []

def book_ticket(table, passenger_choice, passenger_data):
    try:
        cursor = mydb.cursor()
        cursor.execute(f"SELECT fare FROM {table} WHERE CHOICE = %s", (passenger_choice,))
        fare = cursor.fetchone()[0]
        cursor.close()
        
        total_fare = fare
        
        # Generate a ticket for the passenger
        random_number = random.randint(1, 40)
        alphabets = ['A', 'B', 'C']
        random_alphabet = random.choice(alphabets)
        
        passenger_name, nationality, email, phone_number, gender = passenger_data
        
        ticket = f"------------------------E-TICKET-----------------------------\n" \
                 f"|E-TICKET #                                                 |\n" \
                 f"|Name: {passenger_name}                                        |\n" \
                 f"|Nationality: {nationality}                                |\n" \
                 f"|Email: {email}                                       |\n" \
                 f"|Phone Number: {phone_number}                                |\n" \
                 f"|Gender: {gender}                                      |\n" \
                 f"|Flight Fare: Rs {total_fare}                             |\n" \
                 f"|Flight Choice: {passenger_choice}                      |\n" \
                 f"|SEAT NUMBER: {random_number}{random_alphabet}             |\n" \
                 f"-------------------------------------------------------------"
        
        return ticket
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return []

def search_button_clicked():
    origin = origin_entry.get()
    destination = destination_entry.get()
    departure_time = departure_time_entry.get()
    table = flight_type.get()

    result = search_flights(table, origin, destination, departure_time)
    
    cursor = mydb.cursor()
    cursor.execute(f"SHOW COLUMNS FROM {table}")  # Fetch column names
    column_names = [desc[0] for desc in cursor]
    cursor.close()
    
    # Display flight information in a table
    table = [column_names] + result
    flight_info_label.config(text=tabulate(table, headers="firstrow", tablefmt="grid"))

def book_button_clicked():
    passenger_choice = passenger_choice_entry.get()
    passenger_name = name_entry.get()
    nationality = nationality_entry.get()
    email = email_entry.get()
    phone_number = phone_entry.get()
    gender = gender_entry.get()

    table = flight_type.get()
    
    ticket = book_ticket(table, passenger_choice, (passenger_name, nationality, email, phone_number, gender))
    
    # Display the ticket directly
    tickets_label.config(text=ticket)
    add_passenger_button.grid(row=8, column=1, pady=5)  # Show the "Add Passenger" button
    terminate_button.grid(row=9, column=1)  # Show the "No" button
    book_button.grid_forget()  # Hide the "Book" button

def add_passenger():
    # Clear flight and passenger info for the next passenger
    flight_info_label.config(text="")
    passenger_choice_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    nationality_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    phone_entry.delete(0, 'end')
    gender_entry.delete(0, 'end')
    tickets_label.config(text="")  # Clear the e-ticket label
    passenger_choice_entry.focus()
    add_passenger_button.grid_forget()  # Hide the "Add Passenger" button
    terminate_button.grid_forget()  # Hide the "No" button
    book_button.grid(row=6, column=1)  # Show the "Book" button

def terminate_program():
    root.quit()

# Main menu
while True:
    print("------------WELCOME TO FLIGHT MANAGEMENT SYSTEM-------")
    print("           MAIN MENU")
    print("1. ADMIN")
    print("2. PASSENGER")
    print("3. EXIT")
    choice = int(input("ENTER THE NUMBER FROM THE FOLLOWING MENU: "))

    if choice == 1:
        while True:
            print("1. ADD RECORDS")
            print("2. UPDATE RECORDS")
            print("3. DELETE RECORDS")
            print("4. SEARCH RECORDS")
            print("5. EXIT")
            admin_choice1 = int(input("PLEASE ENTER THE NUMBER TO OPERATE FOLLOWING MENU: "))

            if admin_choice1 == 1:
                print("1. ADD RECORDS FOR IN LIST OF FLIGHT")
                print("2. ADD RECORDS IN TOUR PACKAGE")
                print("3. EXIT")
                admin_add = int(input("PLEASE ENTER THE NUMBER: "))

                if admin_add == 1:
                    add_record(mycursor, mydb, "domestic")
                elif admin_add == 2:
                    add_record(mycursor, mydb, "tour")
                elif admin_add == 3:
                    print("EXITING FROM THE ADD RECORDS IN THE LIST")
                    break
                else:
                    print("PLEASE PROVIDE A PROPER NUMBER TO EXECUTE")

            elif admin_choice1 == 2:
                print("1. UPDATE RECORDS FOR IN LIST OF FLIGHT")
                print("2. UPDATE RECORDS IN TOUR PACKAGE")
                print("3. EXIT")
                admin_update = int(input("PLEASE ENTER THE NUMBER: "))

                if admin_update == 1:
                    update_record(mycursor, mydb, "domestic")
                elif admin_update == 2:
                    update_record(mycursor, mydb, "tour")
                elif admin_update == 3:
                    print("EXITING FROM THE UPDATE RECORDS")
                    break
                else:
                    print("PLEASE PROVIDE A PROPER NUMBER TO EXECUTE")

            elif admin_choice1 == 3:
                print("1. DELETE RECORDS FOR IN LIST OF FLIGHT")
                print("2. DELETE RECORDS IN TOUR PACKAGE")
                print("3. EXIT")
                admin_delete = int(input("ENTER THE NUMBER FROM THE ABOVE MENU: "))

                if admin_delete == 1:
                    delete_record(mycursor, mydb, "domestic")
                elif admin_delete == 2:
                    delete_record(mycursor, mydb, "tour")
                elif admin_delete == 3:
                    print("EXITING FROM DELETE RECORDS IN THE LIST")
                    break
                else:
                    print("PLEASE PROVIDE A PROPER NUMBER TO EXECUTE")
            elif admin_choice1 == 4:
                print("1. SEARCH RECORDS FOR IN LIST OF FLIGHT")
                print("2. SEARCH RECORDS IN TOUR PACKAGE")
                print("3. EXIT")
                admin_search = int(input("ENTER THE NUMBER FROM THE ABOVE MENU: "))

                if admin_search == 1:
                    search_records(mycursor, mydb, "domestic")
                elif admin_search == 2:
                    search_records(mycursor, mydb, "tour")
                elif admin_search == 3:
                    print("EXITING FROM SEARCH RECORDS IN THE LIST")
                    break
                else:
                    print("PLEASE PROVIDE A PROPER NUMBER TO EXECUTE")
            elif admin_choice1==5:
                break

    elif choice == 2:
        root = tk.Tk()
        root.title("Passenger Module")

# Flight Search Section
        search_frame = ttk.LabelFrame(root, text="Search Flights")
        search_frame.grid(row=0, column=0, padx=10, pady=10)

        origin_label = ttk.Label(search_frame, text="Origin:")
        destination_label = ttk.Label(search_frame, text="Destination:")
        departure_time_label = ttk.Label(search_frame, text="Departure Time (YYYY-MM-DD):")
        flight_type_label = ttk.Label(search_frame, text="Flight Type:")

        origin_entry = ttk.Entry(search_frame)
        destination_entry = ttk.Entry(search_frame)
        departure_time_entry = ttk.Entry(search_frame)
        flight_type = tk.StringVar(value="domestic")
        flight_type_combobox = ttk.Combobox(search_frame, textvariable=flight_type, values=["domestic", "tour"])

        search_button = ttk.Button(search_frame, text="Search", command=search_button_clicked)

        origin_label.grid(row=0, column=0)
        destination_label.grid(row=1, column=0)
        departure_time_label.grid(row=2, column=0)
        flight_type_label.grid(row=3, column=0)

        origin_entry.grid(row=0, column=1)
        destination_entry.grid(row=1, column=1)
        departure_time_entry.grid(row=2, column=1)
        flight_type_combobox.grid(row=3, column=1)

        search_button.grid(row=4, column=1)

        flight_info_label = ttk.Label(search_frame, text="", wraplength=500)
        flight_info_label.grid(row=5, columnspan=2)

# Booking Section
        booking_frame = ttk.LabelFrame(root, text="Book Ticket")
        booking_frame.grid(row=1, column=0, padx=10, pady=10)

        passenger_choice_label = ttk.Label(booking_frame, text="Flight Choice:")
        name_label = ttk.Label(booking_frame, text="Passenger Name:")
        nationality_label = ttk.Label(booking_frame, text="Nationality:")
        email_label = ttk.Label(booking_frame, text="Email:")
        phone_label = ttk.Label(booking_frame, text="Phone Number:")
        gender_label = ttk.Label(booking_frame, text="Gender:")

        passenger_choice_entry = ttk.Entry(booking_frame)
        name_entry = ttk.Entry(booking_frame)
        nationality_entry = ttk.Entry(booking_frame)
        email_entry = ttk.Entry(booking_frame)
        phone_entry = ttk.Entry(booking_frame)
        gender_entry = ttk.Entry(booking_frame)

        passenger_choice_label.grid(row=0, column=0)
        name_label.grid(row=1, column=0)
        nationality_label.grid(row=2, column=0)
        email_label.grid(row=3, column=0)
        phone_label.grid(row=4, column=0)
        gender_label.grid(row=5, column=0)

        passenger_choice_entry.grid(row=0, column=1)
        name_entry.grid(row=1, column=1)
        nationality_entry.grid(row=2, column=1)
        email_entry.grid(row=3, column=1)
        phone_entry.grid(row=4, column=1)
        gender_entry.grid(row=5, column=1)

        book_button = ttk.Button(booking_frame, text="Book", command=book_button_clicked)
        add_passenger_button = ttk.Button(booking_frame, text="Add Passenger", command=add_passenger)
        terminate_button = ttk.Button(booking_frame, text="No", command=terminate_program)

        book_button.grid(row=6, column=1)
        tickets_label = ttk.Label(booking_frame, text="", wraplength=500)
        tickets_label.grid(row=7, columnspan=2)

        root.mainloop()

    elif choice == 3:
        print("EXITING FROM THE SYSTEM")
        break

mydb.close()
