import jwt;

def accept_request():
    decode = jwt.decode(token,"password", verify=false)
