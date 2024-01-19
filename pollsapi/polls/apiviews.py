from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from polls.models import Polls, Choice
from polls.serializers import PollsSerializer

class PollList(APIView):
    def get(self, request):
        polls = Polls.objects.all()[:20]
        data =  PollsSerializer(polls, many=True).data
        return Response(data)
    

class PollDetail(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Polls, pk=pk)
        data = PollsSerializer(poll).data
        return Response(data)