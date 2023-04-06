from django.urls import path
from .views import ListarPostsListView, ExtendPost

urlpatterns = [
    path('', ListarPostsListView.as_view(), name='home'),
    path('detalhe/<slug:slug>/', ExtendPost.as_view(), name='postDetail'),

]