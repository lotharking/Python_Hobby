import json

print('Loading function')

def lambda_handler(event, context):
    """Lambda function developer for test the event parameters 
    in a request.
    The rute of the access to the lambda funciton is: 
    /test/transactions?transactionId=5&type=PURCHASE&amout=500
    """
    # 1. Parse out query string params
    transactionId = event['queryStringParameters']['transactionId']
    transactionType = event['queryStringParameters']['type']
    transactionAmout = event['queryStringParameters']['amout']

    print('transactionId='+transactionId)
    print('transactionType='+transactionType)
    print('transactionAmout='+transactionAmout)

    # 2. Construct the body of the response object
    transactionResponse = {}
    transactionResponse['transactionId'] = transactionId
    transactionResponse['transactionType'] = transactionType
    transactionResponse['transactionAmout'] = transactionAmout

    # 3. Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)

    # 4. Return the response object
    return responseObject
