# EBazar

Simple ecommerce project.


## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.
python version 3.6
django version 2.2

### Create virtual environment
```bash
py -m venv env
```

### Activate virtual env
```bash
.\env\Scripts\activate
```

### Install packages
```bash
pip install -r requirements 
```


## Run

### Init Database
Create migrations
```bash
python manage.py makemigrations
```
Apply migrations
```bash
python manage.py migrate
```


### Add admin user
```bash
python manage.py createsuperuser
```
Enter username, email, passwork for user.






## License
[MIT](https://choosealicense.com/licenses/mit/)
