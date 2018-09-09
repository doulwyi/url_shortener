# url_shortener

## Requirements
- Python 3.6
- Docker 

## How to run locally (or VMs)

- ```git clone https://github.com/doulwyi/url_shortener.git```
- ```cd url_shortener/```
- ```python -m venv .env ``` to create a virtual environment.
- ```pip instal -r requeriments.txt``` to install all dependencies. 
- ```python app.py```

## How to run using docker

- ```docker-compose up``` 



For scalability, I would use containers combine with kubernetes and cloud services
e.g. Google Cloud platform or AWS.

Since I'm using SQLAlchemy for this project, it is possible to connect any relational database. I've used SQLite
for this development and local testing, but I would recommend using postgreSQL since SQLite is not recommended for scale.
