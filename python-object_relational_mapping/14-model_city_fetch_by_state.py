#!/usr/bin/python3
'''a Python file similar to model_state.py named model_city.py
that contains the class definition of a City'''


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    states = session.query(State, City) \
        .filter(State.id == City.state_id).order_by(City.id).all()

    for state in states:
        print("{}: ({}) {}".format(
            state[0].__dict__['name'],
            state[1].__dict__['id'],
            state[1].__dict__['name']))

    session.close()
