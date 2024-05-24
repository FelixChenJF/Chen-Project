document.addEventListener('DOMContentLoaded', function() {
    const listItems = document.querySelectorAll('.left-column li');
    const labels = document.querySelectorAll('.label-group .label-item');

    listItems.forEach(item => {
        item.addEventListener('click', function() {
            const selectedTitle = this.getAttribute('data-title');

            labels.forEach(label => {
                label.style.display = 'none';
            });

            labels.forEach(label => {
                if (label.getAttribute('data-foreign-key') === selectedTitle) {
                    label.style.display = 'inline';
                }
            });
        });
    });
});