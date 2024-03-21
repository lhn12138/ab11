from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User


@api_view(['POST'])
def register(request):
    print(request.data)
    username = request.data.get('username')
    password = request.data.get('password')
    # 检查用户名是否已存在
    if User.objects.filter(username=username).exists():
        return Response({'error': '用户名已存在'}, status=status.HTTP_400_BAD_REQUEST)

    # 创建新用户
    user = User.objects.create(
        username=username,
        password=password
    )

    return Response({'message': '注册成功'}, status=status.HTTP_200_OK)



@api_view(['POST'])
def login(request):
    print(request.data)
    username = request.data.get('username')
    password = request.data.get('password')

    # 验证用户名和密码
    if User.objects.filter(username=username).filter(password=password).exists():
        # 用户名和密码验证通过
        return Response({'message': '登录成功'}, status=status.HTTP_200_OK)
    else:
        # 用户名或密码错误
        return Response({'error': '用户名或密码错误'}, status=status.HTTP_400_BAD_REQUEST)
