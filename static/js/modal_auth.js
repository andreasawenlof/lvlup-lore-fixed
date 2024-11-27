document.addEventListener('DOMContentLoaded', () => {
    const modalAuth = document.getElementById('modalAuth'); // The modal element
    const modalAuthForm = modalAuth.querySelector('#modalAuthForm'); // The form in the modal

    modalAuth.addEventListener('show.bs.modal', (event) => {
        const button = event.relatedTarget; // Button that triggered the modal
        const modalTitle = button.getAttribute('data-bs-title');
        const modalBody = button.getAttribute('data-bs-body');
        const cancelBtn = button.getAttribute('data-bs-cancel');
        const formType = button.getAttribute('data-bs-form_type');
        const confirmBtn = button.getAttribute('data-bs-confirm');
        const confirmBtnColor = button.getAttribute('data-bs-confirm-color');
        const authUrl = button.getAttribute('data-bs-url');

        // Modal elements
        const modalTitleElement = modalAuth.querySelector('.modal-title');
        const modalBodyElement = modalAuth.querySelector('.modal-body'); // Update text within the paragraph
        const modalFormTypeElement = modalAuth.querySelector('.modal-form_type');
        const modalCancelElement = modalAuth.querySelector('.modal-cancel');
        const modalConfirmElement = modalAuth.querySelector('.modal-confirm');

        // Update modal elements dynamically
        if (modalTitle) modalTitleElement.textContent = modalTitle;
        if (modalBody) modalBodyElement.textContent = modalBody;
        if (formType) modalFormTypeElement.textContent = formType;
        if (cancelBtn) modalCancelElement.textContent = cancelBtn;
        if (confirmBtn) modalConfirmElement.textContent = confirmBtn;
        modalConfirmElement.className = `modal-confirm btn ${confirmBtnColor || 'btn-primary'}`;

        // Update form action dynamically
        if (authUrl) modalAuthForm.setAttribute('action', authUrl);
    });
});
