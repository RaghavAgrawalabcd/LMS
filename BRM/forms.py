from django import forms

class book_form(forms.Form):
    Bcode=forms.IntegerField(label="Bcode")
    Btitle=forms.CharField(label="Btitle",max_length=20)
    Bauthor=forms.CharField(label="Bauthor",max_length=20)
    Bpublisher=forms.CharField(label="Bpublisher",max_length=20)

class search_form(forms.Form):
    Bcode=forms.IntegerField(label="Bcode")