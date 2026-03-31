from services.db import Db
from abc import ABCMeta, abstractmethod

class ActiveRecordEntity(metaclass = ABCMeta):
  @classmethod
  def find_all(cls):
    db = Db()
    table_name = cls.get_table_name()
    return db.query(f"SELECT * FROM `{table_name}`", {}, cls)
    # items = db.query("SELECT * FROM 'table1'")
    # print(items)

  @classmethod
  def get_by_id(cls, id):
    db = Db()
    table_name = cls.get_table_name()
    return db.query(f"SELECT * FROM `{table_name}` WHERE id = {id}", {}, cls)[0]
  
  @classmethod
  @abstractmethod
  def get_table_name():
    pass