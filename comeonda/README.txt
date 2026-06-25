PROJECT SETUP

1. Clone the repository
   git clone <repository_url>
   cd comeonda

2. Create a virtual environment
   uv venv

3. Activate the virtual environment (Windows)
   .venv\Scripts\activate

4. Install dependencies
   uv pip install -r requirements.txt

5. Create a MySQL database
   Create a database named: come_on_da_db

6. Configure environment variables
   Fill the .env file in the project root:

   DATABASE_URL=mysql+aiomysql://root:password@localhost:3306/come_on_da_db
   SECRET_KEY=your_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   MAIL_USERNAME=your_email@gmail.com
   MAIL_PASSWORD=your_app_password
   MAIL_FROM=your_email@gmail.com
   MAIL_PORT=587
   MAIL_SERVER=smtp.gmail.com
   MAIL_FROM_NAME=Come On Da

7. Apply database migrations
   alembic upgrade head

8. Run the application
   uv run uvicorn main:app --reload


DEFAULT ADMIN ACCOUNT
Username: admin
Password: admin123


API LIST

USERS
POST    /users/register                            Register User
POST    /users/login                               Login
GET     /users/profile                             Profile


SPORTS
GET     /sports/                                   Get Sports
POST    /sports/                                   Create Sport
GET     /sports/{sport_id}                         Get Sport
PUT     /sports/{sport_id}                         Update Sport
DELETE  /sports/{sport_id}                         Delete Sport


TEAMS
GET     /teams/                                    Get Teams
POST    /teams/                                    Create Team
GET     /teams/{team_id}                           Get Team
PUT     /teams/{team_id}                           Update Team
DELETE  /teams/{team_id}                           Delete Team


MATCHES
GET     /matches/                                  Get Matches
POST    /matches/                                  Create Match
GET     /matches/{match_id}                        Get Match
PUT     /matches/{match_id}                        Update Match
DELETE  /matches/{match_id}                        Delete Match


QUESTIONS
GET     /questions/                                Get Questions
POST    /questions/                                Create Question
GET     /questions/{question_id}                   Get Question
PUT     /questions/{question_id}                   Update Question
DELETE  /questions/{question_id}                   Delete Question


ANSWERS
POST    /answers/                                  Submit Answer
GET     /answers/my-history                        My History


RESULTS
POST    /results/                                  Declare Result
GET     /results/{question_id}                     Get Result
GET     /results/my-result/{question_id}           My Result


POINT HISTORY
GET     /point-history/my-history                  My Point History
GET     /point-history/user/{user_id}              Get User Point History
GET     /point-history/                            Get All Point History


NOTIFICATIONS
GET     /notifications/my-notifications            My Notifications
PATCH   /notifications/{notification_id}/read      Mark As Read
DELETE  /notifications/{notification_id}           Delete Notification
GET     /notifications/all                         Get All Notifications


LEADERBOARD
GET     /leaderboard/global                        Global Leaderboard
GET     /leaderboard/top/{count}                   Top Players
GET     /leaderboard/me                            My Rank