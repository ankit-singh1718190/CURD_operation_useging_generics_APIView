from django.urls import path
from .views import studentListCreat,studentReUptDes
urlpatterns = [
    path('lc/',studentListCreat.as_view(),name='List-Create'),
    path('rud/<int:pk>/', studentReUptDes.as_view(), name='retrieve-update-destroy'),
]
