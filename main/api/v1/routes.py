from ninja import Router

from users.api.v1.bearers import AuthTokenBearer

router = Router()


# @router.post('create_record/', auth=AuthTokenBearer())
# def create_record(request, body: RecordBodySchema):
#     pass
