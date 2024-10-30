#!/usr/bin/python3

""" Script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    """ If the code is not being imported but run directly
        Arguments:
            mysql username: username to connect the mySQL database
            mysql password: password to connect the mySQL database
            database name: name of the database to connect 
    """

    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all the results
    query_rows = cursor.fetchall()
    
    # Print each row
    for row in query_rows:
        print(row)
    
    # Close the cursor
    cursor.close()
    # Close the database connection
    db.close()