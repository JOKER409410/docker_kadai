from django import forms

from .models import Seat


class SeatAssignForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = ["occupant_name"]
        widgets = {
            "occupant_name": forms.TextInput(attrs={"placeholder": "氏名を入力"}),
        }
        labels = {"occupant_name": "氏名"}