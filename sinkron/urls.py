from django.urls import path

from index.views import index, progress

urlpatterns = [
    path('', index, name="index"),
    path('progress/<task>/', progress, name='progress')
]
