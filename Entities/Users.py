import json
import requests

class Users:
    def __init__(self):
        self.base_uri = "https://reqres.in"
        self.list_users = "/api/users?page=2"
        self.list_resource = "/api/unknown"

    def get_users(self):
        request = requests.get(self.base_uri + self.list_users)
        return {'code':request.status_code, 'json':request.json()}

    def get_users_resource(self):
        request = requests.get(self.base_uri + self.list_resource)
        return {'code':request.status_code, 'json': request.json()}