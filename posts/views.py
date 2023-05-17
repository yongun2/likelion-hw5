from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.serializers import PostListModelSerializer, PostModelSerializer


class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer

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