import random
import markdown

from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Note, Quotes, Topic, Room, Message, ToDoList

from .gemini import notes

@login_required(login_url='login')
def home(request):

    if request.POST.get('name'):
        if request.method == 'POST':
            noteName = request.POST.get('name').title()
            noteUserName = request.user

            note = Note.objects.create(name=noteName, user=noteUserName)
            return redirect('home')
    
    show_all = request.GET.get('show') == 'all'

    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    show_less = False

    if show_all:
        notes = Note.objects.filter(
            Q(name__icontains=q) & Q(user=request.user)
        )
        show_less = True
    else:
        notes = Note.objects.filter(
            Q(name__icontains=q) & Q(user=request.user)
        )[:5]

    quote = Quotes.objects.get(id=random.randint(1,14))
    rooms = Room.objects.all().order_by('-created_at')[:5]
    toDoListItems = ToDoList.objects.all()
    revision_topic = Topic.objects.order_by('?').first()
    context = {
        'notes':notes,
        'quote':quote,
        'rooms':rooms,
        'q': q,
        'show_less':show_less,
        'listItems':toDoListItems,
        'revision_topic':revision_topic,
    }
    return render(request, 'base/home.html', context)

def deleteToDListItem(request, pk):
    listItem = ToDoList.objects.get(id=pk)
    listItem.delete()
    return redirect('home')


def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return redirect('home')

def updateNote(request, pk):
    update = True
    note = Note.objects.get(id=pk)
    revision_topic = Topic.objects.order_by('?').first()

    if request.method == "POST":
        noteName = request.POST.get('name');
        note.name = noteName
        note.save()
        return redirect('home')

    notes = Note.objects.exclude(id=pk).filter(user=request.user)
    quote = Quotes.objects.get(id=random.randint(1,5))


    context = {
        'note':note,
        'notes':notes,
        'quote':quote,
        'update':update,
        'revision_topic':revision_topic,
    }

    return render(request, 'base/home.html', context)


def noteView(request, pk):
    note = Note.objects.get(id=pk)

    if request.POST.get('todoitem'):
        if request.method == 'POST':
            listItem = request.POST.get('todoitem').title()
            ToDoList.objects.create(listItem=listItem, listOwner=request.user)
            return redirect('')

    if request.POST.get('topic-name'):
        if request.method == 'POST':
            topicName = request.POST.get('topic-name').title()
            url = request.POST.get('youtube-url')
            vidSummary = notes(url)
            vidSummary = markdown.markdown(vidSummary[0])
            transcript = vidSummary[1]
            print(transcript)
            Topic.objects.create(topic_name=topicName, url=url, note=note, summary=vidSummary, transcript=transcript)
            return redirect('note_view', note.id)
    
    recent_topic = Topic.objects.filter(note=note).first()
    topics = Topic.objects.filter(note=note)
    context = {
        'note':note,
        'recent_topic':recent_topic,
        'topics':topics,
    }
    return render(request,'base/note.html', context)


def noteTopicView(request, noteId, topicId):
    note = Note.objects.get(id=noteId)
    selected_topic = Topic.objects.get(id=topicId)
    topics = Topic.objects.filter(note=note)
    context = {
        'note':note,
        'selected_topic':selected_topic,
        'topics':topics,
    }

    return render(request, 'base/note_topic.html', context)


def topicDelete(request, noteId, topicId):
    note = Note.objects.get(id=noteId)
    topic = Topic.objects.get(id=topicId)
    topic.delete()
    return redirect('note_view', note.id)

# def topicUpdate(request, noteId, topicId):
#     update = True
#     context = {'upadte':update}
#     return render(request, 'base/note.html', context)


# def addTopic(request):
#     topicName = request.POST.get('topic-name')
#     return render(request, 'base/note.html')



# def topicView(request, noteId, topicId):
#     note = 


# def noteUpdate(request, pk):
#     note = Note.objects.get(id=pk)
#     form = NoteForm(instance=note)

#     if request.method == 'POST':
#         form = NoteForm(request.POST, instance=note)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
        
#     context = {'updateForm':form}
#     return render(request,'base/home.html', context)

def roomView(request, pk):
    room = Room.objects.get(id=pk)
    messages = room.message_set.all().order_by('-created_at')
    
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            Message.objects.create(user=request.user, room=room, body=message)
            return redirect('room_view', pk)

    context = {
        'room':room,
        'messages':messages,
    }
    return render(request, 'base/room.html', context)


def test(request):
    return render(request, 'test.html')