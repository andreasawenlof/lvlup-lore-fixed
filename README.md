# LVL-UP Lore

## Live Project

The live project can be viewed here: [LVL-UP Lore](https://lvlup-lore-627e6743039a.herokuapp.com/)

![AM-I-Responsive](static/images/readme-files/am-i-responsive.png)

Welcome to **LVL-UP Lore**, a gaming blog where admins can share gaming-related posts, and users can engage through comments. This project emphasizes delivering core functionality with a clean, responsive interface. The platform fosters open discussions while ensuring respectful interactions.

---

## Table of Contents

- [LVL-UP Lore](#lvl-up-lore)
  - [Live Project](#live-project)
  - [Table of Contents](#table-of-contents)
  - [Purpose and Demographic](#purpose-and-demographic)
  - [UX Design](#ux-design)
    - [The Strategy](#the-strategy)
      - [Project Goals](#project-goals)
    - [Assignment Requirements](#assignment-requirements)
    - [Planning and Project Management](#planning-and-project-management)
    - [User Stories](#user-stories)
      - [For Users](#for-users)
      - [For Admins](#for-admins)
    - [The Scope](#the-scope)
      - [Features Included](#features-included)
      - [Features Excluded](#features-excluded)
  - [Features](#features)
    - [Header Navigation](#header-navigation)
    - [Search Bar](#search-bar)
  - [Design Choices](#design-choices)
      - [Typography](#typography)
      - [Color Scheme](#color-scheme)
  - [Database Design](#database-design)
    - [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
  - [Future Features](#future-features)
  - [Testing](#testing)
  - [Setup and Deployment](#setup-and-deployment)
    - [Create Repository](#create-repository)
    - [Deployment to Heroku](#deployment-to-heroku)
  - [Acknowledgments](#acknowledgments)

---

## Purpose and Demographic

**LVL-UP Lore** is designed for:
- **Gaming enthusiasts** who want to stay updated on gaming trends.
- **Users** who want to express their opinions freely while adhering to respectful interactions.
- **Admins** or **content creators** who require easy-to-use tools for managing blog posts and moderating user activity.
---

## UX Design

### The Strategy

<details>
<summary>Click to expand</summary>

#### Project Goals
1. Build a platform where users can access gaming-related posts and interact with them.
2. Provide admins with tools for managing content effectively, including posts, comments, and feedback.
3. Deliver a responsive, visually appealing site for users across all devices.

</details>

---

### Assignment Requirements

<details>
<summary>Click to expand</summary>

1. **Functionality**: Create a fully functional web application where users can post and comment on blogs.
2. **User Authentication**: Implement secure user registration and login capabilities.
3. **Database Management**: Use Django ORM to handle data storage for posts, comments, and user profiles.
4. **Responsive Design**: Ensure the website adapts seamlessly to different screen sizes.
5. **User Interface**: Build a clean, user-friendly interface with Bootstrap.
6. **Testing and Accessibility**: Validate the code, ensure accessibility, and conduct thorough testing.
7. **Documentation**: Provide clear project documentation.

</details>

---

### Planning and Project Management

<details>
<summary>Click to expand</summary>

This project followed Agile principles. Tasks were managed with a Kanban board:

- **To Do**: Tasks not yet started.
- **In Progress**: Tasks currently being worked on.
- **Completed**: Finished tasks.

![Kanban Board Screenshot](static/images/readme-files/kanban-board.png)

View the board here: [GitHub Project Board](https://github.com/users/andreasawenlof/projects/5).

</details>

---

### User Stories

<details>
<summary>Click to expand</summary>

#### For Users
1. Browse gaming-related posts.
2. Comment on posts and edit or delete their own comments.
3. Search for posts by title.
4. View user profiles.

#### For Admins
1. Create, edit, and delete posts.
2. Moderate user comments.
3. Respond to inquiries via the contact form.

</details>

---

### The Scope

<details>
<summary>Click to expand</summary>

#### Features Included
1. **Dynamic Navigation** based on user role (guest, logged-in user, or admin).
2. **CRUD Operations** for comments and posts.
3. **User Profiles** with bio and activity tracking.
4. **Search Bar** for post titles.
5. **Contact Form** for inquiries.
6. **Responsive Design** via Bootstrap.

#### Features Excluded
1. Dark mode (planned for future updates).
2. AJAX for real-time updates.
3. Advanced search functionality.

</details>

---

## Features

### Header Navigation

![Header Navigation Screenshot](static/images/readme-files/header.png)
![Header Navigation for Guests](static/images/readme-files/header-not-logged-in.png)
![Header Navigation for Users](static/images/readme-files/header-logged-no-staff.png)

### Search Bar

<details>
<summary>Click to expand</summary>

![Search Bar Screenshot](static/images/readme-files/search-bar.png)
![Search Bar No Results Screenshot](static/images/readme-files/search-no-found.png)

</details>

---

## Design Choices

<details>
<summary>Click to expand</summary>

#### Typography
- **Roboto** for readability.
  ![Roboto Font Screenshot](static/images/readme-files/main-font.png)
- **Press Start 2P** for a retro gaming vibe.
  ![Press Start 2P Font Screenshot](static/images/readme-files/title-font.png)

#### Color Scheme
- Neutral tones for backgrounds.
- Accent green for buttons and links.
  ![Color Palette Screenshot](static/images/readme-files/palette.png)

</details>

---

## Database Design

### Entity Relationship Diagram (ERD)

<details>
<summary>Click to expand</summary>

The database includes:
1. **User**: Handles authentication.
2. **Post**: Stores blog content.
3. **Comment**: Tracks user interactions.
4. **Profile**: Manages user-specific data.

</details>

---

## Future Features

<details>
<summary>Click to expand</summary>

1. **Profile Editing**.
2. **Dark Mode**.
3. **Advanced Search**.
4. **AJAX for Real-Time Updates**.


</details>

---

## Testing

The site was tested for functionality, responsiveness, and browser compatibility. Detailed results are available in the [TESTING.md](TESTING.md).


---

## Setup and Deployment

### Create Repository

<details>
<summary>Click to expand</summary>

1. Log in to GitHub.
2. Create a new repository from the Gitpod Full Template.
3. Push code to GitHub.

</details>

---

### Deployment to Heroku

<details>
<summary>Click to expand</summary>

1. Set up Heroku with your application.
2. Add necessary environment variables (e.g., `SECRET_KEY`, `DATABASE_URL`).
3. Deploy via GitHub integration.


</details>

---

## Acknowledgments

- **Mentor**: Gareth for the invaluable guidance.
- **Swedish Slack Community**: For consistent support.
- **Family**: For their understanding and encouragement.

---
