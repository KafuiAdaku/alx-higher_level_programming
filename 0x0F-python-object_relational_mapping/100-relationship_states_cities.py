#!/usr/bin/python3
""" a script that creates the State “California” with the City
    “San Francisco” from the database `hbtn_0e_100_usa`.
    Your script should take 3 arguments: `mysql username`,
    `mysql password` and `database name`.
    You must use the module SQLAlchemy.
    Your script should connect to a MySQL server running on
    localhost at port 3306.
    You must use the cities relationship for all State objects.
    Your code should not be executed when imported.
"""
if __name__ == "__main__":
    import argparse
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine, asc, desc
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
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="SanFrancisco")
    new_city.state = new_state

    session.add(new_state)
    session.add(new_city)
    session.commit()

    session.close()
