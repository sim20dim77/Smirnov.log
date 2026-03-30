from services.db import Db

class Article:
  __tablename__ = 'table1'
  id = None
  author_id = None
  name = None
  text = None
  created_at = None

  def findAll(cls):
    db = Db()
    return db.query("SELECT * FROM 'table1'", {}, cls)
    # items = db.query("SELECT * FROM 'table1'")
    # print(items)