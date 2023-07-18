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
        navigator.clipboard.writeText(window.location + 'post/' + button.dataset.id); 
    });
}