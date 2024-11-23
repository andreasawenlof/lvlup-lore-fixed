const editButtons = document.querySelectorAll(".btn-edit");
const commentForm = document.getElementById("commentForm");
const commentText = document.getElementById("id_body");
const submitButton = document.getElementById("submitButton");
const postSlug = commentForm.getAttribute("data-post-slug");

editButtons.forEach((button) => {
    button.addEventListener("click", () => {
        const commentId = button.getAttribute("data-comment-id");
        const commentBody = button.getAttribute("data-comment-body");

        // Populate the comment form with the comment's body
        commentText.value = commentBody;

        // Update the form's action to point to `edit_comment`
        commentForm.setAttribute(
            "action",
            `/post/${postSlug}/edit_comment/${commentId}/`
        );

        // Change the submit button text to "Update"
        submitButton.innerText = "Update";
    });
});
