from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:jss_id>/', views.detail, name="detail"),
    path('delete/<int:jss_id>/', views.delete, name='delete'),
    path('update/<int:jss_id>/', views.update, name="update"),
    path('myindex/', views.myindex, name='my_index'),

    #comment
    path('comment/<int:jss_id>/', views.createComment, name="createComment"),
    path('comment/<int:jss_id>/<int:comment_id>/', views.deleteComment, name="deleteComment"),
]