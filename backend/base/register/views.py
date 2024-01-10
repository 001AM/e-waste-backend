from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

class EventCardView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = EventCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        id = request.query_params.get('id')
        try:
            if id:
                event = EventCard.objects.get(id=id)
                serializer = EventCardSerializer(event)
            else:
                # Replace 'created_on' with 'date' or another appropriate field
                events = EventCard.objects.all().order_by('-date')
                serializer = EventCardSerializer(events, many=True)
                
            return Response(serializer.data, status=status.HTTP_200_OK)
        except EventCard.DoesNotExist:
            return Response({"error": "Event record not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Add logging here
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EventRegistrationView(APIView):
    def post(self, request):
        serializer = EventRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AddCastImageView(APIView):
    """
    View to add a cast image to an EventCard.
    """
    def post(self, request, event_id, format=None):
        try:
            event = EventCard.objects.get(id=event_id)
        except EventCard.DoesNotExist:
            return Response({'error': 'EventCard not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CastImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(event=event)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)