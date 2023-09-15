#!/usr/bin/python3
""" a script that lists all cities from the database hbtn_0e_4_usa.
    Your script should take 3 arguments: mysql username, mysql password
    and database name
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost
    at port 3306
    Results must be sorted in ascending order by cities.id
    You can use only execute() once
    Results must be displayed as they are in the example below
    Your code should not be executed when imported
"""
if __name__ == "__main__":
    import MySQLdb
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("mysql_username", type=str, help="MySQL username")
    parser.add_argument("mysql_password", type=str, help="MySQL password")
    parser.add_argument("database", type=str, help="databse name")
    parser.add_argument("statename", type=str, help="state name")

    args = parser.parse_args()
    username = args.mysql_username
    password = args.mysql_password
    database = args.database
    state_name = args.statename

    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database
            )
    query = "SELECT cities.name\
            FROM cities\
            INNER JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC"
    cursor = db.cursor()
    cursor.execute(query, (state_name,))

    result = cursor.fetchall()
    # my_list = []
    # for row in result:
        # my_list.append(row[0].strip("()"))
    # print(my_list)

    my_list = [row[0].strip("()") for row in result]

    for index in range(len(my_list)):
        if index != 0:
            print(", ", end="")
        print(my_list[index], end="")
    print()

    cursor.close()
    db.close()
