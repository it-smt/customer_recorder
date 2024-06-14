from ninja import Schema


class SuccessLoginUser(Schema):
    msg: str
    token: str


class BadLoginUser(Schema):
    msg: str
