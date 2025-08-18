import cloudinary.uploader
from functools import wraps


def handle_logo_upload(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        logo_file = request.FILES.get("logo")
        if logo_file:
            upload_result = cloudinary.uploader.upload(logo_file)
            request.data._mutable = True
            request.data["logo_url"] = upload_result.get("secure_url")
            del request.data["logo"]
            request.data._mutable = False
        return func(self, request, *args, **kwargs)

    return wrapper
