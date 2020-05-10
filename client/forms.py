from django import forms


class PhoneForm(forms.Form):
    phone = forms.CharField(label='Phone', max_length=13)


class CardForm(forms.Form):
    card = forms.CharField(label='Card', max_length=16)


# class DishIdForm(forms.Form):
#     dish_id = forms.IntegerField()
