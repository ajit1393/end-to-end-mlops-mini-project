import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/ajit1393/end-to-end-mlops-mini-project.mlflow') 
dagshub.init(repo_owner='ajit1393', repo_name='end-to-end-mlops-mini-project', mlflow=True) 
 
with mlflow.start_run(): 
    mlflow.log_param('parameter name', 'value') 
    mlflow.log_metric('metric name', 1)