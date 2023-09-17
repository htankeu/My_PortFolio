from django.forms import ModelForm
from .models import  Project, Message, Skill


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        # fields = ['title', 'body']
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'from-control'})
        self.fields['body'].widget.attrs.update({'class': 'from-control'})


class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['is_read']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'from-control'})
        self.fields['email'].widget.attrs.update({'class': 'from-control'})
        self.fields['subject'].widget.attrs.update({'class': 'from-control'})
        self.fields['body'].widget.attrs.update({'class': 'from-control'})


class SkillForm(ModelForm):

    class Meta:
        model = Skill
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'from-control'})
        self.fields['body'].widget.attrs.update({'class': 'from-control'})