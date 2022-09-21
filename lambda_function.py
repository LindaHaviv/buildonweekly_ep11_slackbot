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
    
    req = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(req)
    data =  response.read()
    
    res = json.loads(data)
    stories = str(res[0])
    
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
    				"text": "*<https://{0}|{1}>*\n".format(res[0]["link"], res[0]["title"])
    			},
    			"accessory": {
    				"type": "image",
    				"image_url": res[0]["img"],
    				"alt_text": "tech"
    			}
    		},
    		{
    			"type": "divider"
    		}
    	]
    }
    
    print(stories)
    message = { "text": stories}
    
    req = urllib.request.Request(os.environ['WEBHOOK_URL'], json.dumps(response_body).encode('utf-8'), headers = hdrs)
    resp = urllib.request.urlopen(req)
    response = resp.read()
    
    