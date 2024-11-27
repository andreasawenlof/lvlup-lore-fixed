document.addEventListener('DOMContentLoaded', () => {
    const modalForm = document.getElementById('modalForm'); // The modal element
    const modalFormForm = modalForm.querySelector('#modalFormForm'); // The form in the modal

    modalForm.addEventListener('show.bs.modal', (event) => {
        const button = event.relatedTarget; // Button that triggered the modal
        const modalTitle = button.getAttribute('data-bs-title') || 'Default Title';
        const modalBody = button.getAttribute('data-bs-body') || 'Default body text.';
        const cancelBtn = button.getAttribute('data-bs-cancel') || 'Cancel';
        const confirmBtn = button.getAttribute('data-bs-confirm') || 'Confirm';
        const confirmBtnColor = button.getAttribute('data-bs-confirm-color') || 'btn-danger';
        const formUrl = button.getAttribute('data-bs-url');

        const modalTitleElement = modalForm.querySelector('.modal-title');
        const modalBodyElement = modalForm.querySelector('.modal-body');
        const modalCancelElement = modalForm.querySelector('.modal-cancel');
        const modalConfirmElement = modalForm.querySelector('.modal-confirm');

        modalTitleElement.textContent = modalTitle;
        modalBodyElement.textContent = modalBody;
        modalCancelElement.textContent = cancelBtn;
        modalConfirmElement.textContent = confirmBtn;
        modalConfirmElement.className = `modal-confirm btn ${confirmBtnColor}`;

        if (formUrl) modalFormForm.setAttribute('action', formUrl);
    });
});
