#!/usr/bin/python3
""" a script that lists all `states` with a `name` starting with `N`
    (upper N) from the database `hbtn_0e_0_usa`.
    Your script should take 3 arguments: mysql username, mysql password
    and database name (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost
    at port 3306
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported
"""
if __name__ == "__main__":
    import MySQLdb

    db = MySQLdb.connect(
            host="localhost",
            user="root",
            port=3306,
            passwd="root",
            db="hbtn_0e_0_usa"
            )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
