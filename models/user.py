import re
import hashlib
import random
from models.active_record_entity import ActiveRecordEntity
from exceptions import InvalidArgumentException
from email_validator import validate_email, EmailNotValidError
from werkzeug.security import generate_password_hash, check_password_hash

class User(ActiveRecordEntity):
  # __tablename__ = 'table1'
  _nickname = None
  _email = None
  _is_confirmed = None
  _created_at = None
  _role = None
  _password_hash = None
  _auth_token = None
  _created_at = None

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
  def get_is_confirmed(self):
        return self._is_confirmed

  def set_nickname(self, nickname):
    self._nickname = nickname
  def set_email(self, email):
    self._email = email
  def set_role(self, role):
    self._role = role
  def set_created_at(self,created_at):
    self._created_at = created_at
  # def set_created_at(self, created_at):
  #   self._created_at = created_at
  def refresh_auth_token(self):
    self._auth_token = hashlib.sha1(random.randbytes(100)).hexdigest() + hashlib.sha1(random.randbytes(100)).hexdigest()

  @staticmethod
  def sign_up(user_data):
    print(user_data)
    if not user_data['nickname']:
      raise InvalidArgumentException('Не передан логин')
    
    if re.search(r'^[a-zA-Z0-9]+$', user_data['nickname']) is None:
      raise InvalidArgumentException('Логин может состоять только из символов латиницы и цифр')
    
    if __class__.find_one_by_column('nickname', user_data['nickname']):
      raise InvalidArgumentException('Логин уже существует')
    if __class__.find_one_by_column('email', user_data['email']):
      raise InvalidArgumentException('Email уже существует')

    if not user_data['email']:
      raise InvalidArgumentException('Не передан email')
    
    try:
      validate_email(user_data['email'])
    except EmailNotValidError as e:
      raise InvalidArgumentException('email некорректен')


    if not user_data['password']:
            raise InvalidArgumentException('Dont transpert "password"')
    if len(user_data['password']) < 8:
      raise InvalidArgumentException('Пароль должен быть не менее восьми символов.')

    user = User()
    user._nickname = user_data['nickname']
    user._email = user_data['email']
    user._is_confirmed = True
    user._role = 'User'
    user._password_hash = generate_password_hash(user_data['password'])
    user.refresh_auth_token()
    user.save()
    return user
  
  @staticmethod
  def sign_in(user_data):
    print(user_data)
    if not user_data['nickname']:
      raise InvalidArgumentException('Не передан логин')
    if not user_data['password']:
      raise InvalidArgumentException('Не передан пароль')
    
    user = User.find_one_by_column('nickname', user_data['nickname'])
    
    if user is None:
      raise InvalidArgumentException('Неверный логин или пароль')
    
    if check_password_hash(user_data['password'], user.get_password_hash):
      raise InvalidArgumentException('Неверный логин или пароль')

    user.refresh_auth_token()
    user.save()
    return user
    
    
  @staticmethod
  def get_table_name():
    return 'users'