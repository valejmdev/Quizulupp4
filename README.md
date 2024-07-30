# Quizulu

## Introduction

Welcome to **Quizulu**, an engaging and interactive quiz game where you can test your knowledge across various categories! This application invites you to enter a username, select a quiz category, and answer a series of multiple-choice questions. It's a fun way to challenge yourself and learn new facts while competing for high scores.

This project was created as part of Code Institute's Full Stack Software Development Diploma, demonstrating a comprehensive integration of Python, the Open Trivia API, Google Sheets API, and web development techniques.

## Table of Contents

- [User Experience](#user-experience)
  - [User Benefits](#user-benefits)
  - [Persona](#persona)
  - [User Journey](#user-journey)
  - [Program Flowchart](#program-flowchart)
- [Features](#features)
  - [Username Validation](#username-validation)
  - [Category Selection](#category-selection)
  - [Question Generation](#question-generation)
  - [Interactive Gameplay](#interactive-gameplay)
  - [Scoring System](#scoring-system)
  - [Leaderboard](#leaderboard)
  - [Game Options](#game-options)
  - [User Feedback](#user-feedback)
  - [Loading Animation](#loading-animation)
- [Technologies Used](#technologies-used)
- [Data Storage](#data-storage)
- [Python Packages Used](#python-packages-used)
- [Testing](#testing)
  - [Python PEP8 Validation](#python-pep8-validation)
  - [Development Bugs](#development-bugs)
- [Deployment](#deployment)
  - [Deploying the App](#deploying-the-app)
  - [Forking the Repository](#forking-the-repository)
  - [Cloning the Repository](#cloning-the-repository)
  - [APIs](#apis)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## User Experience

### User Benefits

## Persona: Alex Johnson

### Demographic Information

- **Age:** 28
- **Gender:** Male
- **Location:** Berlin, Germany
- **Occupation:** Software Developer
- **Education:** Bachelor's Degree in Computer Science
- **Income:** $85,000/year
- **Marital Status:** Single
- **Technology Usage:** Heavy (frequent user of computers, smartphones, tablets, and smart home devices)

### Psychographic Information

- **Interests:**
    - Passionate about technology and programming
    - Enjoys learning new things and staying intellectually challenged
    - Loves participating in trivia nights and quiz competitions
    - Enthusiast of pop culture, including movies, TV shows, and video games
    - Avid reader of science fiction and fantasy novels
    - Listens to a diverse range of music, from classical to electro
- **Hobbies:**
    - Playing video games (both casual and competitive)
    - Attending local trivia nights with friends
    - Exploring new coding projects and contributing to open-source communities
    - Watching documentaries and learning about history and science
    - Participating in online forums and social media discussions about favorite shows and books
- **Values:**
    - Lifelong learning and continuous self-improvement
    - Community and social connections, both online and offline
    - Creativity and innovation in both personal and professional life
    - Fun and entertainment as essential parts of a balanced life

### Behavioral Information

- **Internet Usage:**
    - Spends significant time online daily for both work and leisure
    - Frequently visits websites related to technology, gaming, and pop culture
    - Actively participates in online trivia and quiz platforms
- **Preferred Websites:**
    - Stack Overflow for programming help
    - Reddit for discussions on various topics
    - IMDb and Rotten Tomatoes for movie and TV show reviews
    - Sporcle and Kahoot! for online quizzes and trivia games
    - Spotify for music streaming
- **Motivations for Using the Trivia Game Website:**
    - Desire to challenge themselves and improve their knowledge in various subjects
    - Interest in creating and sharing their own quizzes with the community
    - Enjoyment of competing with friends and other users to achieve high scores
    - Opportunity to explore and learn about new topics in a fun and engaging way
- **Goals:**
    - To become a top scorer in various trivia categories
    - To create popular and challenging quizzes that other users enjoy
    - To use the website as a fun way to relax and unwind after work
    - To connect with other trivia enthusiasts and expand their social circle

### Scenario

Alex Johnson is sitting at their favorite coffee shop on a Saturday afternoon, browsing through their tablet. After catching up on the latest tech news and Reddit discussions, Alex decides they want to take a break and do something fun but intellectually stimulating. They remember the Trivia Game website they recently discovered and decide to log in.

Upon logging in, Alex is greeted by their personalized dashboard showing their high scores and quizzes they've created. Feeling competitive, Alex chooses to play a multiple-choice quiz in the "Video Games" category. After enjoying the quiz and scoring high, they decide to create a new quiz on "Cybersecurity," a topic they are passionate about.

Alex spends the next hour crafting challenging questions and perfecting the quiz. Satisfied with their creation, they publish it and share the link on their social media, inviting friends to try it out. Before leaving the coffee shop, Alex checks their dashboard once more, smiling at the thought of all the fun and learning ahead.

### User Journey

### Program Flowchart

## Features

### User Registration and Login
- **Register**: Allows new users to create an account with a username and password.
- **Login**: Authenticates users and provides access to the application.

### User Profile
- **Profile Management**: Users can view and update their profile information.
- **Delete Profile**: Users have the option to delete their profile, which will remove their account from the application.

### Quiz Management
- **Create Quiz**: Logged-in users can create new quizzes and set up questions for them.
- **Update Quiz**: Users can edit existing quizzes they have created.
- **Delete Quiz**: Users can delete quizzes they have created.
- **Quiz Detail**: View details of a specific quiz including its title, description, and questions.

### Question Management
- **Create Question**: Add new questions to a quiz they create.

### Quiz Participation
- **Play Quiz**: Users can take quizzes by answering questions. The application keeps track of their progress and scores.
- **Quiz Results**: After completing a quiz, users can view their results and see their scores.

### Categories and Random Quiz
- **List Categories**: Display all available quiz categories.
- **Random Quiz**: Redirect users to a random quiz from a specified category.

### Leaderboard
- **Leaderboard**: Shows the top 10 users based on their total quiz scores.

