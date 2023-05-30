# Project Name

This is a small api project for the scratchpay coding challenge via helm.
For the sake of speed, we implemented sealed secret here. 
However, in production, a solution like kube-vault or a cloud provider's secret management service may be a better choice.


## Installation
Install helm and sealed secrets. Note that we are deploying sealed secret first/separately because the postgres chart depends on values stored in sealed secrets.
An example of installing helm chart:
```
helm repo add sealed-secrets https://bitnami-labs.github.io/sealed-secrets
helm install sealed-secrets -n kube-system --set-string fullnameOverride=sealed-secrets-controller sealed-secrets/sealed-secrets
```
An example of installing kubeseal is below 
(See more at https://github.com/bitnami-labs/sealed-secrets#installation):
```
wget https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.21.0/kubeseal-0.21.0-linux-amd64.tar.gz
tar -xvzf kubeseal-0.21.0-linux-amd64.tar.gz kubeseal
sudo install -m 755 kubeseal /usr/local/bin/kubeseal
```
After installing, create a secret for postgres user
```
kubectl create secret generic pgpasssecret --dry-run=client --from-literal=postgres-password=YOURPGADMINPASSWORD -o json >pgpasssecret.json
kubeseal <pgpasssecret.json >pgpasssealedsecret.json
kubectl create -f pgpasssealedsecret.json
```
ENCRYPTED_PG_PASS=$(echo -n "password" | kubeseal --raw --name apiusersecret --namespace default --scope cluster-wide --from-file=/dev/stdin)
sed -i 's/apiuserpgpass:.*/apiuserpgpass: "'$ENCRYPTED_PG_PASS'"/' values.yaml

## Usage
The installation has been tested on Ubuntu 22 and microk8s.
For the sake of speed, we skipped the implementation of a load balancer and setting up ssl/tls.
These should be implemented before we go to production.
```
helm install mychart . -f values.yaml 
```