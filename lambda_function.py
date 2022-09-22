import json
import urllib.request
import os
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['TABLE_NAME'])

    url = os.environ['TECH_FEED']
    headers = {
            "X-RapidAPI-Key": os.environ['RAPIDAPI_KEY'],
            "X-RapidAPI-Host": os.environ['RAPIDAPI_HOST']
    }

    hdrs = {'Content-Type': 'application/json'}

    def send_to_database (link, title, img, dateTime):
        try: 
            response = table.put_item(
                Item = {
                    'tech_news_id': dateTime.replace(" ", "") + "-" + title.replace(" ", ""),
                    'url': url,
                    'title': title
                },
                ConditionExpression='attribute_not_exists(tech_news_id)'
            )
            post_to_slack (link, title, img)
        except Exception as inst:
            print(inst)
            response = None
        return response

    def post_to_slack (link, title, img): 
        response_body = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":newspaper: New Story published on 9to5 Mac"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*<https://{0}|{1}>*\n".format(link, title)
                    },
                    "accessory": {
                        "type": "image",
                        "image_url": img,
                        "alt_text": "tech"
                    }
                },
                {
                    "type": "divider"
                }
            ]
        }
        
        req = urllib.request.Request(os.environ['WEBHOOK_URL'], json.dumps(response_body).encode('utf-8'), headers = hdrs)
        resp = urllib.request.urlopen(req)
        response = resp.read()
        print (response)
        
        
    try: 
        req = urllib.request.Request(url, headers = headers)
        response = urllib.request.urlopen(req)
    #if there is an error
    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        print('HTTPError: {}'.format(e.code))
    else:
        #iterate over the results
        data =  response.read()
        res = json.loads(data)
        for item in reversed(res):
            send_to_database(item["link"], item["title"], item["img"], item["dateTime"])  

