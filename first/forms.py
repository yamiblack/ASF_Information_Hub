from django.forms import ModelForm
from first.models import InfectedPlace
from django.utils.translation import gettext_lazy as _

class InfectedPlaceForm(ModelForm):
    class Meta:
        model = InfectedPlace
        fields = ['name', 'address', 'lat', 'lng', 'memo']
        labels = {
            'name': _('이름'),
            'address': _('주소'),
            'lat': _('위도'),
            'lng': _('경도'),
            'memo': _('세부사항'),
        }