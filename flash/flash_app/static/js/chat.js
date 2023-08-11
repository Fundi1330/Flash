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
            let text = document.getElementById('no_messages');
            if(text != null) {
                messages.removeChild(text);
            }
            document.getElementById('new_message').value = '';
            messages.innerHTML += data['message'];
        }
    });
});


// document.addEventListener('mouseenter', (ev) => {
//     const element = ev.target;
//     if(element.classList.contains('message')) {
//         const button = document.createElement('button');
//     }
// })