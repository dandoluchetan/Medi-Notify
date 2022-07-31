from django.forms import ModelForm
from cats.models import cat
class CatForm(ModelForm):
    class Meta:
        model=cat
        fields="__all__"