# Project Name

This is a small smoke test that can be run to verify the api server after deployment

## Installation
You need to have docker or docker desktop installed 
```
docker build -t scratch/apitest:0.0.1 .
```

## Usage
Substitue the network name with the network name that the docker-compose stack is running in.
The default should be scratch_sp_api
```
docker run --network YOUR_API_STACK_NETWORK scratch/apitest:0.0.1
```