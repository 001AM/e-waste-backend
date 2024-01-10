from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer,CustomUserDetailsSerializer,CustomUserProductSerializer,CustomUserProductSellerSerializer, LoginSerializer, EducationSerializer
from base.models import CustomUser,UserProducts, Education
from rest_framework_simplejwt.tokens import RefreshToken, Token
from django.http import Http404
from django.core.mail import send_mail,EmailMessage
from django.db import transaction
from django. shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from base.forms import CustomUserCreationForm


class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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
        statusget = request.query_params.get('filter')
        print(status)
        userid = request.user.id
        print(userid)
        try:
            if statusget == 'empty':
                user = UserProducts.objects.filter(user=userid)
            else: 
                user = UserProducts.objects.filter(user=userid, status=statusget)
            print(user)
            serializer = CustomUserProductSerializer(user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)  # Use status.HTTP_200_OK
        except UserProducts.DoesNotExist:
            raise Http404("User does not exist")

    def post(self, request):
        ewaste_coins = {
            'Phone': 100,
            'Headset': 150,
            'Laptop': 300,
            'Mixer': 200,
            'Refrigerator': 500,
            'Speaker': 250,
            'Television': 400,
            'Washing Machine': 450,
        }
        user = request.user
        user_email = request.user.email

        try:
            created_by = CustomUser.objects.get(email=user_email)
            user_product = UserProducts(user=created_by)

            product_type = request.data.get('product_type')

            if product_type in ewaste_coins:
                user_product.product_type = product_type
                user_product.coins = ewaste_coins[product_type]
                    # Generate a random order number of length 10
            import random
            import string
            order_no = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            user_product.orderno = order_no
            user_product.status = 'None'

            serializer = CustomUserProductSerializer(user_product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                user.save()
                return Response({'message': 'User product created successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            raise Http404("User does not exist")

class CustomUserProductSellerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            ticketid = request.query_params.get('ticketid')
            userid = request.query_params.get('id')
            print(ticketid,userid)
            try:
                user = UserProducts.objects.filter(user=userid, id=ticketid)
                print(user)
                serializer = CustomUserProductSerializer(user, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)  # Use status.HTTP_200_OK
            except UserProducts.DoesNotExist:
                raise Http404("User does not exist")
        except:
            pass
    
    def post(self, request):
        ticketid = request.POST.get('id')
        userid = request.POST.get('user')
        try:
            user_product = UserProducts.objects.get(user=userid, id=ticketid)
            # You can generate a random order number of length 10
            import random
            import string
            transaction_no = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
            user_product.transaction_no = transaction_no
            user_product.status = 'Yes'
            serializer = CustomUserProductSellerSerializer(user_product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User product created successfully'}, status=status.HTTP_201_CREATED)
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
        
class EducationView(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        try:
            if id:
                education = Education.objects.get(id=id)
                serializer = EducationSerializer(education)
            else:
                education = Education.objects.all().order_by('-created_on').values()  # Optionally, add .order_by('some_field')
                serializer = EducationSerializer(education, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Education.DoesNotExist:
            return Response({"error": "Education record not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Log the exception for debugging
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
