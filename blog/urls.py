from django.urls import path
<<<<<<< HEAD
from .views import ProductsView, DetailView, SavedView, ProductUpdate, AboutView, ProductDeleteView, AddProductView
=======
from .views import ProductsView, DetailView, SavedView, ProductUpdate, AboutView, AddCommentView, CommentView
>>>>>>> 4b4278c130807f6c602707a3f1778a3e45b9e02f


app_name = 'home'
urlpatterns = [
    path('', ProductsView.as_view(), name='home-page'),
    path('detail/<int:pk>/', DetailView.as_view(), name='detail'),
    path('saved/', SavedView.as_view(), name='saved'),
    path('add-save/<int:pk>/', SavedView.as_view(), name='add-save'),
    path('product-update/<int:pk>/', ProductUpdate.as_view(), name='product-update'),
    path('about/', AboutView.as_view(), name='about'),
<<<<<<< HEAD
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('add-product/', AddProductView.as_view(), name='add-product'),
=======
    path('add-comment/<int:pk>/', AddCommentView.as_view(), name='add-comment'),
    path('comments/<int:pk>/', CommentView.as_view(), name='comment'),

>>>>>>> 4b4278c130807f6c602707a3f1778a3e45b9e02f
]