#!/usr/bin/python3

"""
Displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

Usage:
    ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        post=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    query = ("SELECT * FROM states WHERE name"
             " LIKE '{}' ORDER "
             "BY id ASC;".format(sys.argv[4]))
    cursor.execute(query)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()