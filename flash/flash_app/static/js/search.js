function search(text) {
    $.ajax('/search/', {
        type: 'POST',
        async: true,
        dataType: 'json',
        data: {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'data': text
        },
        success: (data) => {
            let dialog = document.getElementById('search_result');
            dialog.show();
            document.getElementById('dark').style.display = 'block';
            dialog.innerHTML = data['result'];
        }
    })
}