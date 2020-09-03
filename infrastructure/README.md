# AWS and K8s configuration resides here.
### AWS

Dont forget to update your DNS servers in the domanin name provider to those created in aws via terraform. 
You can retrieve them during the aws infrastructure creation from Route53 (NS records)

Update variables in `variables.tf` file and then execute:
```
terraform plan
terraform apply
```

Update your kubeconfig context with newly created EKS cluster
```
aws eks update-kubeconfig --name <clustername>
```

### Kubernetes
Apply files from `k8s/clusterconfig` to deploy argocd-server and other dependencies.  
```
kubectl apply -k k8s/clusterconfig
```
Now add clusterconfig and other remaining kubernetes deployments to argocd, so they will be deployed into the server
```
kubectl apply -f k8s/clusterconfig-argocd.yaml
kubectl apply -f k8s/mysql-argocd.yaml
kubectl apply -f k8s/postgres-argocd.yaml
kubectl apply -f k8s/flask-argocd.yaml
kubectl apply -f k8s/aiohttp-argocd.yaml
```