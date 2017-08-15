from django import forms


class SearchForm(forms.Form):
    origin_field = forms.CharField(label='From', max_length=100, initial='uk')
    destination_field = forms.CharField(label='To', max_length=100, initial='us')
    from_date_field = forms.CharField(label='To', max_length=100, initial='2017')
    to_date_field = forms.CharField(label='To', max_length=100, initial='2017')
    service_field = forms.ChoiceField(choices=[('browsequotes','Quotes'),('browseroutes','Routes'),('browsedates','Dates'),('browsegrid','Grid')], widget=forms.RadioSelect())