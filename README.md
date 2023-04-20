
# Phisher

This tool is designed to help social engineers to automate their phishing campagnes.
The software is developped in python using Django Framework.


## Installation

Install Phisher with python

```bash
    $ pip install django
    $ pip install django-import-export
    $ pip install django-admin-extra-buttons
```

Starting the project
```bash
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ mkdir emails                          (Here will be stored the email examples)
    $ python manage.py runserver
```
## Features

- Import/Export data in several formats(csv,excel, etc..)
- User Friendly UI
- Easy to use
- Realist process


## Demo

- Go to http://localhost:8000/
- Login with the admin user created
- Go to Frontend/Users tab
- Click on Import button and add the mail_list.csv data set test from the root path of the git repository
- Click on Send Amazon/Netflix/Github emails button to simulate sending the emails
- Check the emails/ folder to see the result
- Open the link from one of the files
- Click on export button to export the data


## Screenshots
- Interface without data
![App Screenshot](https://raw.githubusercontent.com/Esdayl/Phisher/main/media/home-screen.png)

- Interface with test data
![App Screenshot](https://raw.githubusercontent.com/Esdayl/Phisher/main/media/test-campagn.png)


## Authors

- Valentin  Huyet
- Romain    Chevallier
- Bastien   Duplaix
- Marius    Mihai


## License

[MIT](https://choosealicense.com/licenses/mit/)


![Logo](https://logonews.fr/wp-content/uploads/2015/03/logo-epita-nb.jpg)

