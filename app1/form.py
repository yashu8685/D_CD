from django import forms
from app1.models import student
class S_form(forms.ModelForm):
    class Meta:
        model=student

        fields='__all__'





# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/yashu8685/D_CD.git
# git push -u origin main