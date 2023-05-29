# Project Name

This is a small api project for the scratchpay coding challenge via helm.

## Installation
Install helm


## Usage
helm template mychart . --show-only templates/postgres-cm.yaml | kubectl apply -f - 
helm install mychart . -f values.yaml  --set auth.postgresPassword=password