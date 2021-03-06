from django import forms

from .models import Post, Products, Shops, Manufactures

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class FindProductForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ('name',)


class FindShopsForm(forms.ModelForm):

    class Meta:
        model = Shops
        fields = ('name',)

class FindShopForm(forms.ModelForm):

    class Meta:
        model = Shops
        fields = ('address',)


class FindManufactureForm(forms.ModelForm):

    class Meta:
        model = Manufactures
        fields = ('name',)

class FindPriceForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ('price',)