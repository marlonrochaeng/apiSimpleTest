from ..Entities.Users import Users

def test_get_users():
    user = Users()
    req = user.get_users()
    assert req['code'] == 200
    assert req['json']['data'][0]['id'] is not '' and req['json']['data'][0]['id'] is not None

def test_get_user_resource():
    user = Users()
    req = user.get_users_resource()
    assert req['code'] == 200
    assert len(req['json']['data']) > 5
    assert req['json']['data'][0]['id'] is not '' and req['json']['data'][0]['id'] is not None

