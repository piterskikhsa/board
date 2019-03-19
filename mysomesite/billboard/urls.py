from django.urls import path, include

from .views import index, by_rubric, AdvCreateView

app_name = 'bboard'

urlpatterns = [
    path('add/', AdvCreateView.as_view(), name='add_adv'),
    path('<int:rubric_id>', by_rubric, name='by_rubric'),
    path('', index, name='home'),
]
