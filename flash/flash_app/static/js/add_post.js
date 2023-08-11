function show(id, input) {
    let dialog = document.getElementById(id);
    dialog.show();
    document.getElementById('dark')
    input.disabled = true;
    dialog.addEventListener('close', () => {
        input.disabled = false;
    })
}

let cropper;

function uploadFile() {
    $('#post_image').change(() => {
        let img = new FormData();
        let image;
        img.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val());
        img.append('file', document.getElementById('post_image').files[0]);
        $.ajax('/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': img,
            'processData': false,
            'contentType': false,
            'success': (data) => {
                image = document.getElementById('post-img');
                image.setAttribute('src', '../../../../media/images/posts/upload.png');
                document.getElementById('img-container').style.display = 'block';
                cropper = new Cropper(image, {
                    aspectRatio: 1 / 1,
                    viewMode: 3,
                    
                });
                image.addEventListener('cropend', (ev) => {
                    cropper.getCroppedCanvas().toBlob((blob) => {
                        let img = new FormData();
                        img.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val());
                        img.append('file', blob);
                        $.ajax('/', {
                            'type': 'POST',
                            'async': true,
                            'dataType': 'json',
                            'data': img,
                            'processData': false,
                            'contentType': false,
                            'success': (data) => {
                            
                            }
                        });
                    });
                
                });
            }
        });
        
    });
}

function ajax() {
    $('#create-post-btn').click(() => {
        $.ajax('/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'title': $('#post_title').val(),
                'text': $('#post_body').val()
            },
            'success': (data) => {
                document.getElementById('new_post').close();
                document.getElementById('posts').insertAdjacentHTML('beforebegin', data['post']);
            }
        });
    });
}

$(document).ready(() => {
    uploadFile();
    ajax();

});