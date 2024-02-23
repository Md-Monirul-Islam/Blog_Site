from django.shortcuts import render
from blog_app.models import Blog
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])
def blog_list(request):
    if request.method == 'GET':
        all_blogs = Blog.objects.filter(is_public=True)
        serializer = BlogSerializer(all_blogs,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def blog_details(request,pk):
    blog = Blog.objects.get(is_public=True,pk=pk)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)