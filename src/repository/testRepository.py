from sqlalchemy import or_
from sqlalchemy.orm import Session

from domain import testSchema
from model import testModel

def create_test(db: Session, name: str, liked: bool):
    db_test = testModel.Test(name=name, liked=liked)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test
    
def update_test(db: Session, db_test: testSchema.Test, test: testSchema.TestUpdate):
    # passa o objeto para dicionário -> banco
    test_data = test.dict(exclude_unset=True)
    for key, value in test_data.items():
        setattr(db_test, key, value)

    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test
    
def get_test(db: Session, test_id: int):
    return db.query(testModel.Test).filter(testModel.Test.id == test_id).first()
    
def delete_test(db: Session, db_test: testSchema.Test):
    db.delete(db_test)
    db.commit()