# Setup
The application depends on Python building blocks and SQLite database engine. I suggest using [Virtualenv](https://virtualenv.readthedocs.org/en/latest/) and [Pip](https://pip.pypa.io/en/stable/) to set up the application's environment.
After the environment is ready, take these steps to prepare the app for Facebook event gathering.
- initialize database by starting python interactive shell and running `init_db` function from `database.py`
```python
>>> import database
>>> database.init_db()
```
- Set your Facebook app's credentials in `settings.py` and fill up the `PROFILES` list with desired profile data
- Run `python manage.py update_events` to insert the event data in the database
