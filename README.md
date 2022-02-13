# Set up postgres and pgadmin
docker-compose up

Wait ~30 seconds for pgadmin to be ready

access pgadmin at http://localhost:8080/

## pgadmin login:
username: charlesfauman@gmail.com
password: password

## database connection:
host: host.docker.internal
database: postgres
user: postgres
password: password

## Tools -> Query Tool

# Init python
`python3 -m venv venv`

`pip install -e .`

`pip install pip --upgrade`


# Check the database
https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-database
sudo apt install postgresql postgresql-contrib
psql --version