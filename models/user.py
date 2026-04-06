from models.active_record_entity import ActiveRecordEntity

class User(ActiveRecordEntity):
  # __tablename__ = 'table1'
  _nickname = None
  _email = None
  _is_confirmed = None
  _created_at = None
  _role = None
  _password_hash = None
  _auth_token = None

  def get_nickname(self):
    return self._nickname
  def get_email(self):
    return self._email
  def get_created_at(self):
    return self._created_at
  def get_role(self):
    return self._role
  def get_password_hash(self):
    return self._password_hash
  def get_auth_token(self):
    return self._auth_token
  
  def set_nickname(self, nickname):
    self._nickname = nickname
  def set_email(self, email):
    self._email = email
  def set_role(self, role):
    self._role = role
  # def set_created_at(self, created_at):
  #   self._created_at = created_at

  @staticmethod
  def get_table_name():
    return 'users'