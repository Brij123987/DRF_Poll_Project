from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse
from polls.models import Polls

# Create your views here.

def poll_lists(request):
    MAX_OBJECTS = 20
    polls = Polls.Objects.all() [:MAX_OBJECTS]
    data = {'results':list(polls.values("question","created_by__username","pub_date"))}
    return JsonResponse(data)


def poll_details(request, pk):
    poll = get_list_or_404(Polls, pk=pk)
    data = {
        "results":{
            "question":poll.question,
            "created_by":poll.created_by.username,
            "pub_date":poll.pub_date

        }
    }
    return JsonResponse(data)

