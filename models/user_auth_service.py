from models.user import User

class UserAuthService:
  @staticmethod
  def create_token(user):
    return str(user.get_id()) + ':' + user.get_auth_token()