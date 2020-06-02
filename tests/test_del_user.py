from ..Entities.User import User

def test_create_user():
    user = User()
    req = user.delete(2)

    assert req.status_code == 204
