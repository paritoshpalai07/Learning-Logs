from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic']
        labels = {'topic':''}

    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)
        self.fields['topic'].widget.attrs['placeholder'] = 'Enter your today\'s topic'
        self.fields['topic'].widget.attrs['autofocus'] = True

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['entry']
        labels = {'entry' : ''}

    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        self.fields['entry'].widget.attrs['placeholder'] = 'Enter your today\'s entry'
        self.fields['entry'].widget.attrs['autofocus'] = True


