# import mysql connector
import mysql.connector

# function to create a connection
def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "iotdb"
    )

def update_employee(empid,salary):
    # get connection
    conn = get_connection()

    # form a query
    query = f"update employee SET salary = %s where empid = %s;"
    val = (salary, empid)

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()



update_employee(103, "250000")

