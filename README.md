# URL Shortener 
Built on Python3 and deployed in AWS
### Application is managed via [ArgoCD](https://argoproj.github.io/argo-cd/) inside the EKS (kubernetes) cluster

You can use any part of this project as an example for your own projects or infrastructure configuration 

This is a demo project.  
**Don't use kubernetes** for a single app just because "having your application on kubernetes is fancy"..  this is how your app might look like by doing that (or how actually this **url-shortener** project looks like on k8s 😉😇):  

<img src="./images/k8s-truck.jpg" alt="drawing" width="500"/>

### Manage your AWS resources and your wallet wisely. 

## API
This project contains two approaches of implementation: using [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Aiohttp](https://docs.aiohttp.org/en/stable/)  

## Infrastructure

All AWS infrastructure creation is automated via [Terraform](https://www.terraform.io/)  
All Kubernetes apps are backed-up by [ArgoCD](https://argoproj.github.io/argo-cd/)