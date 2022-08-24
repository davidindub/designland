
# designland

![Designland logo](docs/images/logo.png)


## Table of Contents


## Introduction

The project is an online directory of useful design resources for web developers and designers.

Users can register to submit resources to the directory, and upvote and bookmark resources they find useful.


## User Stories



## 



## UX  



### Typography


### Wireframes

![](/docs/images/wireframe.png)

### Database Design

![](/docs/images/database_design.png)


## Features 


### Existing Features

#### Upvote Resources and view most Popular

#### Register / Login

#### Bookmarks

#### User Profiles

#### Submit Resources to Directory


***


### Features Left to Implement



## Technologies Used

- [Python](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/) for installing Python packages.
- [Git](https://git-scm.com/) for version control.
- [GitHub](https://github.com/) for storing the repository online during development.
- GitHub Projects was invaluable throughout the project and helped me keep track of things to do and bugs to fix - you can see [the project's board here](https://github.com/users/davidindub/projects/7).
- [GitPod](https://gitpod.io/) as a cloud based IDE.
- [Balsamiq](https://balsamiq.com/wireframes/) for wireframing.
- [Bootstrap](https://getbootstrap.com/) as a front end framework.
- [Google Chrome](https://www.google.com/intl/en_ie/chrome/), [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/) and [Safari](https://www.apple.com/safari/) for testing on macOS Monterey.
<!-- - [Lucid Chart](https://lucid.app/) for making flow charts. -->

## External Python Packages Used

- [django-taggit](https://github.com/jazzband/django-taggit) for tags on directory entries



## Testing 



### Challenges Faced




### Code Validation


<details>

<summary>PEP8 Online Validation</summary>

</details>

***



## Deployment

### Local Deployment


In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

- `git clone https://github.com/davidindub/designland.git`


Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/davidindub/designland)

***

After cloning or opening the repository in Gitpod, you will need to:

1. Create your own `env.py` files in the root level of the project:

```
os.environ["DATABASE_URL"] = "postgres://"
os.environ["SECRET_KEY"] = "YOUR_DJANGO_SECRET_KEY"
os.environ["CLOUDINARY_URL"] = "cloudinary://YOUR_CLOUDINARY_URL"
os.environ["HEROKU_HOSTNAME"] = "URL_OF_PROJECT_DEPLOYED_ON_HEROKU"
os.environ["DEVELOPMENT"] = "True"
```
**Ensure the 'env.py' file is added to your '.gitignore' file so it doesn't get pushed to a public repository.

If you don't have a Cloudinary account already, you will need to [Sign Up for Free](https://cloudinary.com/users/register/free) to host the static files in the project.

2. Run `pip3 install -r requirements.txt` to install required Python packages.

3. Migrate the database models using:
`python3 manage.py migrate`

4. Create a superuser with your own credentials:
`python3 manage.py migrate`

5. Run the Django sever:
`python manage.py runserver`
The address of the server will appear in the terminal window.
Add /admin to the address to acces the Django admin panel using your superuser credentials.

### Heroku Deployment
<details>

<summary>
Full Instructions on deploying to Heroku
</summary>

Sign up to [Heroku](https://heroku.com/) for free if you don't already have an account.

1. Create a new app in Heroku.

2. In the Resources tab of your app in the Heroku dashboard, click Add-Ons and select Heroku Postgres. Select Hobby Dev - Free as your plan.

3. When Heroku Postgres is installed, click the Settings tab in the Heroku Dashboard.
Click Reveal Config Vars, and add the same variables from your `env.py` file here, except for `DEBUG`, as you don't want debug mode on the deployed project.

4. Copy the value of `DATABASE_URL` from the Config Vars. In your `settings.py` file, comment out the default database configuration, and add a new one with the Postgres url.

```
DATABASES = {
    'default': dj_database_url.parse('your DATABASE_URL here'))
}
```

5. Migrate the database models using:
`python3 manage.py migrate`

6. Create a superuser with your own credentials:
`python3 manage.py migrate`

7. Create a file called `Procfile` (no extension) containing the following:
```
web: gunicorn designland.wsgi
```

8. Run `pip3 install -r requirements.txt` to install required Python packages.

9. Add the url of your Heroku app (for example 'designland.herokuapp.com') to your `env.py` file in the local deployment, and to the Config Vars in your Heroku deployment.

10. Disable collect static so that Heroku doesn't try to collect static files when you deploy by typing the following command in the terminal

```
heroku config:set DISABLE_COLLECTSTATIC=1
```

11. Stage and commit your files to GitHub
```
git add . 
git commit -m "Commit message"
git push
```

12. In the Heroku dashboard for your App, select Deploy.
Under Deployment Method, choose GitHub and search for your repository and click Connect.

13. Select Enable Automatic Deployments, and then Deploy Branch. Heroku will build the App from the branch you selected.

14. Now whenever you push your commits to GitHub, Heroku will rebuild the application.

</details>


## Credits 

### Content 


### Media

- [Bootstrap Icons](https://icons.getbootstrap.com/) were used extensively in the project.





### Acknowledgements
