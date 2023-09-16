#!/usr/bin/python3
""" a script that adds the State object “Louisiana” to the database
    `hbtn_0e_6_usa`.
    Your script should take 3 arguments: `mysql username`,
    `mysql password` and `database name`.
    You must use the module SQLAlchemy.
    You must import State and Base from model_state -
    `from model_state import Base, State`.
    Your script should connect to a MySQL server running on
    localhost at port 3306.
    Print the new states.id after creation
    Your code should not be executed when imported
"""
if __name__ == "__main__":
    import argparse
    from model_state import Base, State
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
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
