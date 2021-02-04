from django.forms import ModelForm
from django import forms
from first.models import InfectedPlace
from django.utils.translation import gettext_lazy as _

class InfectedPlaceForm(ModelForm):
    class Meta:
        model = InfectedPlace
        fields = ['name', 'address', 'lat', 'lng', 'happened_at', 'reported2oie_at', 'memo', 'password']
        labels = {
            'name': _('국가명'),
            'address': _('발생지역'),
            'lat': _('위도'),
            'lng': _('경도'),
            'happened_at': _('발병일'),
            'reported2oie_at': _('OIE 보고일'),
            'memo': _('세부사항'),
            'password': _('비밀번호'),
        }
        help_texts = {
            'happened_at': _('YYYY-MM-DD'),
            'reported2oie_at': _('YYYY-MM-DD'),
        }
        widgets = {
            'password': forms.PasswordInput()
        }
        
class UpdateInfectedPlaceForm(InfectedPlaceForm):
    class Meta:
        model = InfectedPlace
        exclude = ['password']