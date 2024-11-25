document.addEventListener('DOMContentLoaded', () => {
    const staticBackdrop = document.getElementById('staticBackdrop'); // The modal element
    const deleteForm = staticBackdrop.querySelector('#deleteForm'); // The form in the modal

    // Event listener for showing the modal and dynamically updating its content
    staticBackdrop.addEventListener('show.bs.modal', (event) => {
        const button = event.relatedTarget; // Button that triggered the modal
        const modalTitle = button.getAttribute('data-bs-title'); // Dynamic title
        const modalBody = button.getAttribute('data-bs-body'); // Dynamic body text
        const confirmUrl = button.getAttribute('data-bs-url'); // Action URL

        // Update modal content dynamically
        const modalTitleElement = staticBackdrop.querySelector('.modal-title');
        const modalBodyElement = staticBackdrop.querySelector('.modal-body');

        modalTitleElement.textContent = modalTitle;
        modalBodyElement.textContent = modalBody;

        // Set the form's action dynamically
        deleteForm.setAttribute('action', confirmUrl);
    });

    // No changes are needed for the form submission.
    // The form will submit normally, and Django will handle the redirect and success message.
});
