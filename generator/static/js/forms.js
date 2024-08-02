document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const loading = document.getElementById('loading');
    const submitButton = form.querySelector('button[type="submit"]');

    form.addEventListener('submit', (event) => {
        
        loading.style.display = 'block';
        
        submitButton.disabled = true;

        
        form.addEventListener('reset', () => {
            loading.style.display = 'none';
            submitButton.disabled = false;
        });

        
        setTimeout(() => {
            loading.style.display = 'none';
            submitButton.disabled = false;
        }, 2000); 
    });
});
