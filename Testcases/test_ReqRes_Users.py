import requests
from Services.UsersServices import Users


class TestUser(Users):

  def test_createUser_api_reqest(self):
      flag = self.verifyCreateUserRequest()
      assert flag is True

  def test_getAllUser_api_request(self):
      flag = self.verifyGetAllUsersListRequest()
      assert flag is True

