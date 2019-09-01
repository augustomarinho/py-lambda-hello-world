# Python Lambda Hello World

# Firs Steps
### Installing AWS CLI
	https://docs.aws.amazon.com/pt_br/cli/latest/userguide/install-linux.html#install-linux-path
	
### Installing SAM CLI
	https://docs.aws.amazon.com/pt_br/serverless-application-model/latest/developerguide/serverless-sam-cli-install-linux.html
	
### Debug with python
	https://docs.aws.amazon.com/pt_br/serverless-application-model/latest/developerguide/serverless-sam-cli-using-debugging-python.html
	
# Build Lambda code
    py-lambda-hello-world$ sam build
    
# Starting API Gateway locally
    py-lambda-hello-world$ sam local start-api -d 5890