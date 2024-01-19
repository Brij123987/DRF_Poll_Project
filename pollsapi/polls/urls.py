from django.urls import path, include
from polls import views
from .apiviews import PollList, PollDetail

# URLS ------------------------------------

urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail")
]