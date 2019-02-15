# Room Reservation Django App

Is a simple django app which allows for room managment with making a daily reservations for specified room


## Installation

Setup virtual envirnoment [virtualenv](https://virtualenv.pypa.io/en/latest/installation/)

Use at least Python 3.6.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all necessary libraries.

```bash
pip install -r requirements.txt
```

Install and setup postgres server on your computer. All required settings are located in settings.py [postgres](https://www.postgresql.org/docs/11/tutorial-install.html).

After postgres server is installed create required database. While in psql:

```bash
CREATE DATABASE contactlist;
```

Add some dummy data to se hows it works:
```bash
pg_dump -U postgres -h localhost -W contactlist > db_dump.sql
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Author

Air-t
