document.addEventListener('DOMContentLoaded', () => {
  console.log('Dom Fully Loaded!');
  const modalForm = document.getElementById('modalForm'); // The modal element
  console.log('Modal Form', modalForm);
  const modalLoginForm = modalForm.querySelector('#modalLoginForm'); // The form in the modal
  console.log('Modal Login Form:', modalLoginForm);
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  const headers = {
    'X-CSRFToken': csrfToken
  };
  
  
  // Event listener for showing the modal and dynamically updating its content
  modalForm.addEventListener('show.bs.modal', async (event) => {
    
    const button = event.relatedTarget; // Button that triggered the modal
    console.log('Button:', button); // Log the button element
    const modalTitle = button.getAttribute('data-bs-title'); // Dynamic title
    const modalBody = button.getAttribute('data-bs-body'); // Dynamic body text
    const cancelBtn = button.getAttribute('data-bs-dismiss'); // Dynamic cancel button
    const confirmBtn = button.getAttribute('data-bs-confirm'); // Dynamic confirm button
    const confirmBtnColor = button.getAttribute('data-bs-confirm-color'); // Dynamic confirm button color
    console.log('Button data-bs-url:', button.getAttribute('data-bs-url'));
    const submitUrl = button.getAttribute('data-bs-url');
    console.log('data-bs-url:', button.getAttribute('data-bs-url')); // Log the URL
    console.log(submitUrl);
    
    // Update modal content dynamically
    const modalTitleElement = modalForm.querySelector('.modal-title');
    const modalCancelElement = modalForm.querySelector('.modal-cancel');
    const modalBodyElement = modalForm.querySelector('.modal-body');
    const modalConfirmElement = modalForm.querySelector('.modal-confirm');

    // Only update elements if they exist
    if (modalTitleElement) modalTitleElement.textContent = modalTitle;
    if (modalBodyElement) modalBodyElement.textContent = modalBody;
    if (modalCancelElement) modalCancelElement.textContent = cancelBtn;
    if (modalConfirmElement) modalConfirmElement.textContent = confirmBtn;
    if (modalConfirmElement) modalConfirmElement.className = `modal-confirm btn ${confirmBtnColor || 'btn-danger'}`;

      // Set the form's action dynamically (if needed)
      console.log('Retrieved submitUrl:', submitUrl); // First log to check the URL value
      if (submitUrl) {
        modalLoginForm.setAttribute('action', submitUrl); // Add action to the form
        console.log('Form action updated to:', modalLoginForm.getAttribute('action')); // Confirm the update
    }

    try {
      const response = await fetch(submitUrl, { method: "GET" });
      const data = await response.json();
      if (data.html) {
          const modalBody = modalForm.querySelector(".modal-body");
          modalBody.innerHTML = data.html;
      } else {
          console.error("No HTML received");
      }
      } catch (error) {
      console.error("Error fetching modal content:", error);
      }
    
  });

  // **AJAX Form Submission Logic** - This should be **outside** of the `show.bs.modal` event listener
  modalLoginForm.addEventListener('submit', async (event) => {
      event.preventDefault();  // Prevent normal form submission
      const modalLoginForm = modalForm.querySelector('form');
      const submitUrl = modalLoginForm.getAttribute('action');
      const formData = new FormData(modalLoginForm);

      try {
          const response = await fetch(submitUrl, {
              method: "POST",
              body: formData
          });

          const result = await response.json();
      if (result.success) {
        console.log('Login successful!');
        const modalInstance = bootstrap.Modal.getInstance(modalForm);
        modalInstance.hide(); // Close the modal on success
        alert('Logged in successfully!');
      } else {
        alert(result.message || 'Invalid credentials. Please try again.');
      }
    } catch (error) {
      console.error('Error submitting form:', error);
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



