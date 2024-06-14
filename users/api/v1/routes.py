from django.contrib.auth import authenticate
from django.http import JsonResponse
from ninja import Router

from users.api.v1.schemas import SuccessLoginUser, BadLoginUser

router = Router()


@router.post('login/', response={200: SuccessLoginUser, 401: BadLoginUser})
def login_user(request, username: str, password: str):
    """Функция аутентификации и авторизации пользователя."""
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return JsonResponse({'msg': 'Вы успешно авторизовались.', 'token': user.auth_token}, status=200)
    return JsonResponse({'msg': 'Неправильно введено имя пользователя или пароль.'}, status=401)
