from django.contrib import admin
from django.urls import path
from . import views
from thirdproject.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('firstpage/', views.first),
    path('next/', views.second),
    path('second/', views.next),
    path('nature/', views.third),
    path('firstmodel/', views.exml),
    path('secondmodel/', views.exml1),
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-feedback'),
    path('register/', views.register, name = 'register'),
    path('update/<int:feedback_id>', views.update_feedback),
    path('delete/<int:feedback_id>', views.delete_feedback),
    path('send/', views.send_message)
]
#DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)