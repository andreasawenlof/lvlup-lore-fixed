document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.querySelectorAll(".btn-edit");
    const commentForm = document.getElementById("commentForm");
    const commentText = document.getElementById("id_body");
    const submitButton = document.getElementById("submitButton");
    const editCommentIdField = document.getElementById("editCommentIdField");

    editButtons.forEach(button => {
        button.addEventListener("click", function() {
            const commentId = this.getAttribute("data-comment-id");
            const commentBody = this.getAttribute("data-comment-body");

            // Populate the form fields
            commentText.value = commentBody;
            editCommentIdField.value = commentId;

            // Update the form action to the edit URL
            commentForm.setAttribute("action", `/comment/${commentId}/edit/`);

            // Scroll to the form for better UX
            commentForm.scrollIntoView({ behavior: "smooth" });

            console.log(`Editing comment ${commentId}`);
        });
    });

    // Handle form submission via AJAX
    commentForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const formData = new FormData(this);
        const url = this.action;

        console.log(`Submitting form to ${url}`);

        fetch(url, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                const commentId = editCommentIdField.value;
                const commentDiv = document.getElementById(`comment${commentId}`);
                commentDiv.innerText = data.body;
                submitButton.textContent = "Submit";
                commentForm.reset();
                editCommentIdField.value = "";
                console.log(`Comment ${commentId} updated successfully`);
            } else {
                alert('Error updating comment');
                console.log('Error updating comment:', data);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while updating the comment.');
        });
    });
});