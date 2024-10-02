A beta version

# Game-Reviews
A web application designed to collect and display reviews for new games. Users can register, add games, and leave their feedback, allowing others to gather insights on new titles and their ratings.

## Key Entities

1. **User Profile**
   - User registration and authentication.
   - Required fields: `username`, `email`, `password`.

2. **Game**
   - Title
   - Genre
   - Description
   - Release Date
   - Developer

3. **Review**
   - Author (user)
   - Game being reviewed
   - Rating (from 1 to 10)
   - Review text
   - Review creation date

4. **Game Review Statistics**
   - Average rating
   - Total number of reviews
   - Percentage of positive (6+) and negative reviews

## Functionality

- **Registration and Login**: Users can create an account and log into their profile using a unique `username` and password.
- **Adding Games**: Automation of the game addition process with all necessary information.
- **Leaving Reviews**: Registered users can leave reviews for games, including textual comments and ratings.
- **Viewing Statistics**: For each game, average ratings and percentages of positive, neutral, and negative reviews are displayed.

## Website Pages

1. **All Games List Page**: View all games added by users (currently as a home page)
2. **User Profile Page**: Displays `username` and all user reviews (currently a profile image can be added only with admin)
3. **Registration Page**: Option to create a new account with a link to the login page.
4. **Login Page**: Log into the profile using username and password.
5. **Game Profile Creation Page**: Form to input information about a new game.
6. **Game Profile**: Information about the game, including average rating and reviews.
7. **Review Submission Page**: Submit a review for a game, including the option to provide a rating.

## Stack Used

- **Backend**: Python - Django
- **Frontend**: HTML, CSS
- **Database**: SQLite3 (as test) for storing user data, game information, and reviews.


## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/hani-momo/Game-Reviews
2. Change to the project directory:
   ```bash
   cd Game-Reviews
3. Create a virtual environment and activate it:
   ```bash
   python -m venv gr_env
   source gr_env/bin/activate  # On Windows: gr_env\Scripts\activate
5. Install the required packages, dependencies:
   ```bash
   pip install -r requirements.txt
6. Run migrations:
   ```bash
   pithon manage.py migrate
7. Create a superuser (opt.):
   ```bash
   python manage.py createsuperuser
8. Start the server:
   ```bash
   python manage.py runserver
9. Go to http://127.0.0.1:8000/
10. To deactivate the venv (optional):
    ```bash
    deactivate
