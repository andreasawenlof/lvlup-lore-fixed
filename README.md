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
      - [**Project Goals**](#project-goals-1)
      - [**Planning and Project Management**](#planning-and-project-management)
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
    - [API Integration](#api-integration)
    - [Cloudinary API](#cloudinary-api)
    - [Testing](#testing)
  - [Setup and Deployment](#setup-and-deployment)
    - [Create Repository](#create-repository)
    - [Initialize in VS Code](#initialize-in-vs-code)
    - [Set Up Virtual Environments](#set-up-virtual-environments)
    - [Create Django Project](#create-django-project)
    - [Deployment to Github](#deployment-to-github)
    - [Deployment to Heroku](#deployment-to-heroku)

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

#### **Project Goals**
1. Build an engaging platform for gaming content.
2. Provide responsive tools for interaction (e.g., comments, profiles).
3. Enable efficient admin management of posts and user queries.

#### **Planning and Project Management**
This project was managed using Agile principles, focusing on iterative development and continuous improvement. A Kanban board was used to track progress and organize tasks effectively.

- **Kanban Board**:
  The Kanban board was structured with the following columns:
  - **To Do**: Tasks not yet started.
  - **In Progress**: Tasks currently being worked on.
  - **Completed**: Finished tasks.

  ![Kanban Board Screenshot Placeholder](path-to-image/kanban-board.png)

  View the live board here: [GitHub Project Board](https://github.com/yourusername/yourproject/projects/1).

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
![Roboto](static/images/readme-files/3a392fca77ce5bebf165216f7f5f30e4.png)

- **Press Start 2P**: Used for titles and headers to enhance visual hierarchy. The blockiness goes with a retro gamer feel.
![Press Start 2P](static/images/readme-files/0311fe69e98b0a1ade4305203e5d1d46.png)

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

1. **Edit Profile**:
   - Allow users to update their bio and upload a custom avatar.
   - Enable a more personalized user experience.
   - This feature would include form validation for safe and secure profile updates.
2. **Dark Mode**: Automatic and manual toggle for light/dark themes.
3. **Advanced Search**: Filter posts by content, category, or author.
4. **AJAX Integration**: Real-time updates for search results and comments.

</details>

---
### <a id="api-integration">API Integration</a>
### Cloudinary API

The project uses the [Cloudinary](https://cloudinary.com/) API for handling media files like images and videos. The API key is stored in `env.py` for security purposes.


### Testing

The site was tested for:
- Functionality, responsiveness, and browser compatibility.
- Accessibility using the Wave tool (no errors or warnings).
- Code quality using W3C validators (no HTML or CSS errors).
- Performance, accessibility, and SEO using Lighthouse (all scores above 90%).

Detailed results are available in the [TESTING.md](TESTING.md).



## <a id="setup-and-deployment">Setup and Deployment</a>
### <a id="create-repository">Create Repository</a>
Step-by-step guide on creating a new repository from the Gitpod Full Template by Code Institute.
<details>
<summary>Click to expand</summary>

**Log in to GitHub:**
1. Open your web browser and navigate to GitHub.
2. If you are not already logged in, enter your GitHub username and password to log in.

**Access the Gitpod Full Template:**
1. Go directly to the Gitpod Full Template repository.

**Create a New Repository Using the Template:**
1. On the template repository page, look for the green button that says "Use this template". Click on this button.
2. You will be redirected to the "Create a new repository from gitpod-full-template" page.

**Configure Your New Repository:**
1. Repository name: Enter a name for your new repository.
2. Repository description (optional): Provide a brief description of your repository.
3. Privacy settings: Choose whether the repository should be Public (anyone can see this repository) or Private (you choose who can see this repository).
4. Leave the "Include all branches" checkbox unchecked if you just need the main branch; check it if you need all branches from the template.

**Create the Repository from the Template:**
1. Click the "Create repository from template" button to create your new repository with the contents of the Gitpod Full Template.

**Access Your New Repository:**
1. Once the repository is created, you will be redirected to your new repository page on GitHub.

### <a id="initialize-in-vs-code">Initialize in VS Code</a>

Clone in VSCode:
1. Open VSCode.
2. Press Ctrl + Shift + P (Cmd + Shift + P on macOS) to open the Command Palette.
3. Type Git: Clone and select it.
4. Paste the repository URL and press Enter.
5. Select a directory to save the repository on your local machine.
6. After cloning, a prompt will ask if you want to open the cloned repository. Click “Open”.

</details>

### <a id="set-up-virtual-environments">Set Up Virtual Environments</a>
Requirements:
<details>
<summary>Click to expand</summary>

**1. Python 3.x installed on your system.**

**Steps:**

**1. Open Your Command Line Interface:** This could be Terminal on macOS/Linux or Command Prompt on Windows.
**2. Navigate to Your Project Directory:** Enter `cd path/to/your/project` to move into your project directory.
**3. Create the Virtual Environment:**
  - On Windows, type `python -m venv .venv`
  - On macOS or Linux, type `python3 -m venv .venv`
  This command creates a folder named `.venv` in your project directory containing the virtual environment.
**4. Activate the Virtual Environment:**
  - On Windows, type `.venv\Scripts\activate`
  - On macOS or Linux, type `source .venv/bin/activate`
  Activation changes the shell to use the environment’s settings and packages.
**5. Install Dependencies:**
  Once the environment is activated, install any required packages using `pip install package-name`.
**6. Capture Installed Dependencies:**
  To create a `requirements.txt` file that lists all installed packages, use `pip freeze > requirements.txt`. This file can then be used to install all necessary packages into another environment or shared with other developers.
**7. Deactivate the Virtual Environment:**
  When finished, you can deactivate the environment by typing `deactivate`.
  </details>

### <a id="create-django-project">Create Django Project</a>
Step-by-step guide on how to create a new Django project.
<details>
<summary>Click to expand</summary>

1. Install Django: Ensure you have Django installed on your system. If not, you can install it using pip:
  ```
  pip install django
  ```

2. Create a New Django Project: Use the django-admin command to create a new Django project. Replace `project_name` with the desired name for your project:
  ```
  django-admin startproject project_name
  ```

3. Navigate to the Project Directory: Change into the newly created project directory:
  ```
  cd project_name
  ```

4. Create a Virtual Environment (Optional): It's good practice to work within a virtual environment. You can create one using virtualenv:
  ```
  virtualenv venv
  ```

  Activate the virtual environment:
  - On Windows:
    ```
    venv\Scripts\activate
    ```
  - On Unix or MacOS:
    ```
    source venv/bin/activate
    ```

5. Initialize Git (Optional): If you're using version control with Git, initialize a new Git repository:
  ```
  git init
  ```

6. Create .gitignore File (Optional): Create a .gitignore file to specify which files and directories Git should ignore. Typically, this includes the `venv` directory, database files, and sensitive configuration files.

7. Set Up Environment Variables: Create an `env.py` file to store sensitive information like secret keys and API keys. Add this file to your `.gitignore` to prevent it from being pushed to your repository. An example `env.py` file might look like this:
  ```python
  import os

  os.environ.setdefault('SECRET_KEY', 'your_secret_key_here')
  os.environ.setdefault('DEBUG', 'True')
  ```

  Replace `'your_secret_key_here'` with a randomly generated secret key.

8. Configure Django Settings: Update the Django settings (`settings.py`) to use environment variables. For example, you can set the `SECRET_KEY` and `DEBUG` variables like this:
  ```python
  import os

  SECRET_KEY = os.environ.get('SECRET_KEY')
  DEBUG = os.environ.get('DEBUG') == 'True'
  ```

  Ensure to import `env` at the top of `settings.py` to load environment variables.

9. Run Migrations: If your project uses a database, apply initial migrations:
  ```
  python manage.py migrate
  ```

10. Start the Development Server: Finally, start the Django development server to verify that everything is set up correctly:
   ```
   python manage.py runserver
   ```

   Open a web browser and navigate to http://127.0.0.1:8000 to see your new Django project in action.

</details>


### <a id="deployment-to-github">Deployment to Github</a>

<details>
<summary>Click to expand</summary>
1. Add Files to Git: Navigate to your project directory in the terminal and add all your project files to the staging area by running:
  ```
  git add .
  ```

2. Commit Changes: Commit the staged files with a descriptive message to track changes. For example:
  ```
  git commit -m "Initial commit: Added Django project files"
  ```

3. Push to GitHub: Push your local repository to GitHub:
  ```
  git push
  ```
  </details>

### <a id="deployment-to-heroku">Deployment to Heroku</a>
<details>
<summary>Click to expand</summary>

The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - EMAIL_HOST_USER: (email address)
  - EMAIL_HOST_PASS: (email app password)
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy

The app should now be deployed.

 </details>
