# your_app/utils.py
from rest_framework_jwt.settings import api_settings

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'name':user.first_name,
        'surname':user.last_name,
        'username':user.username,
        'api_token': token,
        # Các thông tin khác mà bạn muốn bao gồm trong payload
    }