import json
import boto3
dynamodb = boto3.resource('dynamodb')
table=dynamodb.Table('my-table')
""" def lambda_handler(event, context):
    response=table.get_item(Key={
        'id':'1'
    })
    views=response['Item']['views']
    views=views+1
    print(views)
    response=table.put_item(Item={
        'id':'1',
        'views':views
    })
    return views  """


def get_item():
    response = table.get_item(Key={'id': '1'})
    return response['Item']

def put_item(views):
    views = views + 1
    table.put_item(Item={'id': '1', 'views': views})
    return views

def lambda_handler(event, context):
    item = get_item()
    views = item['views']
    updated_views = put_item(views)
    return updated_views