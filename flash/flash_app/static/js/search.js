function search(text) {
    $.ajax('/search', {
        type: 'POST',
        async: true,
        dataType: 'json',
        data: {
            'data': text
        },
        success: (data) => {
            console.log(data)
        }
    })
}