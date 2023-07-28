
function closeDialog(closeBtn) { 
    document.getElementById(closeBtn.dataset.id).close();
    if(Boolean(closeBtn.dataset.post)) {
        document.getElementById(closeBtn.dataset.input_id).disabled = false;
    }
}

    