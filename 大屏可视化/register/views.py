from rest_framework.views import APIView
from rest_framework.response import Response


class HelloView(APIView):
    def get(self, request, *args, **kwargs):
        print("hello")
        print(request.query_params)
        return Response({"status": True, 'message': '发送成功'})

