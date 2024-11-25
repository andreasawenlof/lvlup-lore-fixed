# LVL-UP Lore

Welcome to **LVL-UP Lore**, a gaming blog where admins can share gaming-related posts, and users can engage through comments. This project emphasizes delivering core functionality with a clean, responsive interface. The platform fosters open discussions while ensuring respectful interactions.

![Homepage Screenshot Placeholder](path-to-image/homepage.png)

---

## Table of Contents

- [LVL-UP Lore](#lvl-up-lore)
  - [Table of Contents](#table-of-contents)
  - [Purpose and Demographic](#purpose-and-demographic)
  - [UX Design](#ux-design)
    - [The Strategy](#the-strategy)
      - [**Project Goals**](#project-goals)
      - [**User Stories**](#user-stories)
    - [The Scope](#the-scope)
      - [**Features Included**](#features-included)
      - [**Features Excluded**](#features-excluded)
    - [The Skeleton (Wireframes)](#the-skeleton-wireframes)
  - [Features](#features)
    - [Header Navigation](#header-navigation)
    - [Search Bar](#search-bar)
  - [Design Choices](#design-choices)
    - [**Typography**](#typography)
    - [**Color Scheme**](#color-scheme)
    - [**Interactive Elements**](#interactive-elements)
  - [Database Design](#database-design)
    - [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
  - [Future Features](#future-features)
  - [Deployment](#deployment)

---

## Purpose and Demographic

**LVL-UP Lore** is designed for:
- **Gaming enthusiasts** who want to stay updated on gaming trends.
- **Users** who want to express their opinions freely while adhering to respectful interactions.
- **Admins** or **content creators** who require easy-to-use tools for managing blog posts and moderating user activity.

![Target Audience Screenshot Placeholder](path-to-image/target-audience.png)

---

## UX Design

### The Strategy

<details>
<summary>Click to expand</summary>

#### **Project Goals**
1. Build a platform where users can access gaming-related posts and interact with them.
2. Provide admins with tools for managing content effectively, including posts, comments, and feedback.
3. Deliver a responsive, visually appealing site for users across all devices.

#### **User Stories**
- **As a user**, I want to:
  - Browse gaming-related posts.
  - Comment on posts and edit or delete my own comments.
  - Search for posts based on their titles.
  - View user profiles, including my own.
- **As an admin**, I want to:
  - Create, edit, publish, or delete posts.
  - Moderate user comments and manage drafts.
  - Review and respond to inquiries from the contact form.

</details>

---

### The Scope

<details>
<summary>Click to expand</summary>

#### **Features Included**
1. **Header Navigation**:
   - Role-based links for guests, logged-in users, and admins.
   - Links include: Home, Profile, Login, Logout, and Contact Us.

2. **CRUD Operations**:
   - Admins can create, edit, delete, and manage drafts of posts.

3. **Comments**:
   - Users can add, edit, and delete their own comments.

4. **Profiles**:
   - User profiles include bio and activity (e.g., posts they’ve commented on). Users can check other profiles.

5. **Search Bar**:
   - Users can search for posts by title, with instant results.

6. **Contact Form**:
   - Users can send inquiries directly to admins.

7. **Responsiveness**:
   - Fully functional on desktop, tablet, and mobile.

#### **Features Excluded**
1. Advanced search (e.g., by category, author, or post content).
2. Dark mode (planned for future implementation).
3. AJAX functionality for real-time search and comment updates.

</details>

---

### The Skeleton (Wireframes)

<details>
<summary>Click to expand</summary>

- **Homepage Wireframe**:
  - Features a hero section and a list of posts in card format.
  - Cards display the post title, image, excerpt, and author details.
  - Includes a navigation bar and a search bar.

![Homepage Wireframe Placeholder](path-to-image/homepage-wireframe.png)

- **Post Detail Page**:
  - Displays the full post and includes a comment section.
  - Comments can be added, edited, or deleted.

![Post Detail Page Wireframe Placeholder](path-to-image/post-detail-wireframe.png)

- **Profile Page Wireframe**:
  - Displays the user’s avatar, bio, and list of interactions (e.g., list of posts that has been commented on).

![Profile Page Wireframe Placeholder](path-to-image/profile-wireframe.png)

</details>

---

## Features

### Header Navigation

- **Dynamic Navigation**:
  - Guest: Home, Sign Up, Log In, Contact Us.
  - Logged-In User: Automatic generated Profile and appeared Logout links.
  - Admin: Adds Create Post, Drafts, and Contact Messages in a drowdown.

![Header Navigation Screenshot Placeholder](path-to-image/header-navigation.png)

---

### Search Bar

<details>
<summary>Click to expand</summary>

- **Functionality**:
  - Allows users to search for posts by title.
  - Displays "No results found" if no matches exist.
  - Returns all posts for an empty search query.

![Search Bar Screenshot Placeholder](path-to-image/search-bar.png)

</details>

---

## Design Choices

<details>
<summary>Click to expand</summary>

### **Typography**
- **Roboto**: Used for body text for readability.
- **Press Start 2P**: Used for titles and headers to enhance visual hierarchy. The blockiness goes with a retro gamer feel.

### **Color Scheme**

- **Primary Colors**: Neutral tones for backgrounds and text.
- **Accent Colors**: Green highlights for buttons and links.

### **Interactive Elements**
- Hover effects on buttons and links.
- Smooth transitions for modals (e.g., confirmations).

![Design Choices Placeholder](path-to-image/design-choices.png)

</details>

## Database Design

### Entity Relationship Diagram (ERD)

<details>
<summary>Click to expand</summary>

The database includes:
1. **User**: Manages authentication and user details.
2. **Post**: Contains all blog post data.
3. **Comment**: Tracks user comments and links them to posts.
4. **Profile**: Stores user bios and avatars.

![ERD Placeholder](path-to-image/erd.png)

</details>

---

## Future Features

<details>
<summary>Click to expand</summary>

1. **Dark Mode**: Automatic and manual toggle for light/dark themes.
2. **Advanced Search**: Filter posts by content, category, or author.
3. **AJAX Integration**: Real-time updates for search results and comments.

</details>

---

## Deployment

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lvl-up-lore.git
