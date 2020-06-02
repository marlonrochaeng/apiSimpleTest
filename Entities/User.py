import json
import requests

class User:
    def __init__(self):
        self.base_uri = "https://reqres.in"
        self.user_uri = "/api/users/"
        self.user_resource = "/api/unknown/"
        self.create_uri = "/api/users"
        

    def get_user(self, _id):
        _id = str(_id)# if not isinstance(_id, str)
        request = requests.get(self.base_uri + self.user_uri + _id)
        return {'code':request.status_code, 'json':request.json()}

    def get_users_resource(self, _id):
        _id = str(_id)# if not isinstance(_id, str)
        request = requests.get(self.base_uri + self.user_resource + _id)
        return {'code':request.status_code, 'json':request.json()}
    
    def create(self, user):
        request = requests.post(self.base_uri + self.create_uri, data=user)
        return {'code':request.status_code, 'json':request.json()}
    
    def update_full(self, _id, user):
        _id = str(_id)
        request = requests.put(self.base_uri + self.create_uri + '/' +  _id, data=user)
        return {'code':request.status_code, 'json':request.json()}
    
    def update_patch(self, _id, user):
        _id = str(_id)
        request = requests.patch(self.base_uri + self.create_uri + '/' +  _id, data=user)
        return {'code':request.status_code, 'json':request.json()}

    def delete(self, _id):
        _id = str(_id)
        return requests.delete(self.base_uri + self.create_uri + '/' +  _id)
        #return {'code':request.status_code, 'json':request.json()}