# Project Name

This is a small api project for the scratchpay coding challenge via helm.
For the sake of speed, we implemented sealed secret here. 
However, in production, a solution like kube-vault or a cloud provider's secret management service.


## Installation
Install helm and sealed secrets. An example of installing sealed secrets is below 
(See more at https://github.com/bitnami-labs/sealed-secrets#installation):
```
wget https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.21.0/kubeseal-0.21.0-linux-amd64.tar.gz
tar -xvzf kubeseal-0.21.0-linux-amd64.tar.gz kubeseal
sudo install -m 755 kubeseal /usr/local/bin/kubeseal
```
After installing, create a secret for postgres
```
kubeseal --fetch-cert \
--controller-name=mychart-sealed-secrets \
--controller-namespace=default \
> pub-cert.pem

echo -n YOUR_PASSWORD_HERE | kubectl create secret generic pgpasssecret --dry-run=client --from-file=foo=/dev/stdin -o json >pgpasssecret.json

```

The installation has been tested on Ubuntu 22


## Usage
# helm template mychart . --show-only templates/postgres-cm.yaml | kubectl apply -f - 
helm install mychart . -f values.yaml  --set auth.postgresPassword=YOUR_ADMIN_PASSWORD