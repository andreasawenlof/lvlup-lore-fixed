document.addEventListener('DOMContentLoaded', () => {
  const modalAuth = document.getElementById('modalAuth'); // The modal element
  const modalLoginForm = modalAuth.querySelector('#modalLoginForm'); // The form in the modal
  
    // Event listener for showing the modal and dynamically updating its content
    modalAuth.addEventListener('show.bs.modal', (event) => {
        event.preventDefault();
        const button = event.relatedTarget; // Button that triggered the modal
        const modalTitle = button.getAttribute('data-bs-title'); // Dynamic title
        const modalBody = button.getAttribute('data-bs-body'); // Dynamic body text
        const cancelBtn = button.getAttribute('data-bs-dismiss');//Dynamic cancel button
        const confirmBtn = button.getAttribute('data-bs-confirm');//Dynamic confirm button
        const confirmBtnColor = button.getAttribute('data-bs-confirm-color');
        const submitUrl = button.getAttribute('data-bs-url'); // Action URL

        // Update modal content dynamically
        const modalTitleElement = modalAuth.querySelector('.modal-title');
        const modalBodyElement = modalAuth.querySelector('.modal-body');
        const modalCancelElement = modalAuth.querySelector('.modal-cancel');
        const modalConfirmElement = modalAuth.querySelector('.modal-confirm');

        const modalFormSubmit = document.getElementById("authModalSubmit");
        const modalFormUser = document.getElementById("authModalUser");
        const modalFormPass = document.getElementById("authModalPass");
        

        

        if (modalTitle) modalTitleElement.textContent = modalTitle;
        if (modalBody) modalBodyElement.textContent = modalBody;
        if (cancelBtn) modalCancelElement.textContent = cancelBtn;
        if (confirmBtn) modalConfirmElement.textContent = confirmBtn;
        if (confirmBtn) modalConfirmElement.className = `modal-confirm btn ${confirmBtnColor || 'btn-danger'}`;

        // Set the form's action dynamically
        if (submitUrl) modalLoginForm.setAttribute('action', submitUrl);
    });

    
    // No changes are needed for the form submission.
    // The form will submit normally, and Django will handle the redirect and success message.

  modalLoginForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(modalLoginForm)
  
    const data = {
      username: formData.get('username'),
      password: formData.get('password')
    }
    try {
      console.log("Action URL: ", modalLoginForm.getAttribute('action'));
      const response = await fetch('/accounts/login/', {
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify(data)
      })
    
      const result = await response.json();
      if (result.success) {
        console.log("Login Successful")
        const modal = new bootstrap.Modal(document.getElementById('modalAuth'));
        modal.hide();  // Close the modal on success
      } else {
        alert(result.message);
    }} catch (error) {
      console.error('Error:', error)
    }
  });
});

// const fetchUserData = () => {
//     // Simulate a fetch request
//     return new Promise((resolve, reject) => {
//       const isSuccess = true;  // Toggle this to simulate success or failure
//       setTimeout(() => {
//         if (isSuccess) {
//           resolve({ name: "Jane Doe", age: 28 });
//         } else {
//           reject("Failed to fetch data.");
//         }
//       }, 2000);
//     });
//   };


// const fetchUserDataAsync = async () => {
//     const {name, age} = await fetchUserData();
    
//     try {
//             return `${name}, ${age}`;
//     }    
//     catch(error) {
//         console.error(error)
//     }
// }


// const fetchUserInfo = async () => {
//     try {
//         const response = await fetch('https://api.example.com/user');
//         const userData = await response.json();
        
//         // Now, log user info based on some condition:
//         if (userData.age > 18) {
//             return userData.posts;
//             // Do something for adults
//         } else {
//             window.alert("Grow up kid, you're not old enough yet!")
//             // Do something else for minors
//         }
//     } catch (error) {
//         console.error('Error fetching data:', error);
//     }
// };



