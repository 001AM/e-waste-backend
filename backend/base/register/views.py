from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EventCard
from .serializers import EventCardSerializer

class EventCardView(APIView):
    def get(self, request):
        events = request.query_params.get('event')
        try:
            if events:
                event = EventCard.objects.get(title=events)
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
