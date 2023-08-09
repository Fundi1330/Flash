

function create_chat(btn) {
    $.ajax('/start_chat', {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'id': btn.dataset['id']
        },
        'success': (data) => {
            if(data['chat'] != undefined) {
                document.body.innerHTML = data['chat'];
            } 
        }
    });
}