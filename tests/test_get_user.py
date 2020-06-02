from ..Entities.User import User

def test_get_user():
    user = User()
    req = user.get_user(2)
    assert req['code'] == 200
    assert req['json']['data']['email'] == 'janet.weaver@reqres.in'
    assert req['json']['data']['first_name'] == 'Janet'
    assert req['json']['data']['last_name'] == 'Weaver'

def test_get_invalid_user():
    user = User()
    req = user.get_user(23)
    assert req['code'] == 404
    assert req['json'] == {}

def test_get_resource():
    user = User()
    req = user.get_users_resource(2)
    assert req['code'] == 200
    assert req['json']['data']['id'] == 2
    assert req['json']['data']['name'] == 'fuchsia rose'
    assert req['json']['data']['year'] == 2001

def test_get_invalid_resource():
    user = User()
    req = user.get_users_resource(23)
    assert req['code'] == 404
    assert req['json'] == {}
