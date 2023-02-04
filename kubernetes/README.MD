# KUBERNETES 
###### WHICH YOU DON'T WANT TO FORGET ;)


## ========================================================

## ===================== DEPLOYMENT ======================

## ========================================================

## CREAT

    kubectl create -f deployment_defination.yml
    

## CREATE WITH RECORD

    kubectl create -f deployment.yaml --record
    
    
## GET

    kubectl get deployments
    

## EDIT WITH RECORD
    
    kubectl edit -f deployment_defination.yml

## EDIT
    
    kubectl edit -f deployment_defination.yml --record

    
## UPDATE

    kubectl apply -f deployment_defination.yml
    
    
    kubectl set image deployment/myapp-deployment nginx=nginx:1.9.1    
    
## STATUS

    kubectl rollout status deployment/myapp-deployment


## ROLLOUT HISTORY
    
    kubectl rollout history deployment/myapp-deployment
    
    
## ROLLBACK

    kubectl rollout undo deployment/myapp-deployment
    
## DELETE

    kubectl delete deployment myapp-deployment
    
    
    
