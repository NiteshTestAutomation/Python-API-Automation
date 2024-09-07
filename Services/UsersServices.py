import requests
from Testdata import UsersTestdata
from Logs import log_file

class Users:

  log = log_file.generateLog()

  def verifyCreateUserRequest(self):
      flag = True
      r = requests.post('https://reqres.in/api/users',data=UsersTestdata.testdata)
      status = r.status_code
      assert r.status_code is 201
      self.log.info(f"Status code is {status}")
      self.log.info("Validated API Response Status code")
      # print(r.json())
      assert r.json()["name"]
      if status is not 201:
          self.log.error(f"Status code is showing {status} not 201")
          flag = False
      return flag

  def verifyGetAllUsersListRequest(self):
      flag = True
      r = requests.get('https://reqres.in/api/users?page=2')
      status = r.status_code
      assert r.status_code is 200
      self.log.info(f"Status code is {status}")
      self.log.info("Validated API Response Status code")
      # print(r.json())
      if status is not 200:
          self.log.error(f"Status code is showing {status} not 200")
          flag = False
      print(r.json()['page'])
      return flag

