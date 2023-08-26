from django.forms import ModelForm
from .models import  Project


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        # fields = ['title', 'body']
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'from-control'})
        self.fields['body'].widget.attrs.update({'class': 'from-control'})
