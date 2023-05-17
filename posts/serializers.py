from rest_framework import serializers, status
from rest_framework.response import Response
from posts.models import Post


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

def calculate(request):
    # 1. 데이터 확인
    num1 = request.GET.get("num1", 0)
    num2 = request.GET.get("num2", 0)
    operators = request.GET.get("operators")
    
    # 2. 계산
    if operators == "+":
        result = int(num1) + int(num2)
    elif operators == "-":
        result = int(num1) - int(num2)
    elif operators == "*":
        result = int(num1) * int(num2)
    elif operators == "/":
        result = int(num1) / int(num2)
    else:
        result = 0
    
    data  = {
        "type": "FBV",
        "result": result
    }

    # 3. 응답
    return Response(data=data, status=status.HTTP_200_OK)

