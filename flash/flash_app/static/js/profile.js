let editProfileBtn = document.getElementById('edit-profile-btn');

editProfileBtn.addEventListener('click', () => {
    $.ajax(editProfileBtn.dataset['url'], {
        type: 'POST',
        dataType: 'json',
        async: true,
        data: {
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'bio': $('#bio').val()
        },
        success: (data) => {
            document.getElementById('user-bio').innerText = data['bio'];
            editProfileBtn.parentElement.close();
            document.getElementById('dark').style.display = 'none';
        }
    });

});
let followBtn = document.getElementById('follow-btn');

if(followBtn != undefined) {
    followBtn.addEventListener('click', () => {
        if(followBtn.innerText == 'Follow') {
            $.ajax(editProfileBtn.dataset['url'], {
                type: 'POST',
                dataType: 'json',
                async: true,
                data: {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'follow': true,
                    'user': followBtn.dataset['user']
                },
                success: (data) => {
                    followBtn.innerText = 'Unfollow';
                    let followersNum = document.getElementById('followers-num');
                    followersNum.innerText = Number(followersNum.innerText) + 1;
                    document.getElementById('followers').innerText = pluralize('follower', Number(followersNum.innerText))
                }
            });
        } else {
            $.ajax(editProfileBtn.dataset['url'], {
                type: 'POST',
                dataType: 'json',
                async: true,
                data: {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'unfollow': true,
                    'user': followBtn.dataset['user']
                },
                success: (data) => {
                    followBtn.innerText = 'Follow';
                    let followersNum = document.getElementById('followers-num');
                    followersNum.innerText = Number(followersNum.innerText) - 1;
                    document.getElementById('followers').innerText = pluralize('follower', Number(followersNum.innerText));
                }
            });
        }
    });
}