
# designland

![Designland logo](docs/images/logo.png)


## Table of Contents


## Introduction

The project is an online directory of useful design resources for web developers and designers.

Users can register to submit resources to the directory, and upvote and bookmark resources they find useful.


## User Stories



## 



## UX  

As the project is a directory of design resources, I wanted to try something fun and bold with the design and was inspired by the trend for neubrutalism web design, and websites such as [Gumroad](https://gumroad.com/) and [Google I/O 2022](https://io.google/2022/).

I ensured that despite bold use of color, every element still met AAA level in the [Web Content Accessibility Guidelines](https://www.w3.org/WAI/WCAG2AAA-Conformance) (WCAG)

[Qode Magazine - 60 Best Examples of Brutalism in Web Design](https://qodeinteractive.com/magazine/best-examples-of-brutalism-in-web-design/)
[Elementor Blog - What Is Brutalism in Web Design?](https://elementor.com/blog/brutalism-in-web-design/)

### Typography

- A display font called [Bebas Neue](https://fonts.google.com/specimen/Bebas+Neue?query=bebas) was used for the logo as it fitted the neubrutalist theme of the site.

- [Baloo 2](https://fonts.google.com/specimen/Baloo+2?query=baloo) contrasts the harsh lines of the display font with friendlier rounded letters that made it suitable for the headings and navbar.


### Wireframes

![](/docs/images/wireframe.png)

### Database Design

![](/docs/images/database_design.png)


## Features 


## Existing Features

### Navbar

The Navbar is responsive and collapses to a hamburger menu on smaller devices. On larger screen it sticks to the top when the page is scrolled.

When a user is logged in, their username is displayed in the navbar, and a dropdown menu includes:
- My Profile (link to the user's own profile)
- My Bookmarks (list of the resources the user has bookmarked)
- My Submissions (list including submissions not yet approved by staff)
- Submit New Resource (form to submit a new resource)
- Logout

When a staff member is logged in, an extra Manage dropdown option is shown which includes:
- Unapproved Resources (submissions not yet visible on the site ready for screening)
- Django Admin Panel (a link to the Django Administration Panel)


### Register / Login

Users can either sign up using their Google or Github account, or directly on the site.

GitHub was chosen as the site is aimed at developers and designers, and Google as is has 1.8 billion active montly users.

Users who have previously registered with GitHub or Google can easily sign in again with one click.

### Upvoting

Users can upvote the resources they like, other users will see the total number of uploads and can view the most popular resources on the site.

### Bookmarks

Users can bookmark resources they find useful in list that only they, and not other users can see.

### User Profiles

Users can display links to their Personal Website, GitHub profile and Twitter profile

A list of all the resources the user has contributed is shown on their page.

When a logged in user views their own profile, they can click a button to edit it. The user can delete their account from this page too if they choose.

### Submit Resources to Directory

When a user submits a resource to the directory, it is awaiting approval by a staff member. In the mean time, the user can see the resource in their My Submissions section (along with a badge telling them if it's been approved or not)

### Footer

The Footer includes:
- A link back to the homepage
- Copyright information
- A link to the Privacy Policy
- A link to the [GitHub repository for the project](https://github.com/davidindub/designland).

### Privacy Policy

As the project can collect data from users, I included a Privacy Policy link in the Footer which explains how data may be used. I used [GDPR.eu](https://gdpr.eu/) for help writing the policy.

See:
[Writing a GDPR-compliant privacy notice (template included)](https://gdpr.eu/privacy-notice/)

### Notifications

Django Messages and Bootstrap's Toast elements were combined to make elegant notification messages when the user performs actions such as signing in/out and bookmarking or upvoting a resource. Staff also see notifications for things like approving/hiding/deleting resources.

***


### Features Left to Implement

- Currently the screenshot thumbnails for the site are manually uploaded to Cloudinary by an administrator, but I would like to add an API such as [URL2PNG](http://url2png.com/) in future to automate the process, however it was difficult to find a free service for this project.

- With Heroku ending free plans in November 2022, the project will be redeployed on a different cloud platform in future. This was only announced when nearing the final sprint.



## Technologies Used

- [Python](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/) for installing Python packages.
- [Git](https://git-scm.com/) for version control.
- [GitHub](https://github.com/) for storing the repository online during development.
- GitHub Projects was invaluable throughout the project and helped me keep track of things to do and bugs to fix - you can see [the project's board here](https://github.com/users/davidindub/projects/7).
- [GitPod](https://gitpod.io/) as a cloud based IDE.
- [Balsamiq](https://balsamiq.com/wireframes/) for wireframing.
- [Bootstrap 5](https://getbootstrap.com/) as a front end framework.
- [Google Chrome](https://www.google.com/intl/en_ie/chrome/), [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/) and [Safari](https://www.apple.com/safari/) for testing on macOS Monterey.
- [diagrams.net](https://www.diagrams.net/) for drawing database diagrams.

## External Python Packages Used

- [django-taggit](https://github.com/jazzband/django-taggit) for tags on directory entries
- [django-crispy-forms](https://pypi.org/project/django-crispy-forms/) for help styling the forms
- [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/) for Bootstrap 5 templates for django-crispy-forms



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
- [Writing a GDPR-compliant privacy notice (template included)](https://gdpr.eu/privacy-notice/)


### Media

- [Bootstrap Icons](https://icons.getbootstrap.com/) were used extensively in the project.





### Acknowledgements
