from django import forms
from .models import Review, Rating, RatingStar
# from snowpenguin.django.recaptcha3.fields import ReCaptchaField
# from snowpenguin.django.recaptcha3.fields import ReCaptchaField
# from captcha.fields import ReCaptchaField

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=("name", "email", "text")
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control border"}),
            "email":forms.EmailInput(attrs={"class":"form-control border"}),
            "text":forms.Textarea(attrs={"class":"form-control border"})
        }


class RatingForm(forms.ModelForm):
    star=forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
        )

    class Meta:
        model=Rating
        fields=('star',)

