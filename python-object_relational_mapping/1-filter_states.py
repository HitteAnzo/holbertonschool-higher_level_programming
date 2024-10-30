#!/usr/bin/python3

"""
Lists all states from the database hbtn_0e_0_usa whose names start with 'N'.

This script connects to a MySQL database using credentials provided as command-line arguments
and retrieves all states from the 'states' table where the name starts with 'N', ordered by their ID.

Usage:
    ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    db.close()
