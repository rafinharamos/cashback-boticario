# cashback-challenge

Application to cashback for challenge.

## Technologies

In the development of this project, the following technologies were used:

- [Python 3.7](https://www.python.org/downloads/release/python-370/)
- [Pip 20.2](https://pip.pypa.io/en/stable/news/#id12) 
- [Django 3.1](https://docs.djangoproject.com/en/3.1/releases/3.1/)
- [Django Rest Framework 3.12](https://www.django-rest-framework.org/community/release-notes/#312x-series)
- [PostgreSQL 13](https://www.postgresql.org/about/news/postgresql-13-released-2077/) 
- [Docker 19.03](https://docs.docker.com/engine/release-notes/#version-1903) 

More details about all libraries used can be found in [requirements.txt](requirements.txt) file. 


## Documentation

You can find a postman collection for the API and do some tests at the root of the project (cashback_collections_api)

You can also have access to the complete system running on heroku at the address (https://cashback-boticario-app.herokuapp.com/)

You can have access to documentation in this address.

Note: *Note that the first request may take a while because it is a free service, so it goes to sleep mode when is not being used.*

## How to run - Docker (recommended)

To run this project over Docker container, everything you have to do is install Docker and 
run docker-compose (it comes with Docker by default). It will start automatically the API and PostgreSQL database, ready to use.

### Installation (docker)

To install Docker, visit [https://docs.docker.com/](https://docs.docker.com/) and follow the instructions related to your OS.

### Running (docker)

After install Docker, open your terminal/cmd, navigate to repository folder and execute the following command:

> docker-compose up --build

PS: even it's used only [Alpine images](https://hub.docker.com/_/alpine) to speed up the process, this command can take some minutes in the first time, 
since it will download postgres/python images and configure the whole environment. 
_So, it's perfect time to take a coffee_ 😅 
 
This command will start two containers:
- `db_1` the PostgreSQL container for database usage 
- `web_1` the Python container running Django application




