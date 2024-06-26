#!/usr/bin/python3
"""
This script lists all state with
where 'name' equals your fourth argument (argv[4])
in ascending order by 'states.id'
from the database hbtn_0e_0_usa
This filter is safe from SQL injections
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

    # db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
    #         ORDER BY states.id ASC".format(argv[4]))

    db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s \
            ORDER BY states.id ASC", {'name': argv[4]})

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
