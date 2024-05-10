from fastapi import APIRouter, HTTPException, Response, status, Depends, Header
from database import get_db
from sqlalchemy.orm import Session

from constants import errorMessages
from domain import testSchema
from repository import testRepository
from utils import security, enumeration

from starlette.responses import JSONResponse

from fastapi_filter import FilterDepends

test = APIRouter(
  prefix="/test"
)

@test.post('/create')
async def create_test(data: testSchema.Test, db: Session = Depends(get_db)):
    testRepository.create_test(db, name=data.name, liked=data.liked)

    return JSONResponse(status_code=201, content={"status": "sucesso"})
    
@test.get('/{test_id}', response_model=testSchema.Test)
async def get_test(test_id: int, db: Session = Depends(get_db)):
    test = testRepository.get_test(db, test_id)

    if not test:
        raise HTTPException(status_code=404, detail="TEST NAO EXISTENTE")

    return test

@test.patch("/{test_id}", response_model=testSchema.Test)
async def update_test(test_id: int, data: testSchema.TestUpdate, db: Session = Depends(get_db)):
    db_test = testRepository.get_test(db, test_id)

    if not db_test:
        raise HTTPException(status_code=404, detail="TEST NAO EXISTENTE")
    
    updated_test = testRepository.update_test(db, db_test, data)

    return updated_test

@test.delete("/{test_id}", response_model=testSchema.Test)
async def delete_test(test_id: int, db: Session = Depends(get_db)):
    db_test = testRepository.get_test(db, test_id)

    if not db_test:
        raise HTTPException(status_code=404, detail="TEST NAO EXISTENTE")
    
    testRepository.delete_test(db, db_test)

    return db_test