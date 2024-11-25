## Testing

<details>
<summary>Click to expand</summary>

### Manual Testing
- Verified CRUD functionality for posts and comments.
- Tested navigation based on user roles (guest, logged-in user, admin).
- Checked success/error messages for all form submissions.

### Bugs Fixed
- Resolved an issue where Django messages failed to display after actions triggered by modals.
- Fixed a bug in the search bar where empty queries did not return all posts.

### Remaining Bugs
- Success messages triggered by modal confirmations are not displaying reliably.
  - This is due to limitations in message handling with form submissions via modals.

### Responsiveness
- Tested on:
  - Desktop: Various screen resolutions (e.g., 1920x1080, 1366x768).
  - Tablet: iPad, Samsung Galaxy Tab.
  - Mobile: iPhone 12, Galaxy S21.

### Browser Compatibility
- Fully functional on:
  - Chrome (Version 114+)
  - Firefox (Version 102+)
  - Safari (macOS and iOS)
  - Edge (Version 100+)

</details>
