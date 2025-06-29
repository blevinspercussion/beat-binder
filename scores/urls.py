from django.urls import path 
from .views import ScoreListView, ScoreDetailView, ScoreCreateView 

app_name = 'scores'

urlpatterns = [
    path('', ScoreListView.as_view(), name='score_list'),
    path('<int:pk>/', ScoreDetailView.as_view(), name='score_detail'),
    path('upload/', ScoreCreateView.as_view(), name='score_upload'),
]