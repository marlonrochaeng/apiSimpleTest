from ..Entities.User import User
import json
import os

def test_create_user():
    f = open(os.path.abspath(os.getcwd()) + '/data/new_user.json')
    request_json = json.loads(f.read())

    user = User()
    req = user.create(request_json)


    assert req['code'] == 201
    assert req['json']['name'] == 'morpheus'
    assert req['json']['job'] == 'leader'

def test_post_user():
    f = open(os.path.abspath(os.getcwd()) + '/data/edit_full_user.json')
    request_json = json.loads(f.read())

    user = User()
    req = user.update_full(2, request_json)

    assert req['code'] == 200
    assert req['json']['name'] == 'morpheus'
    assert req['json']['job'] == 'zion resident'
    assert req['json']['updatedAt'] is not None

def test_patch_user():
    f = open(os.path.abspath(os.getcwd()) + '/data/edit_full_user.json')
    request_json = json.loads(f.read())

    user = User()
    req = user.update_patch(2, request_json)

    assert req['code'] == 200
    assert req['json']['name'] == 'morpheus'
    assert req['json']['job'] == 'zion resident'
    assert req['json']['updatedAt'] is not None