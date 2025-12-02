let topicForm = document.getElementById('add-topic-form');
    // let noTopicMsg = document.getElementById('note-topic');
    // let ytContainer = document.getElementById('youtube-container');
    let topicDiv = document.getElementById('topic-div');
    let overAllTopicDiv = document.getElementById('note-topic');

    topicDiv.querySelectorAll('h2').forEach((h2)=>{
        h2.classList.add('font-bold');
    });

    topicDiv.querySelectorAll('h3').forEach((h3)=>{
        h3.classList.add('font-bold');
    });

    topicDiv.querySelectorAll('ul').forEach((ul)=>{
        ul.classList.add('list-disc');
        ul.classList.add('pl-5');

    });

    function togglehide(){
        topicForm.classList.toggle('hidden');
        overAllTopicDiv.classList.toggle('hidden');
        console.log('CLICKED');
        // noTopicMsg.classList.toggle('hidden');
    }