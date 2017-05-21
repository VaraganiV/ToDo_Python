
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class ToDo(Base) : 
	__tablename__ = 'todo'

	task_id = Column(Integer, primary_key=True)
	task_desc = Column(String(250), nullable=False)


	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'task_desc': self.task_desc,
			'task_id' : self.task_id
		}


engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)