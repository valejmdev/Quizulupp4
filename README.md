# Quizulu

## Introduction

Welcome to **Quizulu**, an engaging and interactive quiz game where you can test your knowledge across various categories! This application invites you to enter a username, select a quiz category, and answer a series of multiple-choice questions. It's a fun way to challenge yourself and learn new facts while competing for high scores.

This project was created as part of Code Institute's Full Stack Software Development Diploma, demonstrating a comprehensive integration of Python, the Open Trivia API, Google Sheets API, and web development techniques.

## Table of Contents

- [User Experience](#user-experience)
  - [User Benefits](#user-benefits)
  - [Persona](#persona)
  - [Program Flowchart](#program-flowchart)
- [Features](#features)
  - [User Registration and Login](#user-registration-and-login)
  - [User Profile](#user-profile)
  - [Quiz Management](#quiz-management)
  - [Question Creation](#question-creation)
  - [Categories and Random Quiz](#categories-and-random-quiz)
  - [Leaderboard](#leaderboard)
  - [Initial Data Population Script](#initial-data-population-script)
- [Technologies Used](#technologies-used)
- [Data Storage](#data-storage)
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

## User Benefits

### Engaging Entertainment
- **Interactive Gameplay**: Enjoy a dynamic and interactive quiz game that challenges your knowledge across various topics.
- **Variety of Quizzes**: Experience the thrill of answering questions from a wide range of categories and topics.

### Educational Value
- **Expand Knowledge**: Learn new facts and information while playing quizzes on different subjects.
- **Skill Improvement**: Enhance your general knowledge and cognitive skills through regular quiz participation.

### Social Interaction
- **Compete with Others**: Challenge friends and other users by comparing scores on the global leaderboard.
- **Community Engagement**: Join a community of quiz enthusiasts and engage in friendly competition.

### Real-time Information
- **Instant Feedback**: Receive immediate feedback on your answers to help you learn and improve.
- **Up-to-date Content**: Access a constantly updated library of quizzes with current and relevant questions.

### User-friendly Experience
- **Easy Navigation**: Enjoy a seamless and intuitive interface designed for effortless navigation and usage.
- **Quick Start**: Get started quickly with clear instructions and user-friendly prompts.

### Motivation and Rewards
- **Score Tracking**: Keep track of your quiz performance and see your progress over time.
- **Leaderboard Recognition**: Strive for high scores and achieve recognition by climbing the leaderboard.

### Personalization
- **User Profiles**: Create and manage your personal profile, customize your experience, and track your quiz history.
- **Profile Management**: Update your profile information easily and keep your account details up-to-date.

### Quiz Management
- **Create Your Own Quizzes**: Design and publish your own quizzes, share them with others, and challenge friends.
- **Edit and Update**: Modify existing quizzes to keep them accurate and engaging.

### Accessibility
- **Multi-Device Compatibility**: Play on various devices, including smartphones, tablets, and computers.
- **Anywhere, Anytime**: Easily access the game from anywhere at any time for quick and engaging entertainment.

### Comprehensive Quiz Participation
- **Diverse Quiz Options**: Choose from a wide array of quizzes and categories tailored to your interests.
- **Detailed Results**: View detailed results after each quiz to understand your strengths and areas for improvement.

### Populate Quizzes Script
- **Populate Quiz Script**: A script that populates 

## Persona: Alex Schmidt

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

### Program Flowchart

![screenshot](documentation/programflowchart/programmflowchart.png)

## Features

#### User Registration and Login
- **Register**: Allows new users to create an account with a username and password.
- **Login**: Authenticates users and provides access to the application.

#### User Profile
- **Profile Management**: Users can view and update their profile information.
- **Delete Profile**: Users have the option to delete their profile, which will remove their account from the application.

#### Quiz Management
- **Create Quiz**: Logged-in users can create new quizzes and set up questions for them.
- **Update Quiz**: Users can edit existing quizzes they have created.
- **Delete Quiz**: Users can delete quizzes they have created.
- **Quiz Detail**: View details of a specific quiz including its title, description, and questions.

#### Question Management
- **Create Question**: Add new questions to a quiz they create.

#### Quiz Participation
- **Play Quiz**: Users can take quizzes by answering questions. The application keeps track of their progress and scores.
- **Quiz Results**: After completing a quiz, users can view their results and see their scores.

#### Categories and Random Quiz
- **List Categories**: Display all available quiz categories.
- **Random Quiz**: Redirect users to a random quiz from a specified category.

#### Leaderboard
- **Leaderboard**: Shows the top 10 users based on their total quiz scores.

### Initial Data Population Script

#### Purpose
The script is designed to populate the database with initial quiz data. It fetches questions from the Open Trivia Database API and creates quizzes in the application database for various categories.

#### Script Explanation
- **Import Libraries**: The script imports necessary libraries including `time`, `requests`, and Django models (`User`, `Quiz`, `Question`).
- **Command Class**: Defines a Django management command class `Command` that extends `BaseCommand`.
- **Help Attribute**: Provides a description of the command's purpose.
- **Handle Method**: The main method executed when the command runs. It performs the following tasks:
  - **Categories Definition**: A list of categories with their corresponding IDs is defined.
  - **Batch Processing**: Categories are processed in batches of 5 to avoid overloading the API.
  - **User Check**: Verifies that at least one user exists in the database. If not, it prompts to create a user first.
  - **API Request**: Fetches data from the Open Trivia Database API for each category.
  - **Error Handling**: Handles various possible errors including rate limits, failed requests, and unexpected errors.
  - **Quiz Creation**: Creates a new quiz for each category and adds questions to it based on the API response.
  - **Batch Delay**: Waits for 30 seconds between batches to avoid overloading the API.

#### Key Operations
1. **Category Definition**: Defines a list of quiz categories and their corresponding IDs from the Open Trivia Database.
2. **Batch Processing**: Divides the list of categories into smaller batches to process them in manageable chunks.
3. **User Existence Check**: Ensures that there is at least one user in the database before proceeding. If no users are found, the script stops and provides an error message.
4. **API Request and Response Handling**: For each category, the script makes an API request to fetch quiz questions. It handles various response statuses:
   - **Success (200)**: Processes the data and creates quizzes and questions in the database.
   - **Rate Limit (429)**: Waits for a specified time before retrying the request.
   - **Other Errors**: Logs an error message and skips the current category.
5. **Quiz and Question Creation**: Uses the fetched data to create quizzes and their associated questions in the application database.
6. **Batch Completion Delay**: Introduces a delay between processing batches to avoid overwhelming the API with requests.

#### Example Usage
To run the script, use the following command in the terminal:
- sh
- python manage.py <command_name>

## Technologies Used

### Backend
- **Django**: The primary web framework used to build the backend of the application. It provides robust features for building scalable and secure web applications.
- **Django Crispy Forms**: Enhances the rendering of Django forms with a more user-friendly layout.
- **Gunicorn**: A WSGI HTTP server for running the Django application.

### Frontend
- **Bootstrap**: A front-end framework used for responsive and mobile-first web development. It provides ready-to-use components and utilities for designing a responsive interface.
- **Font Awesome**: A library of icons used to enhance the visual appeal of the application.
- **Custom CSS**: For additional styling and layout customization of the application.
- **JavaScript**: For adding interactive functionality to the application.

### Database
- **SQLite**: The default database used by Django for development purposes. It is lightweight and easy to set up.

### Other Libraries
- **asgiref**: A collection of ASGI utilities used by Django for asynchronous support.
- **contourpy**: A library for contour plotting.
- **cycler**: A library used for creating iterable objects.
- **fabio**: A library for handling images and data.
- **fonttools**: A library for manipulating fonts.
- **h5py**: A library for interacting with HDF5 binary data format files.
- **hdf5plugin**: Plugins for HDF5 compression.
- **kiwisolver**: A library for solving mathematical expressions.
- **lxml**: A library for processing XML and HTML.
- **matplotlib**: A plotting library used for creating static, animated, and interactive visualizations.
- **numpy**: A library for numerical operations in Python.
- **pillow**: A library for image processing.
- **pyparsing**: A library for parsing strings into data structures.
- **PyQt5**: A set of Python bindings for the Qt application framework.
- **silx**: A library for scientific data visualization and analysis.
- **sqlparse**: A library for parsing SQL queries.
- **whitenoise**: A library for serving static files in a Django application.

### External Services
- **Open Trivia Database API**: An external API used to fetch quiz questions for populating the application database.

## Testing

### Code Validation

#### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot |
| --- | --- | --- |
| quizulu | index.html | ![screenshot](documentation/validation/html/w3chtmlvalidatorhome.png) |  
| quizulu | categories.html | ![screenshot](documentation/validation/html/w3chtmlvalidatorcategories.png) |
| quizulu | profile.html | ![screenshot](documentation/validation/html/w3chtmlvalidatorprofile.png) |  
| quizulu | leaderboard.html | ![screenshot](documentation/validation/html/w3chtmlvalidatorleaderboard.png) |  
| quizulu | login.html | ![screenshot](documentation/validation/html/w3chtmlvalidatorlogin.png) |  
| quizulu | logout.html | ![screenshot](documentation/validation/html/w3chtmlvalidatorlogout.png) |  
| quizulu | quiz_play.html | ![screenshot](documentation/validation/html/w3chtmlvalidatorquizplay.png) |  
| quizulu | question_creator.html | ![screenshot](documentation/validation/html/w3chtmlvalidatorquestioncreator.png) |  
| quizulu | quiz_creator.html | ![screenshot](documentation/validation/html/w3chtmlvalidatorquizcreator.png) |  
| quizulu | register.html | ![screenshot](documentation/validation/html/w3chtmlvalidatorregister.png) |  
| quizulu | my_quizzes.html | ![screenshot](documentation/validation/html/w3chtmlvalidatormyquizzes.png) | 
| quizulu | quiz_detail.html | ![screenshot](documentation/validation/html/w3chtmlvalidatorquizdetail.png) | 

#### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot |
| --- | --- | --- | 
| quizulu | style.css | ![screenshot](documentation/validation/css/w3ccssvalidator.png) |

#### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot 
| --- | --- | --- |
| quizulu | script.js | ![screenshot](documentation/validation/js/jshintes6validator.png) |  

#### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

apps.py  
![screenshot](documentation/validation/python/cipythonquizappappspy.png)   
forms.py
![screenshot](documentation/validation/python/cipythonquizappformspy.png)    
models.py 
![screenshot](documentation/validation/python/cipythonquizappmodelspy.png) 
urls.py
![screenshot](documentation/validation/python/cipythonquizappurlspy.png)    
views.py
![screenshot](documentation/validation/python/cipythonquizappviewspy.png) 
populate_quizzes.py
![screenshot](documentation/validation/python/cipythonquizapppopulatequizzespy.png)   
apps.py
![screenshot](documentation/validation/python/cipythonusersappspy.png) 
forms.py
![screenshot](documentation/validation/python/cipythonusersformspy.png) 
views.py
![screenshot](documentation/validation/python/cipythonusersviews.png)
models.py
![screenshot](documentation/validation/python/cipythonusersmodelspy.png) 
signals.py
![screenshot](documentation/validation/python/cipythonuserssignalspy.png)    
urls.py
![screenshot](documentation/validation/python/cipythonquizuludjangoprojecturlspy.png)

#### Lighthouse Audit
----------------

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

##### Desktop
| Page | Screenshot |
| --- | --- |
| Index |  ![screenshot](documentation/validation/lighthouse/lighthousedesktopindex.png)  | 
| Register | ![screenshot](documentation/validation/lighthouse/lighthousedesktopregister.png) | 
| Login | ![screenshot](documentation/validation/lighthouse/lighthousedesktoplogin.png) | 
| Categories |  ![screenshot](documentation/validation/lighthouse/lighthousedesktopcategories.png)  | 
| Profile |  ![screenshot](documentation/validation/lighthouse/lighthousedesktopprofile.png)| 
| Leaderboard |  ![screenshot](documentation/validation/lighthouse/lighthousedesktopleaderboard.png)  | 
| My Quizzes|  ![screenshot](documentation/validation/lighthouse/lighthousedesktopmyquizzes.png)  | 
| Question Creator|  ![screenshot](documentation/validation/lighthouse/lighthousedesktopquestionscreator.png)  | 
| Quiz Play |  ![screenshot](documentation/validation/lighthouse/lighthousedesktopquizplay.png)  | 
| Quiz Creator |  ![screenshot](documentation/validation/lighthouse/lighthousedesktopquizcreator.png)  |
| Quiz Details|  ![screenshot](documentation/validation/lighthouse/lighthousedesktopquizdetails.png)  | 
| Quiz Editor|  ![screenshot](documentation/validation/lighthouse/lighthousedesktopquizeditor.png)  | 
| Quiz Result|  ![screenshot](documentation/validation/lighthouse/lighthousedesktopquizresults.png)  | 

##### Mobile
| Page | Screenshot |
| --- | --- |
| Index |  ![screenshot](documentation/validation/lighthouse/lighthousemobileindex.png)  | 
| Register | ![screenshot](documentation/validation/lighthouse/lighthousemobileregister.png) | 
| Login | ![screenshot](documentation/validation/lighthouse/lighthousemobilelogin.png) | 
| Categories |  ![screenshot](documentation/validation/lighthouse/lighthousemobilecategories.png)  | 
| Profile |  ![screenshot](documentation/validation/lighthouse/lighthousemobileprofile.png)| 
| Leaderboard |  ![screenshot](documentation/validation/lighthouse/lighthousemobileleaderboard.png)  | 
| My Quizzes|  ![screenshot](documentation/validation/lighthouse/lighthousemobilemyquizzes.png)  | 
| Question Creator|  ![screenshot](documentation/validation/lighthouse/lighthousemobilequestionscreator.png)  | 
| Quiz Play |  ![screenshot](documentation/validation/lighthouse/lighthousemobilequizplay.png)  | 
| Quiz Creator |  ![screenshot](documentation/validation/lighthouse/lighthousemobilequizcreator.png)  |
| Quiz Details|  ![screenshot](documentation/validation/lighthouse/lighthousemobilequizdetails.png)  | 
| Quiz Editor|  ![screenshot](documentation/validation/lighthouse/lighthousemobilequizeditor.png)  | 
| Quiz Result|  ![screenshot](documentation/validation/lighthouse/lighthousemobilequizresults.png)  | 


### General Testing
-   Each feature was developed on the main branch. 
-   Each time a feature was added, all the functions were tested to see if there was an impact.
-   The site was sent to friends and relatives for feedback and testing.
-   The username input has a validation and will not submit without the proper information.
-   .gitignore file has been included to prevent system file commits.
-   External links open in a new tab.


## Manual Testing

The below table provides evidence of manual testing carried out for each feature.
  

| Feature | Test | Expected Outcome | Screenshot | Pass/Fail |
| ------------------- | ----------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------- | --------- |
| Register | Register a new user | User is registered and redirected to the login page | ![screenshot](documentation/manual/manualtestingregister.png) | Pass |
| Login | Log in with registered user | User is logged in and redirected to the profile page | ![screenshot](documentation/manual/manualtestinglogin.png) | Pass |
| Create Quiz | Create a new quiz | Quiz is created and displayed on the profile page | ![screenshot](documentation/manual/manualtestingquizcreator.png)| Pass |
| Update Quiz | Update an existing quiz | Quiz is updated and displayed on the profile page | ![screenshot](documentation/manual/manualtestingupdatequiz.png) | Pass |
| Delete Quiz | Delete an existing quiz | Quiz is deleted and removed from the profile page | ![screenshot](documentation/manual/manualtestingdeletequiz.png) | Pass |
| View Quizzes | View all quizzes | All quizzes are displayed | ![screenshot](documentation/manual/manualtestingquizview.png) | Pass |
| Play Quiz | Play a quiz | Quiz is played and results are displayed | ![screenshot](documentation/manual/manualtestingquizplay.png) | Pass |
| View Results | View quiz results | Quiz results are displayed | ![screenshot](documentation/manual/manualtestingresults.png) | Pass |
| Profile | View profile page | Profile page is displayed with user details and quizzes | ![screenshot](documentation/manual/manualtestingprofile.png) | Pass |
| Admin Manage Users | Admin views and manages users | Admin can view, edit, and delete users | ![screenshot](documentation/manual/manualtestingadminusers.png) | Pass |
| Admin Manage Quizzes| Admin views and manages quizzes | Admin can view, edit, and delete quizzes | ![screenshot](documentation/manual/manualtestingadminquizs.png) | Pass |

### Mobile Testing

-   I tested the site personally on my Android device, going through the entire process, checking buttons, functions, restarting the game, etc. I was personally unable to test on iOS.
-   The site was sent to friends and relatives for them to follow the same process. They have tested on their devices, only missing iOS devices.
- The testing was done using the Google Chrome Browser. Chrome Developer Tools were used extensively, particularly to check responsiveness on different screen sizes. Testing was also done using Firefox and Opera on desktop, and again on Google Chrome and Opera and Brave on the Nothing Phone (2).
-   Responsive on all device sizes between 320px - 2600px wide.
-   Devices tested using the Google Developer Tools emulator:


| Device                   | Device Size    | Tested |
|--------------------------|----------------|--------|
| BlackBerry Z30           | 360px x 640px  | ✅     |
| BlackBerry PlayBook      | 600px x 1024px | ✅     |
| Samsung Galaxy Note 3    | 360px x 640px  | ✅     |
| Samsung Galaxy S3        | 360px x 640px  | ✅     |
| Samsung Galaxy S9+       | 320px x 658px  | ✅     |
| LG Optimus L70           | 384px x 640px  | ✅     |
| Microsoft Lumia 550      | 640px x 360px  | ✅     |
| Microsoft Lumia 950      | 360px x 640px  | ✅     |
| Nexus 4                  | 384px x 640px  | ✅     |
| Nokia Lumia 520          | 320px x 533px  | ✅     |
| Nokia N9                 | 480px x 854px  | ✅     |
| Pixel 3                  | 393px x 786px  | ✅     |
| Apple iPad Mini          | 468px x 4024px | ✅     |
| Apple iPhone 4           | 320px x 480px  | ✅     |
| Apple iPhone 5/S         | 320px x 568px  | ✅     |
| Apple iPhone 6/7/8       | 375px x 667px  | ✅     |
| Apple iPhone 6/7/8 Plus  | 414px x 736px  | ✅     |
| Apple iPhone X           | 375px x 812px  | ✅     |
***

### Development Bugs

-   **Issue**: ImportError was raised due to incorrect import in `quiz_app/urls.py`.
-   **Solution**: Correct the import statement to refer to the correct views module. For example, change `from .templates.quiz_app import views` to `from . import views`.-   **Class-Based Views (CBVs) Login Requirement**:

-   **Issue**: `login_required` decorator was used on CBVs, which is not appropriate.
-   **Solution**: Use `LoginRequiredMixin` for class-based views to enforce login requirements.-   **`urls.py` Configuration**:

-   **Issue**: The URL patterns were not correctly defined, causing routing issues.
-   **Solution**: Ensure the `urlpatterns` list in `quizulu_django_project/urls.py` correctly includes paths from `quiz_app`.-   **Missing Templates**:

-   **Issue**: Errors due to missing templates or incorrect template paths.
-   **Solution**: Verify the existence and correct paths of all templates used in the views (e.g., `quiz_app/quiz_detail.html`, `quiz_app/play_quiz.html`).-   **Model Relationship Issues**:

-   **Issue**: Incorrect relationships between models causing errors.
-   **Solution**: Ensure the models (`Quiz`, `Question`, `UserQuizProgress`) are correctly defined with proper foreign key relationships.-   **Form Validation**:

-   **Issue**: Forms not validating correctly or not saving user data.
-   **Solution**: Properly configure forms and handle form validation in the views (e.g., `QuizForm` in `MyQuizCreateView`).-   **QuerySet Handling**:

-   **Issue**: Incorrect handling of QuerySets leading to runtime errors.
-   **Solution**: Ensure that QuerySets are correctly filtered and handled. For example, `Quiz.objects.values_list('category', flat=True).distinct()` to get distinct categories.-   **Redirection Logic**:

-   **Issue**: Incorrect redirection after form submission or quiz completion.
-   **Solution**: Correctly use `redirect` and `reverse_lazy` to manage URL redirection after various actions.-   **User Progress Tracking**:

-   **Issue**: Issues in tracking user progress within a quiz.
-   **Solution**: Correctly implement logic to track and update user progress in `UserQuizProgress`.-   **Shuffling Answers**:

-   **Issue**: Shuffling answers incorrectly or not shuffling at all.
-   **Solution**: Properly use Python's `random.shuffle` to shuffle quiz answers before presenting them to the user.-   **Handling POST Requests**:

-   **Issue**: Issues in handling POST requests in the `play_quiz` view.
-   **Solution**: Correctly parse and handle form data submitted via POST requests to process quiz answers.-   **Error Logging**:

-   **Issue**: Lack of proper error logging making it difficult to debug.
-   **Solution**: Implement logging using Python's `logging` module to log errors and important actions in the application.-   **Database Migrations**:

-   **Issue**: Errors during `makemigrations` or `migrate` commands.
-   **Solution**: Ensure all models are correctly defined and registered in `admin.py`. Run `python manage.py makemigrations` and `python manage.py migrate` to apply changes to the database schema.-   **User Authentication**:

-   **Issue**: Problems with user authentication and access control.
-   **Solution**: Implement proper authentication checks using decorators and mixins to ensure only authorized users can access certain views.

## Data Storage

The Quizulu App utilizes SQLite for efficient data storage and management. Here's how the data is organized and utilized within the app:

### User Information

- The `User` model in the `users` app contains details such as usernames, email addresses, and password hashes. This information is crucial for user authentication and personalized experiences within the app.

### Quizzes and Questions

- The `Quiz` and `Question` models in the `quiz_app` manage the storage of quiz details and questions respectively. This includes quiz titles, descriptions, question texts, choices, and correct answers.

### User Progress and Scores

- User progress and scores are tracked through models such as `UserQuiz` and `UserAnswer`. These models store information about which quizzes users have taken, their responses, and scores, enabling the app to provide feedback and track performance over time.

## Data Handling and Privacy

### Django ORM Integration

- The app integrates with SQLite using Django's Object-Relational Mapping (ORM) system. This allows for seamless database operations while keeping the codebase clean and maintainable.

### Data Privacy

- Sensitive data, such as user passwords, are hashed before storage using Django's built-in hashing mechanisms. This ensures that even if the database is compromised, the actual passwords remain secure.

### Real-Time Updates

- The app dynamically updates user scores and progress in real-time. After each quiz attempt, scores are calculated and updated immediately, providing users with instant feedback.

### Security Measures

- Django's built-in security features, such as SQL injection prevention, cross-site scripting (XSS) protection, and cross-site request forgery (CSRF) protection, are utilized to enhance the security of data interactions within the app.

### Static Files Management

- The `WhiteNoise` middleware is used to efficiently serve static files. This includes CSS, JavaScript, and image files that are necessary for the front-end of the application. Static files are managed securely and served with optimal performance.


## Deployment

The Quizulu App was developed using Gitpod and Visual Studio Code for code creation and file management. The project files, code, and related information are hosted on GitHub.

### Deploying the App

To deploy the Quizulu App on Heroku, follow these steps:

1.  **Heroku Account Setup:** Log in to Heroku or create an account if you haven't already.
2.  **Create a New App:** From the Heroku dashboard, click on the "New" button and select "Create new app" from the dropdown menu.
3.  **App Configuration:** Provide a unique name for your application and select the appropriate region.
    -   Example: Name: "quizulu-app", Region: Europe.
4.  **Add Config Vars (if necessary):**
    -   If your project requires environment variables, add them under the "Settings" tab in the "Config Vars" section.
5.  **Set Buildpacks:**
    -   Navigate to the "Settings" tab and locate the "Buildpacks" section.
    -   Click on "Add buildpack" and select Python.
    -   Add another buildpack for Node.js.
    -   Ensure that the Python buildpack is positioned above the Node.js buildpack.
6.  **Deploy from GitHub:**
    -   Go to the "Deploy" section and choose "GitHub" as the deployment method.
    -   Connect your GitHub repository to Heroku by searching for the repository name and clicking "Connect".
    -   Scroll down and click "Deploy Branch" to deploy the app.
7.  **Automatic Deploys (Optional):**
    -   If desired, enable automatic deploys to rebuild the app whenever changes are pushed to GitHub.

### Forking The Repository

You can fork the Quizulu App repository to create a copy for viewing and editing without affecting the original. Follow these steps:

1.  Navigate to the repository on GitHub.
2.  Click on the "fork" tab in the top right corner.
3.  Click on "create fork" to fork the repository.

### Cloning The Repository

To clone the Quizulu App repository from GitHub:

1.  Go to the repository and select the "code" tab.
2.  Copy the repository's HTTPS URL.
3.  Open Git Bash and navigate to the desired directory.
4.  Type `git clone` followed by the copied URL and press "enter".

### APIs

The Quizulu App does not require external APIs for its core functionality. All necessary data is managed internally through the SQLite database and Django models. If you plan to integrate additional features that require APIs, please refer to the respective API documentation for setup instructions.

For further instructions and detailed steps on deploying and managing your Heroku app, refer to the Heroku documentation and the Django deployment guide.


## Acknowledgements: 
- A very special thanks to Pascal the most helpful person i ever met.  He has helped me tremendously with ideas, fixes and feedback.

- I also want to thank my Mentor Rory-Patrick who gave me so many tips and tricks, and inspired me along the way.

- Also very special thanks to my dog who provided emotional support and times to unwind.

- I thank all my peers in my course, who provided a lot of support and feedback!

- I thank all my family members and friends who not only gave feedback and support but also tested it on their devices.
> Written with [StackEdit](https://stackedit.io/).