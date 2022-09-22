import json
import urllib.request
import boto3
import os

def lambda_handler(event, context):
    
    url = os.environ['TECH_FEED']
    headers = {
            "X-RapidAPI-Key": os.environ['RAPIDAPI_KEY'],
            "X-RapidAPI-Host": os.environ['RAPIDAPI_HOST']
    }

    hdrs = {'Content-Type': 'application/json'}
    
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
          post_to_slack(item["link"], item["title"], item["img"])  


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
    
    