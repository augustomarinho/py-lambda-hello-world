import json
import ptvsd

# Enable ptvsd on 0.0.0.0 address and on port 5890 that we'll connect later with our IDE
ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
ptvsd.wait_for_attach()
print('connected')
    
def lambda_handler(event, context):
    print("Hello from Lambda!")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }