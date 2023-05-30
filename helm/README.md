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
After installing, create a secrets for postgres init and access
```
set +o history
kubectl create secret generic pgpasssecret --dry-run=client --from-literal=postgres-password=YOUR_PGADMIN_PASSWORD --from-literal=user-password=YOUR_USER_PASSWORD -o yaml >pgpasssecret.yaml
set -o history
kubeseal <pgpasssecret.yaml >pgpasssealedsecret.yaml
kubectl create -f pgpasssealedsecret.yaml
rm pgpasssecret.yaml
# Update the files/init.sql to have the same password as the same one as YOUR_USER_PASSWORD above
# Be sure to not commit changes to init.sql to git
kubectl create secret generic init-sealed --from-file=files/init.sql --dry-run=client -o yaml > init.yaml
kubeseal --format=yaml < init.yaml > init-sealed.yaml
kubectl create -f init-sealed.yaml
rm init.yaml
```


## Usage
The installation has been tested on Ubuntu 22 and microk8s.
For the sake of speed, we skipped the implementation of a load balancer and setting up ssl/tls, as well as helm tests.
These should be implemented before we go to production.
```
helm dependency update
helm install mychartrelease . -f values.yaml 
```