#!/usr/bin/python3
"""a script that lists all states from the database `hbtn_0e_0_usa`
    Your script should take 3 arguments: mysql username, mysql password and
    database name (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost
    at port 3306
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported
"""

if __name__ == "__main__":
    import MySQLdb
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("mysql_username", type=str, help="MySQL username")
    parser.add_argument("mysql_password", type=str, help="MySQL password")
    parser.add_argument("database", type=str, help="database name")

    args = parser.parse_args()
    username= args.mysql_username
    password = args.mysql_password
    database = args.database

    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            port=3306,
            db=database
            )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
