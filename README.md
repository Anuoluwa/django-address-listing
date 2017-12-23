# django-address-listing
A Django based application which stores names and email addresses in a database (SQLite ). 

•	Django App
---------------
Make an application which stores names and email addresses in a database (SQLite is fine). Make sure it:
1.	Has welcome page in http://localhost/ 
Note: this page has links to list and create functions
2.	Lists all stored names/email address in http://localhost/list
3.	Adds a name/email address to the database in http://localhost/add 
Note: should validate input and show errors

The challenge is a Django based application, so please make sure you use all of Django infrastructure (form, template inheritance, ORM) correctly. Also make sure the app does not have major security problems: CSRF, XSS, SQL Injection.

Make reasonable assumptions, state your assumptions, and proceed. Once you have completed the challenge, let us know and share your thoughts on the problems/solutions.

#### Git Workflow
**The master branch is intact. I used another branch 'Develop'. And for every feature, I new branch is created locally and merged upstream with develop branch with pull requests.**

### Django Infasctructure Used
  #### ModelForm, template inheritance, ORM, migrations were all used


### Unit Tests

Unit testing is one of the assumptions that I made for this app, so I implemented unit tests for model and view only, I did not write tests for forms because I used _Django ModelForms_.


### Functionalities
**This app essentially focus on the backend, using Django and Python**
* A user should be able to create Listing
* A user should be able to can add Listings
* A user should be able to view a single list on a page
* A user should be able to update lists
* A user should be able to delete a specific list
