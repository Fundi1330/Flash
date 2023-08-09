let writeMessageBtn = document.getElementById('write-msg-btn');

writeMessageBtn.addEventListener('click', () => {
    $.ajax('/chat/' + writeMessageBtn.dataset['id'], {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'msg': $('#new_message').val()
        },
        'success': (data) => {
            const messages = document.getElementById('chat_messages');
            if(messages.innerHTML.includes('<p>No messages here...</p>')) {
                messages.innerHTML.replace('<p>No messages here...</p>', '');
            }
            document.getElementById('new_message').value = '';
            messages.innerHTML += data['message'];
        }
    });
});