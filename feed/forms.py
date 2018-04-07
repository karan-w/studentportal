from django import forms
class PostForm(forms.Form):
    text = forms.CharField(label='text', max_length=100, required=True)
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    ACADEMIC = 'AC'
    CLUBSANDASSOCIATIONS = 'CA'
    CLASSREPRESENTATIVE = 'CR'
    GENERAL = 'GN'
    SPORTS = 'SP'
    CATEGORY_CHOICES = (
        (ACADEMIC, 'Academics'),
        (CLUBSANDASSOCIATIONS, 'Clubs and Associations'),
        (GENERAL,'General'),
        (CLASSREPRESENTATIVE, 'Class Representative'),
        (SPORTS, 'Sports'),
    )
    category = forms.ChoiceField(choices = CATEGORY_CHOICES, label="", initial='', widget=forms.Select(), required=True)