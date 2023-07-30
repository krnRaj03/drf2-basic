from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer
# Create your views here.

class MovieList(APIView):
    def get(self, request):
        movie=Movie.objects.all()
        serializer=MovieSerializer(movie, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(  serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetail(APIView):
    def get(self,request,pk):
        try:
           movie=Movie.objects.get(pk=pk)
        except movie.DoesNotExist():
           return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
        
        
    def put(self,request,pk):
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(  serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
