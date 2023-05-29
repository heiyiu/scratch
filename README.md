# Project Name

This is a small api project for the scratchpay coding challenge.

## Installation
You need to have docker or docker desktop installed, as well as docker-compose.
Due to time constrains, the project utilizes docker secret, but for production use,
we should utilize key management solution like Hashicorp Vault and AWS Secret Manager.


Create a pg_user_password.txt file in the same directory and store the password for the database user.
Adjust the POSTGRES_USER and POSTGRES_DB to desired values.


The deployment has been tested with docker and docker-compose on an ubunut environment.
It may not work correctly with podman/podman-compose due to networking and permission issues.
```
docker compose up -d --build
```

## Documentation
After spinning up the stack, documentation are available at this endpoint via a web browser:
http://YOUR_PUBLIC_IP:8000/docs
