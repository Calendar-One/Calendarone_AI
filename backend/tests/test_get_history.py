# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm.attributes import get_history

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

with Session(engine) as session:
    user1 = User(name='Alice')
    session.add(user1)

    session.flush() # Flush to make 'Alice' the 'unchanged' value
    user1.name = 'Bob' # Modify the attribute

    history = get_history(user1, 'name')
    print(f"Added: {history.added}")
    print(f"Unchanged: {history.unchanged}")
    print(f"Deleted: {history.deleted}")

    if history.has_changes():
        old_val = history.deleted[0] if history.deleted else None
        new_val = history.added[0] if history.added else getattr(user1, 'name')
        print(f"Old value: {old_val}")
        print(f"New value: {new_val}")

    session.commit()


    user1 = session.query(User).filter(User.name == 'Bob').first()
    session.delete(user1)
    session.flush()
    
    history = get_history(user1, 'name')
    print(f"Added: {history.added}")
    print(f"Unchanged: {history.unchanged}")
    print(f"Deleted: {history.deleted}")

    if history.has_changes():
        old_val = history.deleted[0] if history.deleted else None
        new_val = history.added[0] if history.added else getattr(user1, 'name')
        print(f"Old value: {old_val}")
        print(f"New value: {new_val}")



