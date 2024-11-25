# Testing Documentation

## Manual Testing

### Core Features

#### **Feature: CRUD Operations**
| Action               | Role         | Expected Result                       | Test Result |
|----------------------|--------------|---------------------------------------|-------------|
| Create Post          | Admin        | Post is successfully created.         | Passed      |
| Edit Post            | Admin        | Changes are saved and reflected.      | Passed      |
| Delete Post          | Admin        | Post is removed from the database.    | Passed      |
| Add Comment          | User         | Comment appears on the post.          | Passed      |
| Edit Comment         | User         | Comment updates are reflected.        | Passed      |
| Delete Comment       | User         | Comment is successfully removed.      | Passed      |

---

#### **Feature: Navigation**
| User Role  | Visible Links                           | Test Result |
|------------|-----------------------------------------|-------------|
| Guest      | Home, Sign Up, Log In, Contact Us       | Passed      |
| Logged-In  | Home, Profile, Logout, Contact Us       | Passed      |
| Admin      | Home, Create Post, Drafts, Admin Panel  | Passed      |

---

#### **Feature: Search Bar**
| Query Input       | Expected Output                  | Test Result |
|-------------------|----------------------------------|-------------|
| Valid Title       | Matching posts displayed.        | Passed      |
| Invalid Query     | "No results found" message shown.| Passed      |
| Empty Query       | All posts displayed.             | Passed      |

---

#### **Feature: Contact Form**
| Input Fields         | Expected Output                          | Test Result |
|----------------------|------------------------------------------|-------------|
| Valid Inputs         | "Message sent" success message displayed.| Passed      |
| Missing Required Data| Error message displayed.                 | Passed      |

---

### Responsiveness

#### Devices Tested:
- **Desktop**: Chrome, Firefox, Safari
- **Mobile**: iPhone X (Safari)

| Device    | Resolution  | Observations                  | Test Result |
|-----------|-------------|-------------------------------|-------------|
| Desktop   | 1920x1080   | Layout looks consistent.      | Passed      |
| Tablet    | 768x1024    | Navigation adapts properly.   | Passed      |
| Mobile    | 375x812 (iPhone X) | All content is readable. | Passed      |
| Mobile    | 390x844 (iPhone 12 Pro) | All content is readable. | Passed      |

---

### Browser Compatibility

| Browser   | Version | Test Result |
|-----------|---------|-------------|
| Chrome    | v114+   | Passed      |
| Firefox   | v102+   | Passed      |
| Safari    | iOS     | Passed      |
| Edge      | v100+   | Passed      |

---

### Lighthouse Testing

The following pages were tested with Lighthouse for performance, accessibility, best practices, and SEO:

| Page             | Performance | Accessibility | Best Practices | SEO  |
|-------------------|-------------|----------------|----------------|------|
| Homepage          | 72%         | 85%            | 80%            | 65%  |
| Post Detail Page  | 78%         | 88%            | 82%            | 70%  |
| Contact Page      | 75%         | 90%            | 85%            | 68%  |

#### Observations
1. **Performance**: Scores were impacted by unoptimized images and lack of caching.
2. **Accessibility**: Minor contrast issues were identified and will be addressed in future iterations.
3. **Best Practices**: Warnings were caused by third-party scripts.
4. **SEO**: Missing structured data and meta descriptions lowered the SEO scores.

### W3C Validation

W3C validation was performed on the following pages:
- Homepage
- Post Detail Page
- Contact Us Page

#### Validation Results
The validation flagged similar non-critical issues across all pages:

| Issue                          | Cause                                                                                  | Impact                     |
|--------------------------------|----------------------------------------------------------------------------------------|---------------------------|
| Trailing slashes on void tags  | Tags like `<meta>` and `<link>` include a trailing slash for XHTML compatibility.       | No impact on functionality. |
| Missing `<p>` tags in scope    | Caused by dynamic Django template logic producing unmatched `</p>` tags in rare cases. | Does not affect rendering or usability. |

#### Observations
- These issues are consistent across the site due to shared templates (e.g., `base.html`) and reusable components.
- All other aspects of the HTML passed validation without errors.

#### Planned Fixes
1. **Trailing Slashes**: Will be removed in future updates to comply strictly with HTML5 standards.
2. **Unmatched Tags**: Template logic will be reviewed and refined to ensure all HTML tags are properly paired.

---

While this issue is acknowledged, it is considered **non-critical** for this project’s current state and submission timeline. Future updates will address the error to ensure full compliance with W3C standards.


Planned improvements include:
- Implementing lazy loading for images.
- Adding structured data for better SEO.
- Enhancing color contrast and adding ARIA labels where needed.


## Knows Bugs
The only thing (not sure i would call it a bug) is that success message doesn't work on delete because of the modal and I can't seem to be able to figure it out. 

---

## Summary
- All core features have been tested and work as expected.
- Known bugs are documented for future fixes.
- The site is responsive across all tested devices and browsers.
