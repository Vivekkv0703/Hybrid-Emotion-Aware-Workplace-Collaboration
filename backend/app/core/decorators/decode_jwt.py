from functools import wraps
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from ..utils.auth import decode_access_token


def require_auth(view_func):
    @wraps(view_func)
    def wrapper(self, request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return Response({"error": "Unauthorized"}, status=HTTP_401_UNAUTHORIZED)

        token = auth_header.split(" ")[1]
        user_id = decode_access_token(token)

        if not user_id:
            return Response(
                {"error": "Invalid or expired token"}, status=HTTP_401_UNAUTHORIZED
            )

        request.user_id = user_id
        return view_func(self, request, *args, **kwargs)

    return wrapper
