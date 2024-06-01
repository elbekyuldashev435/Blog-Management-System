from django.forms import ModelForm
from .models import Saved, Products, Comments


class Addsave(ModelForm):
    class Meta:
        model = Saved
        fields = "__all__"


class ProductUpdateForm(ModelForm):
    class Meta:
        model = Products
        fields = ('image', 'video', 'title', 'description')

<<<<<<< HEAD

class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['image', 'video', 'title', 'description']
=======
class AddCommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
>>>>>>> 4b4278c130807f6c602707a3f1778a3e45b9e02f
