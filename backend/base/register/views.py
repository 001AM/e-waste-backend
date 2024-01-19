# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EventCard, EventRegistration, CastImage
from .serializers import EventCardSerializer, EventRegistrationSerializer, CastImageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

class EventCardView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = EventCardSerializer(data=request.data)
        if serializer.is_valid():
            event = serializer.save()

            # Handle cast images
            cast_images_data = request.data.getlist('cast_images', [])
            for cast_image_data in cast_images_data:
                # Create a new CastImage instance
                cast_image_instance = CastImage(event=event)

                # Update the image field with the uploaded file
                cast_image_instance.image = cast_image_data

                # Save the CastImage instance
                cast_image_instance.save()

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
                events = EventCard.objects.all().order_by('-date')
                serializer = EventCardSerializer(events, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except EventCard.DoesNotExist:
            return Response({"error": "Event record not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EventRegistrationView(APIView):
    def post(self, request):
        serializer = EventRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddCastImageView(APIView):
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
