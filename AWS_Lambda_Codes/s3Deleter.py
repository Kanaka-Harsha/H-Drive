import json
import boto3

s3_client = boto3.client('s3')
bucket_name = 'hs3-storage'

def lambda_handler(event, context):
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type,Authorization',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,DELETE'
            },
            'body': json.dumps('CORS Preflight JSON')
        }

    try:
        if 'body' not in event:
            return {
                'statusCode': 400,
                'headers': { 'Access-Control-Allow-Origin': '*' },
                'body': json.dumps('Missing request body')
            }
            
        body = json.loads(event['body'])
        filename = body.get('filename')
        
        if not filename:
            return {
                'statusCode': 400,
                'headers': { 'Access-Control-Allow-Origin': '*' },
                'body': json.dumps('Missing filename (key) in request body')
            }
        s3_client.delete_object(
            Bucket=bucket_name,
            Key=filename
        )

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,DELETE'
            },
            'body': json.dumps({
                'message': f'Successfully deleted {filename}',
                'filename': filename
            })
        }

    except Exception as e:
        print(f"Error deleting object: {str(e)}")
        return {
            'statusCode': 500,
            'headers': { 'Access-Control-Allow-Origin': '*' },
            'body': json.dumps(f"Internal Server Error: {str(e)}")
        }
