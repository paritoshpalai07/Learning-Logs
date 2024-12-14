from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

from django.contrib.auth.decorators import login_required

# --------------------------------------    INDEX VIEW  ---------------------------------------------------
def index(request):
    return render(request, 'index.html')

# ------------------------------------------    TOPICS VIEW -------------------------------------------------
# View to show topics
@login_required
def show_topics(request, user_id):
    user = User.objects.get(id=user_id)
    topics = user.topic_set.all()
    context = {'user': user, 'topics' : topics}
    return render(request, 'topics.html', context)

# View to add new topic
def new_topic(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.user = user
            new_topic.save()
            return redirect('show_topics', user_id=user.id)
        
    context = {'form' : form}
    return render(request, 'new_topic.html', context)

# View to delete topics
def delete_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    user = topic.user_id
    topic.delete()
    return redirect('show_topics', user_id = user)

#---------------------------------------------  ENTRIES VIEW ---------------------------------------------------------
# View to show entries
def show_entries(request, user_id, topic_id):
    user = User.objects.get(id=user_id)
    topic = user.topic_set.get(id=topic_id)
    entries = topic.entry_set.all().order_by('-date')
    context = {'topic' : topic, 'entries' : entries}
    return render(request, 'entries.html', context)

# view to add new entries
def new_entry(request, user_id, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('show_entries',user_id=user_id, topic_id=topic_id)
        
    context = {'topic': topic,'form' : form}
    return render(request, 'new_entry.html', context)

# View to edit entries
def edit_entry(request, user_id, topic_id, entry_id):
    user = User.objects.get(id=user_id)
    topic = user.topic_set.get(id=topic_id)
    entry = topic.entry_set.get(id=entry_id)

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_entries',user_id ,topic_id)
        
    context = {
        'entry' : entry,
        'topic' : topic,
        'form' : form,
    }

    return render(request, 'edit_entry.html', context)

# view to delete entries
def delete_entry(request,user_id, topic_id, entry_id):
    user = User.objects.get(id=user_id)
    topic = user.topic_set.get(id=topic_id)
    entry = topic.entry_set.get(id=entry_id)
    entry.delete()
    return redirect('show_entries', user_id, topic_id)


# --------------------------------------    REGISTRATION VIEW   ------------------------------------------------------------
def register_view(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('show_topics', user.id)
        
    context  = {'form' : form}
    return render(request, 'register.html', context)

def login_view(request):
    if request.method != 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('show_topics', user.id)
        
    context  = {'form' : form}
    return render(request, 'login.html', context)

def logout(request):
    # user = User.objects.get(id=user_id)
    logout(request)
    return redirect('index')