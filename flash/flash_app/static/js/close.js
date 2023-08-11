
function closeDialog(closeBtn) { 
    document.getElementById(closeBtn.dataset.id).close();
    document.getElementById('dark').style.display = 'none';
    if(Boolean(closeBtn.dataset.post)) {
        document.getElementById(closeBtn.dataset.input_id).disabled = false;
    }
}

    