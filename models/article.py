from services.db import Db

class Article:
  __tablename__ = 'table1'
  id = None
  author_id = None
  name = None
  text = None
  created_at = None

  def find_all(cls):
    db = Db()
    return db.query("SELECT * FROM 'table1'", {}, cls)
    # items = db.query("SELECT * FROM 'table1'")
    # print(items)

  def get_by_id(id, cls):
    db = Db()
    return db.query(f"SELECT * FROM 'table1' WHERE id = {id}", {}, cls)[0]