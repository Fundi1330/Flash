// let buttons = document.querySelectorAll('.comment')

// for(let button of buttons) {
//     document.getElementById(button.id).show();
//     document.body.style.overflow = 'hidden';
//     document.body.style.height = '100%';
// }

let shareButtons = document.querySelectorAll('.share');

for(let button of shareButtons) {
    button.addEventListener('click', () => {
        document.getElementById('messages').innerHTML += '<li class="info flex justify-center items-center left-1/2 z-10 bg-white -translate-x-1/2 fixed p-8 border border-l-8 border-l-green-500 w-1/3 mx-auto -mt-16 rounded-xl">Link copied to clipboard<button onclick="this.parentNode.remove(this.Node);"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-10 h-10"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" /></svg></button></li>'; 
        navigator.clipboard.writeText(window.location + '#post-' + button.dataset.id); 
    });
}

let editBtn = document.getElementsByClassName('edit-post-btn');
for(let btn of editBtn) {
    btn.addEventListener('click', () => {
        document.getElementById(btn.dataset['id'] + '-edit').close();
        document.getElementById(btn.dataset['id']).show();
        $.ajax('/edit_post/' + btn.dataset['id'], {
            'type': 'POST',
            'dataType': 'json',
            'async': true,
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'new_title': $('#edit-post-title-' + btn.dataset['id']).val(),
                'new_text': $('#edit-post-body-' + btn.dataset['id']).val(),
                'id': btn.dataset['id']
            },
            'success': (data) => {  
                document.getElementById('post-modal-text-' + btn.dataset['id']).innerText = data['text'];
                document.getElementById('post-text-' + btn.dataset['id']).innerText = data['text'];
                document.getElementById('post-modal-title-' + btn.dataset['id']).innerText = data['title'];
                document.getElementById('post-title-' + btn.dataset['id']).innerText = data['title'];
            }
        });
    });
}

let commentsBtn = document.getElementsByClassName('create-comment-btn');

for(let commentBtn of commentsBtn) {
    commentBtn.addEventListener('click', () => {
        const id = commentBtn.dataset['id'];

        $.ajax('/comment/', {
            'type': 'POST',
            'dataType': 'json',
            'async': true,
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'comment': document.getElementById('comment-' + id).value,
                'post': id
            },
            'success': (data) => {
                document.getElementById('comments-' + id).innerHTML += data['comment'],
                document.getElementById('comment-' + id).value = '';
            }
        })
    });
}

let deletPostButtons = document.getElementsByClassName('delete-post-btn');

for(let deletePostBtn of deletPostButtons) {
    deletePostBtn.addEventListener('click', () => {
        const id = deletePostBtn.dataset['id'];
        $.ajax('/delete_post/', {
            'type': 'POST',
            'dataType': 'json',
            'async': true,
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'post': id
            },
            'success': (data) => {
                let post = document.getElementById('posts-post-' + data['id']);
                post.parentNode.removeChild(post);
                document.getElementById(`sure-delete this post-${ data['id'] }`).close();
                document.getElementById('dark').style.display = 'none';
            }
        })
    });
}

const likeBtns = document.getElementsByClassName('like');

for(let likeBtn of likeBtns) {
    likeBtn.addEventListener('click', () => {
        let id = likeBtn.dataset['id'];
        if(!likeBtn.firstElementChild.classList.contains('fill-red-600')) {
            likeBtn.firstElementChild.classList.add('fill-red-600');
            $.ajax('/like/', {
                'type': 'POST',
                'dataType': 'json',
                'async': true,
                'data': {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'post': id,
                    'like': true
                },
                'success': (data) => {
                    let likesNum = document.getElementById('likes-num-' + data['id']);
                    likesNum.innerText = Number(likesNum.innerText) + 1;
                    document.getElementById('likes-' + data['id']).innerText = pluralize('like', Number(likesNum.innerText))
                }
            })
        } else {
            likeBtn.firstElementChild.classList.remove('fill-red-600');
            $.ajax('/like/', {
                'type': 'POST',
                'dataType': 'json',
                'async': true,
                'data': {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'post': id,
                    'unlike': true
                },
                'success': (data) => {
                    let likesNum = document.getElementById('likes-num-' + data['id']);
                    likesNum.innerText = Number(likesNum.innerText) - 1;
                    document.getElementById('likes-' + data['id']).innerText = pluralize('like', Number(likesNum.innerText))
                }
            })
        }
    });
}

