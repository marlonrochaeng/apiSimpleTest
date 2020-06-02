from ..Entities.Register import Register
import os
import json

def test_register_user():

    f = open(os.path.abspath(os.getcwd()) + '/data/success_reg.json')
    request_json = json.loads(f.read())

    register = Register()
    req = register.register(request_json)

    assert req['code'] == 200
    assert req['json']['id'] == 4
    assert req['json']['token'] == 'QpwL5tke4Pnpja7X4'


def test_unsuccessfull_register_user():

    f = open(os.path.abspath(os.getcwd()) + '/data/unsuccess_reg.json')
    request_json = json.loads(f.read())

    register = Register()
    req = register.register(request_json)

    assert req['code'] == 400
    assert req['json']['error'] == 'Missing password'