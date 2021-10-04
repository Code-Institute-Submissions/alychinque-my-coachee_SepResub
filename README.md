# **My Coachee**

![multi platform](add-later-on)

## **Project Goal**
This is a platform to help coaches to keep their sessions organized. A coach can add all their coachees and then book sessions with them. In a session, there is everything they talk about in the previous sessions. So that coaches have a powerful tool in their hands. This project have a membership system with three categories.
Happy Code! 👨‍💻 Happy days!

## Table of contents 
* [UX](#ux)🎯
    * [User Goals](#user-goals)
    * [User Stories](#user-stories)
    * [Site Owners Goals](#site-owners-goals)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
        * [Requirements](#requirements)
        * [Expectations](#expectations)
    * [Design Choices](#design-choices)🎨
        * [Fonts](#fonts)
        * [Structure](#structure)
* [Wireframes and Flowcharts](#wireframes-and-flowcharts)👨‍🔧
    * [Wireframes](#wireframes)
* [Features](#features)🤖
    * [Existing Features](#existing-features)
    * [Features to be implemented](#features-to-be-implemented)
* [Technologies used](#technologies-used)👀
    * [Languages](#languages)🔍
    * [Libraries and Frameworks](#libraries-and-frameworks)📚
    * [Tools](#tools)🔧
* [Testing](#testing)
* [Bugs](#bugs)🐞
* [Future Implementations](#future-implementations)🛸
* [Deployment](#deployment)
    * [Local Deployment](#local-deployment)
    * [Heroku Deployment](#heroku-deployment)
* [Credits](#credits)


### **User Goals**

* This web platform has to work well on all kind of devices like mobile phones, tables and desktops.
* I want to have a clear dashboard with icons. 
* I want to have a profile.
* I want to add, update and delete coachees.
* I want to add, update and delete sessions.
* I want to be able to update materials.
* This web platform has to be user friendly.
* Visually appealing web application.

### **Site owners Goals**
* Have a valuable web platform.
* Have great tools to help coaches get organized.
* Have membership plans.

### **User Stories**

#### As a user, I would like...

* To be able to register for the web platform so I can have my personal environment.
* To login after I created an account and see my previous inserted information.
* To be able to add, update, and delete coachees.
* To be able to add, update, and delete sessions.
* To see the content of the previous sessions in the current session.
* To send some materials after each session via email.
* To add, update and delete my own material.
* To be able to subscribe to a plan.

#### As a site's owner, I would like...

* To add, update, and delete some interesting news for coaches subscribed.
* To add, update, and delete material.
* To have clean pages.
* To have three different plans.


### **User Requirements and Expectations**

#### Requirements

* Easy to navigate by using few buttons.
* Appealing dashboard with a functional overview.
* Easy way to subscribe.
* Ability to add, edit, and delete coachees.
* Ability to add, edit, and delete sessions.
* Ability to add, edit, and delete materials like books, movies, and activities.
* See a report with information about hours spent in the platform.

#### Expectations

* A powerful platform to organize all coachees and sessions.
* To have a dashboard where all the necessary information is visible.
* It should be easy to add, edit, and delete coachees, sessions and materials.
* It should be multiplatform.

### **Design Choices**🎨
TO BE DEFINED

#### Fonts
TO BE DEFINED

#### Structure
I will use [Boootstrap](https://getbootstrap.com/) to create an overall structure for the web platform. 
Bootstrap provides various elements of CSS and Javascript which is very helpful to keep a good structure throughout the pages.

## **Wireframes and Flowcharts**👨‍🔧

### **Wireframes**
I used [Draw.io](https://draw.io/) to create wireframes for my website. 

You can find my wireframes below:

#### Desktop Wireframes
* [Go to Desktop Wireframes](wireframes/desktop-wireframes.pdf)

#### Mobile Wireframes
* [Go to Mobile Wireframes](wireframes/mobile-wireframes.pdf)

#### Tablet Wireframes
* [Go to Table Wireframes](wireframes/tablet-wireframes.pdf)

## **Features**🤖

### **Existing Features**

* Sign-In and Out functionality
* Payment system
* Add multiple coachees per user 
* CRUD Functions:
    * Create: possibility to add various coachees.
    * Read: list all your coachees
    * Update: edit your coachees
    * Delete: delete your coachees
* CRUD Functions:
    * Create: possibility to add various appointments.
    * Read: list all your appointments
    * Update: edit your appointments
    * Delete: delete your appointments
* CRUD Functions:
    * Create: possibility to add various sessions.
    * Read: list all your sessions
    * Update: edit your sessions
    * Delete: delete your sessions

### **Features to be implemented**

* Have a fucionality to depends on plan show more or less indications.
* Have a more extensive management over the system.
* Have a functionality to report time spent in the platform
* Have a functionality to show old appointments 

## **Technologies used**👀

### **Languages**🔍

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://www.python.org/)

### **Libraries and Frameworks**📚

* [Django](https://www.djangoproject.com/)
* [Font Awesome](https://fontawesome.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Google Fonts](https://fonts.google.com/)
* [jQuery](https://jquery.com/)

### **Tools**🔧
* [Git](https://git-scm.com/)
* [Heroku](https://www.heroku.com/)
* [Balsamic](https://balsamiq.com/wireframes/)

## **Testing**

### **Register**

#### User story: As a user, I would like to be able to register for the web platform so I can have my personal environment.

* **Plan**  
Use allauth and then create a coach

* **Implementation**  
Allauth manages the registration 

* **Test**  
One can register by insert email, username and password

* **Verdict**    
The test has passed all the criteria and works like planned.

### **Login**

#### User story: As a user, I want to login after I created an account and see my previous inserted information.

* **Plan**  
Use allauth to gain access to the platform

* **Implementation**  
Allauth manages the login 

* **Test**  
One can login by insert username and password

* **Verdict**    
The test has passed all the criteria and works like planned.

### **CRUD Coachees**

#### User story: As a user, I would like to be able to add, update, and delete coachees.

* **Plan**  
Create view, urls and templates to create, read, update and delete coachees.

* **Implementation**  
Created the logic in the view and a template for each crud step.

* **Test**  
One can create, read, update and delete coachees.

* **Verdict**    
The test has passed all the criteria and works like planned.

### **CRUD Sessions**

#### User story: As a user, I would like to be able to add, update, and delete sessions.

* **Plan**  
Create view, urls and templates to create, read, update and delete sessions.

* **Implementation**  
Created the logic in the view and a template for each crud step.

* **Test**  
One can create, read, update and delete sessions.

* **Verdict**    
The test has passed all the criteria and works like planned.


## **Deployment**

### Heroku Deployment

#### Steps to deploy my-coachee to Heroku using Postgres

### In Heroku:
1. Setup and account and log in to Heroku
2. On the apps page select `NEW`.
3. Give the app a name and select the closest region – then click `Create App`.
4. Click on Resources tab to provision a new Postgres database for it.
5. Search in the Addons search bar for `Heroku Postgres`.
6. Select your Development plan.

### In GitPod or IDE:
7. To use postgres open project in GitPod and install:
```
*   pip3 install dj_database_url
*   pip3 install psycopg2-binary
*   Update requirements: pip3 freeze > requirements.txt
```

### In Django - setup new database:
In `Settings.py`:   

8. Make sure import os is there.
9. Add: `import dj_database_url`.
10. Go to Database settings and comment out existing database setting and add below example to point the database at the new Postgres database.
```
example:
    DATABASES = {
        'default': dj_database_url.parse( # ***paste in the database URL from Heroku***)
    }
```
11. Run Migrations. `Migrations have now been made to the Postgres Database.`
12. Now we can create a superuser -: `python3 manage.py createsuperuser`.
13. Runserver and login as superuser to the admin page.

14. Restart the server and check admin
15. Go to Settings -  Database settings - remove the Postgres database URL.
16.  Create an if/else code block to check if the os.environ variable is defined. 
if it is defined that will mean we are on Heroku so we will use the Postgres database.
Else we will be in our local environment and so use the default database.
```
    Example: 
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
```

17. In the Terminal install gunicorn as our webserver: `pip3 install gunicorn`
18. Freeze requirements. `Pip3 freeze > requirements.txt`
19. Create a Procfile at the same level as the project. 
20. Enter the following code into the Procfile to tell Heroku to create a web dyno that will run gunicorn and serve eHand:
```
    web: gunicorn ehand.wsgi:application
```
21. Temporarily disable collect static – to do this:
*   login via the terminal: heroku login –i.
*   Enter heroku email and password.
*   Enter the following in the terminal:
```
    heroku config:set DISABLE_COLLECTSTATIC=1 --app mr-smyth-ehand
```
In `Settings.py`:   

22. Add the hostname of the Heroku app – to ALLOWED_HOSTS (also include localhost):
```
    ALLOWED_HOSTS = ['my-coachee.herokuapp.com', '127.0.0.1'].
```
23. Ensure all .env variables such as the Django and stripe secret keys remain private. Also, make sure they are set up inside Heroku's config vars.

In `The Terminal`:

24. Deploy to Heroku:
*   Add and push to GitHub
*   git add .
*   git commit –m “**your-message**”
*   git push
*   Now initialize heroku git remote (because we created our app on the website rather than with the CLI): 
*       heroku git:remote -a my-coachee
*   Then push to heroku : git push heroku master

In `The Heroku`:

25. Setup automatic deployment in Heroku:
*   Go to the deploy tab
*   Set deployment method to GitHub
*   Search for my-coachee
*   Click connect
*   Scroll down and click Enable Automatic Deploys

ehand is now deployed to Heroku


### Local Deployment

**Before starting, some prerequisites:**

*   Before starting you should have an IDE set up - [Visual Studio Code](https://code.visualstudio.com/). - for example.
*   Its advisable to have a virtual environment setup. Pythons own can be used : 

```
    python3 -m .venv venv
    .venv\Scripts\activate
```

*   Have **at least** the following installed:   
    *   Python3 - to run the application.
    *   Pip - to install any requirements.
    *   GIT - required for version control.

### Steps to Deploy

1.  Open a Git Bash Command line, in your preferred destination.
2.  Enter git clone and paste in this link `https://github.com/alychinque/my-coachee`.
3.  Open the cloned repo in your IDE.
4.  Create a .env file containing private credentials.
```
Example of env file

DEVELOPMENT_LOCAL=True
SECRET_KEY=from a genetrator
STRIPE_PUBLIC_KEY=from stripe
STRIPE_SECRET_KEY=from stripe
```

The above example displays an env for a local purpose only.

5.  Install all requirements for the application by using this command:
```
    sudo -H pip3 -r requirements.txt
```
6.  In the IDE terminal, use the following command to start my-coachee:
```
    python manage.py runserver
```

my-coachee should now be running locally on localhost port 8000. (http://127.0.0.1:8000)

7.  After running Django initially, it will create the local database **db.SQLite3**.
8.  Make all migrations:
```
python3 manage.py makemigrations --dry-run
python3 manage.py makemigrations
python3 manage.py migrate --plan
python3 manage.py migrate
```

9.  Create a superuser:
```
python3 manage.py createsuperuser
***Enter username, email and password***
```

You should now have a local copy of my-coachee.
