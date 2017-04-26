from django import forms

class UserForm(forms.Form):
    genderchoices = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    email = forms.CharField(max_length=50)
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=20)
    gender = forms.ChoiceField(choices=genderchoices, required=True)

class ReportForm(forms.Form):
    vectors = (
        ('aedes', 'Aedes Mosquito'),
        ('rat', 'Rat'),
    )

    amount = (
        ('5', '1 - 10'),
        ('18', '11 - 25'),
        ('38', '26 - 50'),
        ('75', '51 - 100'),
    )
    case_vector = forms.ChoiceField(choices=vectors, required=True)
    case_vec_num = forms.ChoiceField(choices=amount, required=True)
    #case_date = forms.DateTimeField(auto_now_add=True)
