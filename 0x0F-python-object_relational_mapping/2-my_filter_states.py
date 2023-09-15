#!/usr/bin/python3
""" a script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
    Your script should take 4 arguments: mysql username, mysql password,
    database name and state name searched (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost at
    port 3306
    You must use format to create the SQL query with the user input
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
    parser.add_argument("database_name", type=str, help="database name")
    parser.add_argument("state_name", type=str, help="state to be searched")

    args = parser.parse_args()
    username = args.mysql_username
    password = args.mysql_password
    database = args.database_name
    state_search = args.state_name

    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            port=3306,
            db=database
            )
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor = db.cursor()
    cursor.execute(query, (state_search,))
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
