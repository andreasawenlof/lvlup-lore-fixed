

// Confirm Delete Modal
document.addEventListener('DOMContentLoaded', () => {
    const modalConfirm = document.getElementById('modalConfirm'); // The modal element
    const modalConfirmForm = modalConfirm.querySelector('#modalConfirmForm'); // The form in the modal

    // Event listener for showing the modal and dynamically updating its content
    modalConfirm.addEventListener('show.bs.modal', (event) => {
        const button = event.relatedTarget; // Button that triggered the modal
        const modalTitle = button.getAttribute('data-bs-title'); // Dynamic title
        const modalBody = button.getAttribute('data-bs-body'); // Dynamic body text
        const cancelBtn = button.getAttribute('data-bs-dismiss');//Dynamic cancel button
        const confirmBtn = button.getAttribute('data-bs-confirm');//Dynamic confirm button
        const confirmBtnColor = button.getAttribute('data-bs-confirm-color');
        const confirmUrl = button.getAttribute('data-bs-url'); // Action URL

        // Update modal content dynamically
        const modalTitleElement = modalConfirm.querySelector('.modal-title');
        const modalBodyElement = modalConfirm.querySelector('.modal-body');
        const modalCancelElement = modalConfirm.querySelector('.modal-cancel');
        const modalConfirmElement = modalConfirm.querySelector('.modal-confirm');

        if (modalTitle) modalTitleElement.textContent = modalTitle;
        if (modalBody) modalBodyElement.textContent = modalBody;
        if (cancelBtn) modalCancelElement.textContent = cancelBtn;
        if (confirmBtn) modalConfirmElement.textContent = confirmBtn;
        if (confirmBtn) modalConfirmElement.className = `modal-confirm btn ${confirmBtnColor || 'btn-danger'}`;

        // Set the form's action dynamically
        if (confirmUrl) modalConfirmForm.setAttribute('action', confirmUrl);
    });

    // No changes are needed for the form submission.
    // The form will submit normally, and Django will handle the redirect and success message.
});


// // Profile Edit Modal
// const modal = document.getElementById("profileEditModal");
// const btn = document.getElementById("myBtn");

// const span = document.getElementsByClassName("close")[0];

// btn.onclick = function() {
//     modal.style.display = "block";
// }

// span.onclick = function() {
//     modal.style.display = "none";
// }

// window.onclick = function(event) {
//     if (event.target == modal) {
//         modal.style.display = "none";
//     }
// }