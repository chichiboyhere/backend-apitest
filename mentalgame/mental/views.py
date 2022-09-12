from rest_framework import viewsets
from .serializers import *
from .models import MentalGameResult, QuantitativeSpsec
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from rest_framework import status

# Create your views here.

# Class view helps with fetching and posting results when user is NOT authenticated
class MentalGameView(viewsets.ModelViewSet):
    serializer_class = MentalGameResultSerializer
    queryset = MentalGameResult.objects.all()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data

    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyResults(request):
    user = request.user
    results = user.mentalgameresult_set.all()
    serializer = MentalGameResultSerializer(results, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postMyResult(request):
    user = request.user
    data = request.data
    result=MentalGameResult.objects.create(
        user=user,
        score=data['score'],
        questions=data['questions'],
        speed=data['speed']
    )
    serializer = MentalGameSerializer(result, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getQuantitativeSpsec(request):
    user = request.user
    results = user.quantitativespsec_set.all()
    serializer = QuantitativeSpsecSerializer(results, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postQuantitativeSpsec(request):
    user = request.user
    data = request.data
    result=QuantitativeSpsec.objects.create(
        user=user,
        score=data['score'],
        quantitativeSps=data['quantitativeSps'],
        
    )
    serializer = QuantitativeSerializer(result, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getVerbalSpsec(request):
    user = request.user
    results = user.verbalspsec_set.all()
    serializer = VerbalSpsecSerializer(results, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postVerbalSpsec(request):
    user = request.user
    data = request.data
    result=VerbalSpsec.objects.create(
        user=user,
        score=data['score'],
        verbalSps=data['verbalSps'],
        
    )
    serializer = VerbalSerializer(result, many=False)
    return Response(serializer.data)   

