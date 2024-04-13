#!/usr/bin/python3
"""
This script lists all state with
where 'name' equals your fourth argument (argv[4])
in ascending order by 'states.id'
from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database for the states
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
