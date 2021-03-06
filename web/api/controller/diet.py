from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.model.diet import Diet
from api.serializer.diet import DietSerializer, DietReadSerializer


@api_view(['GET', 'POST'])
def diets(req):
    """
    Get all diets, or create a new one
    """
    if req.method == 'GET':
        diets = Diet.objects.all()
        serializer = DietReadSerializer(diets, many=True)
        return Response(serializer.data)

    elif req.method == 'POST':
        serializer = DietSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def myDiets(req):
    user = User.objects.get(id=req.user.id)
    if req.method == 'GET':
        serializer = DietReadSerializer(user.diet_set, many=True)
        return Response(serializer.data)
    if req.method == 'PUT':
        pass
    return Response()


@api_view(['POST', 'DELETE'])
def myDiet(req, dietId):
    try:
        user = User.objects.get(id=req.user.id)
        diet = Diet.objects.get(id=dietId)
    except User.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Diet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method == 'POST':
        user.diet_set.add(diet)
        return Response({}, status=status.HTTP_201_CREATED)
    if req.method == 'DELETE':
        user.diet_set.remove(diet)
        return Response({})


@api_view(['GET', 'PUT', 'DELETE'])
def diet(req, dietId):
    """
    Retrive, modify or delete single diet by id
    """
    try:
        diet = Diet.objects.get(id=dietId)
    except Diet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = DietReadSerializer(diet)
        return Response(serializer.data)

    elif req.method == 'PUT':
        serializer = DietSerializer(diet, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif req.method == 'DELETE':
        diet.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
