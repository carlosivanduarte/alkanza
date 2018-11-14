from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Result
from .serializers import ResponseSerializer, PlacesSerializer


@api_view(['GET', 'POST'])
def results_list(request, format=None):
    if request.method == 'GET':
        results = Result.objects.all()
        serializer = ResponseSerializer(results, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = PlacesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)