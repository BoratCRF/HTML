document.addEventListener('DOMContentLoaded', function () {
    
    const firstRadio = document.querySelector('input[type="radio"]');
    if (firstRadio) {
        firstRadio.checked = true;
        firstRadio.dispatchEvent(new Event('change'));
    }
});

document.querySelectorAll('input[type="radio"]').forEach(radio => {
    radio.addEventListener('change', function() {
   
        document.querySelectorAll('.content').forEach(content => {
            content.style.display = 'none';
        });

       
        if (this.id === 'radio_toTheHel') {
            document.querySelector('.content_toTheHel').style.display = 'block';
        } else if (this.id === 'radio_flappyCat') {
            document.querySelector('.content_flappyCat').style.display = 'block';
        } else if (this.id === 'radio_skyfighter') {
            document.querySelector('.content_skyfighter').style.display = 'block';
        }
    });
});
