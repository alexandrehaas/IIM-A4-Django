from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='cvIndex'),
    path('upload', views.upload, name='cvUpload'),
    path('uploaded', views.uploaded, name="cvUploaded")
]