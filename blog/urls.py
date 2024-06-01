from django.urls import path
from .views import ProductsView, DetailView, SavedView, ProductUpdate, AboutView, AddCommentView, CommentView


app_name = 'home'
urlpatterns = [
    path('', ProductsView.as_view(), name='home-page'),
    path('detail/<int:pk>/', DetailView.as_view(), name='detail'),
    path('saved/', SavedView.as_view(), name='saved'),
    path('add-save/<int:pk>/', SavedView.as_view(), name='add-save'),
    path('product-update/<int:pk>/', ProductUpdate.as_view(), name='product-update'),
    path('about/', AboutView.as_view(), name='about'),
    path('add-comment/<int:pk>/', AddCommentView.as_view(), name='add-comment'),
    path('comments/<int:pk>/', CommentView.as_view(), name='comment'),

]