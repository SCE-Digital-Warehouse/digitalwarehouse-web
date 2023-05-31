# SCE DigitalWarehouse | DHT

## Requirements:
- Python v3.11 (at least)
- Windows 10

## Project installation and configuration:

#### Note: the project was tested on *Windows 10*

1. Install the latest version of Python on your environment ([instructions](https://docs.python.org/3/using/windows.html))
2. Open *Git Bash* and run the commands (you have to have permissions):
   - `git clone git@github.com:BS-PMC-2023/BS-PMC-2023-Team8.git`
   - `cd BS-PMC-2023-Team8`
   - `explorer .`
3. Now open a terminal inside the opened folder and run the commands:
   - `python -m venv .venv`
   - `.\.venv\Scripts\Activate`
   - `pip install --upgrade pip`
   - `pip install -r requirements.txt`
4. Now you are ready to run the project, the last step is to create a db and seed it, run these commands:
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