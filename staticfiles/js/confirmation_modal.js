document.addEventListener('DOMContentLoaded', () => {
    const staticBackdrop = document.getElementById('staticBackdrop');
    staticBackdrop.addEventListener('show.bs.modal', (event) => {
        const button = event.relatedTarget;
        const modalTitle = button.getAttribute('data-bs-title');
        const modalBody = button.getAttribute('data-bs-body');
        const confirmUrl = button.getAttribute('data-bs-url');

        const modalTitleElement = staticBackdrop.querySelector('.modal-title');
        const modalBodyElement = staticBackdrop.querySelector('.modal-body');
        const deleteForm = staticBackdrop.querySelector('#deleteForm');

        modalTitleElement.textContent = modalTitle;
        modalBodyElement.textContent = modalBody;
        deleteForm.setAttribute('action', confirmUrl);
    });
});