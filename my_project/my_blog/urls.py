from django.urls import path
from .import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('detail/<int:pk>/',views.post_detail,name='post_detail'),
    path('edit/<int:pk>/',views.post_edit,name='edit'),
    path('delete/<int:pk>/',views.post_delete,name='delete'),
    #path('about/',views.about,name='about'),
]
