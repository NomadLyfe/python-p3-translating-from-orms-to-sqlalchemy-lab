from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog)

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).all()[0]

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).all()[0]

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).all()[0]

def update_breed(session, dog, breed):
    session.query(Dog).filter(Dog.id == dog.id).update({Dog.breed: breed})