from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer,CustomUserDetailsSerializer,CustomUserProductSerializer
from base.models import CustomUser,UserProducts
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated


class CustomUserView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def post(self, request, *args, **kwargs):
        reg_serializer = CustomUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()  # Use save method of the serializer
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        userid = request.GET.get('userid')
        queryset = CustomUser.objects.get(id=userid)
        serializer = CustomUserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CustomUserDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserDetailsSerializer
    

    def get(self, request):
        userid = self.request.query_params.get('userid')
        try:
            user = CustomUser.objects.get(id=userid)
            serializer = CustomUserDetailsSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            raise Http404("User does not exist")

    def post(self, request):
        userid = request.query_params.get('userid')
        try:
            user = CustomUser.objects.get(id=userid)
            serializer = CustomUserDetailsSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User updated successfully'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            raise Http404("User does not exist")

class CustomUserProductView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserProductSerializer

    def get(self, request):
        userid = self.request.query_params.get('userid')
        try:
            user = UserProducts.objects.get(id=userid)
            serializer = CustomUserProductSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserProducts.DoesNotExist:
            raise Http404("User does not exist")


    def post(self, request):
        parser_classes = (MultiPartParser, )
        user_email = request.user.email
        try:
            created_by = CustomUser.objects.get(email=user_email)
            user = UserProducts.objects.create(user=created_by)
            serializer = CustomUserProductSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User updated successfully'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            raise Http404("User does not exist")
        
class BlacklistTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logged out successfully'})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)