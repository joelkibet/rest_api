from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post

# Create your views here.
class Live_view(APIView):
    def get(self, request, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

#def App_View(request):
#    data = {
#        "first": "Kelvin",
#        "last": "Doe",
#        "age": 30
#    }
##   return JsonResponse(data)
