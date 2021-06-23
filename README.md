### First is the main tutorial repo which does UPDATE/ADD/DELETE

In django websites, url.py of main project folder contains urls of all the apps which are connected to the root website. Furthermore, for login/logout/signup there's a separate app that you need to include in urls (See first project's settings/url for demo). 

In each app, there's again a url.py file which contains link to a functionality of the site (contained in views.py). "views.py" contains functionality (each functionality contains a website, i.e. in each function we typically return a HttpResponse or we can return a template html and pass a dictionary of parameters to the template html, which is interpreted in the template html). So each views functionality has a url, which is referenced by urls.py (inside the app, not the root project)

For example, suppose my project name is first and an app named "want" is made in it. To reference a functionality of the app "want" we've to go to localhost:want/functionality. Typically we also past GET/POST variables in it. 

As for how to do CRUD with database, look into the project "first". In the "want" app inside it, in the views.py file you can see the functions for doing CRUD. Please raise an issue if you have a question or there's something you don't understand in my code. 
