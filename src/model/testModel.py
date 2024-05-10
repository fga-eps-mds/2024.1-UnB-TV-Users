from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Test(Base):
  __tablename__ = "test"
  __table_args__ = {'extend_existing': True}

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  liked = Column(Boolean, default=False)