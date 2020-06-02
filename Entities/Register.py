import json
import requests

class Register:
    def __init__(self):
        self.base_uri = "https://reqres.in"
        self.reg_uri = "/api/register"      

    def register(self, user):
        request = requests.post(self.base_uri + self.reg_uri, data=user)
        return {'code':request.status_code, 'json':request.json()}