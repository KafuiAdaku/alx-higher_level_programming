#!/usr/bin/python3
""" a script that lists all `State` objects, and corresponding `City`
    objects, contained in the database `hbtn_0e_101_usa`.
    Your script should take 3 arguments: `mysql username`,
    `mysql password` and `database name`.
    You must use the module SQLAlchemy.
    Your script should connect to a MySQL server running on
    localhost at port 3306.
    You must only use one query to the database.
    You must use the cities relationship for all State objects
    Results must be sorted in ascending order by states.id and cities.id
    Your code should not be executed when imported.
"""
if __name__ == "__main__":
    import argparse
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine, asc
    from sqlalchemy.orm import sessionmaker

    parser = argparse.ArgumentParser()
    parser.add_argument("mysql_username", type=str, help="MySQL username")
    parser.add_argument("mysql_password", type=str, help="MySQL password")
    parser.add_argument("database", type=str, help="database name")

    args = parser.parse_args()
    username = args.mysql_username
    password = args.mysql_password
    database = args.database

    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:\
            3306/{database}")

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(asc(State.id)).all()

    for state in result:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    session.close()
