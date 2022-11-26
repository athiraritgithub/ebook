# ebook
# django-rest-api
A REST api written in Django for people with deadlines

## Technologies used
* [Django]
* [DRF]


## Installation
* to run a build should install python globally .
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/athiraritgithub/ebook.git
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd ebookmanagement
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  venv -p python
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service using an api tester
    ```
        http://localhost:8000/ebooks/v1/users/accounts/signup
        
        for getting token
        http://localhost:8000/ebooks/v1/accounts/token/
        
        these are the api for crud functions
        
         http://localhost:8000/ebooks/v1/ebook
         http://localhost:8000/ebooks/v1/ebook/1
    ```
