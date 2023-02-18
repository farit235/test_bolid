from django.urls import path
from events import views

urlpatterns = [
    path('', views.EventListView.as_view()),
    path('<int:pk>/', views.EventDetailView.as_view()),
    path('create/', views.EventCreateView.as_view()),
    path('<int:pk>/update/', views.EventUpdateView.as_view()),
    path('<int:pk>/delete/', views.EventDeleteView.as_view()),
    path('sensor/', views.SensorListView.as_view()),
    path('sensor/<int:pk>/', views.SensorDetailView.as_view()),
    path('sensor/create/', views.SensorCreateView.as_view()),
    path('sensor/<int:pk>/update/', views.SensorUpdateView.as_view()),
    path('sensor/<int:pk>/delete/', views.SensorDeleteView.as_view()),
    path('create-list/', views.EventListCreateView.as_view()),
]
