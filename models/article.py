from models.active_record_entity import ActiveRecordEntity

class Article(ActiveRecordEntity):
  __tablename__ = 'table1'
  id = None
  author_id = None
  name = None
  text = None
  created_at = None


  @staticmethod
  def get_table_name():
    return 'table1'