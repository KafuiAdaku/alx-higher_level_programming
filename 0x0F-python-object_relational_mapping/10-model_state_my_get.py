#!/usr/bin/python3
"""a script that prints the State object with the
    name passed as argument from the database `hbtn_0e_6_usa`.
    Your script should take 4 arguments: `mysql username`, `mysql password`,
    `database name` and `state name to search` (SQL injection free).
    You must use the module SQLAlchemy.
    You must import State and Base from model_state -
    `from model_state import Base, State`.
    Your script should connect to a MySQL server running on
    localhost at port 3306.
    You can assume you have one record with the state name to search.
    Results must display the states.id.
    If no state has the name you searched for, display `Not found`
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
    parser.add_argument("state_name", type=str, help="state name to search")

    args = parser.parse_args()
    username = args.mysql_username
    password = args.mysql_password
    database = args.database
    state_name = args.state_name

    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:\
            3306/{database}")
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter_by(name=state_name).\
        order_by(asc(State.id)).first()

    if states:
        print(f"{states.id}")
    else:
        print("Not found")

    session.close()
