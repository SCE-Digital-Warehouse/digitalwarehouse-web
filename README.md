# SCE Digital Warehouse

## Requirements:
- Python v3.11 (at least)
- Windows 10

## Project installation and configuration:

#### Note: the project was tested on *Windows 10* with *Python v3.11* and *Django 4.1.7*

1. Install the latest version of Python on your environment ([instructions](https://docs.python.org/3/using/windows.html))
2. Open *Git Bash* and run the commands (you have to have permissions):
   - `git clone git@github.com:BS-PMC-2023/BS-PMC-2023-Team8.git`
   - `cd BS-PMC-2023-Team8`
   - `explorer .`
3. Now open a terminal inside the opened folder and run the commands:
   - `pip install --upgrade pip`
   - `python -m venv .venv`
   - `.\.venv\Scripts\Activate`
   - `pip install -r requirements.txt`
4. Now you are ready to start, the last step is to create a db and seed it, run these commands:
    - `python manage.py makemigrations`
    - `python manage.py migrate`
    - `python manage.py seed`
5. Run the project:
    - `python manage.py runserver`
6. The site is available at your [localhost](http://127.0.0.1:8000/)
7. Now you can login as:
    - **Superuser:**
        - username: `root`
        - password: `sce123456`
    - **Warehouse Manager:**
        - username: `manager_dht`
        - password: `sce123456`
    - **Moderator:**
        - username: `mod_dht`
        - password: `sce123456`
   - **Regular User:**
        - username: `regular_user`
        - password: `sce123456`
  
## Adding amount of users from the `.csv` file

##### You can add amount of users from your `.csv` file, to do so:

1. Create a `.csv` file and add the data in the format:

    `"identity_num","first_name","last_name","mobile_num","email","role"`

    where:

    - **identity_num** is a 9-digit string
    - **first_name**, **last_name** are strings consisting of letters only
    - **mobile_num** is a 10-digit string that starts with `05`
    - **email** is a string where after the `@` it can only have `sce.ac.il` or `ac.sce.ac.il`
    - **role** is a string with one of these values: `student`, `lecturer`

    ##### Example of the `.csv` file:

    `"identity_num","first_name","last_name","mobile_num","email","role"
    "372047254","John","Kek","0547382956","kek@ac.sce.ac.il","student"
    "235513229","Rar","Sas","0532145219","lol@ac.sce.ac.il","student"
    "925345765","Ch","Zh","0521245563","fp@sce.ac.il","lecturer"
    "284760485","Avh","Droc","0591537859","rey@ac.sce.ac.il","student"
    "865612168","Irvin","Rer","0591235497","yhk@ac.sce.ac.il","student"`

2. Go to the [users](http://localhost:8000/users/) page and click on the `הוספת כמות משתמשים` button
3. Then choose your `.csv` file

##### If the provided data is correct, the user entries will be created and added to the db and you will see the updated list of users.

## Testing

#### In order to run tests:
1. `python manage.py runserver`
2. `python manage.py test base`

##### Note: you have the virtual environment to be activated: `.\.venv\Scripts\Activate`