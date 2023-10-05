from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_jwt.views import APIView
from .serializers import CustomUserSerializer
from .custom.custom_response import jwt_response_payload_handler
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from api_auth.models import CustomUser

def generatorJWT(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token

def decodeJWT(JWTToken):
    jwt_payload_get_username_handler = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER
    jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
    username = ""
    is_token_expired = False
    try:
        payload = jwt_decode_handler(JWTToken)
        expiration_timestamp = payload['exp']
        username = jwt_payload_get_username_handler(payload)
        current_timestamp = datetime.utcnow().timestamp()
        is_token_expired = (current_timestamp > expiration_timestamp)
    except Exception as e:
        is_token_expired = True 
    return username,is_token_expired

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Xác thực thành công, đăng nhập người dùng
            #sinh token
            token = generatorJWT(user)
            print(token)
            response_data = jwt_response_payload_handler(token,user,request)
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            # Xác thực thất bại
            return Response({'message': 'Tên đăng nhập hoặc mật khẩu không đúng'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def register(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            # Sử dụng jwt_response_payload_handler để tạo response
            token = generatorJWT(user)
            response_data = jwt_response_payload_handler(token, user, request)
            
            return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyTokenView(APIView):
    def post(self, request):
        token = request.data.get('api_token')
        username, is_token_expired = decodeJWT(token)
        if is_token_expired:
            return Response({'message': 'Lỗi xác thực'}, status=status.HTTP_401_UNAUTHORIZED)
        user = CustomUser.objects.get(username=username)
        response_data = jwt_response_payload_handler(token, user, request)
        return Response(response_data, status=status.HTTP_200_OK)