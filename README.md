# Let's Build a SlackApp on AWS 
Build on Weekly show on Twitch.tv/aws - episode 11

## Description

Building a [slack app](https://slack.com/apps) that shares Tech News articles when published to slack. This is a webhook app. We will use [AWS Lambda](https://aws.amazon.com/lambda/), [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon CloudWatch Events](https://aws.amazon.com/cloudwatch/) to build out the functionality. We will use tech news feeds from [Rapid API](https://rapidapi.com/hub)  

## Steps to follow along with Stream

### Step 1: Create a webhook app on slack 

* Create a slack workspace for testing
* Create a “channel” within the workspace
* Navigate to api.slack.com -> click "your apps"
* Choose webhook app & add to the webhook to a channel

### Step 2: Run the generated Curl command
* Copy the   curl  command generated by slack and run it in your Command Line App (ex. Terminal) to verify it’s working. You should see “Hello World” appear on slack.

### Step 3: Let’s create a Lambda function and send a “Hello World” message via lambda 
* Create a  new Lambda function with a Python runtime & Basic lambda role permissions
* Increase the default timeout of the lambda function to 15 or 30 seconds
* Test posting "Hello World" to the webhook endpoint (verify by seeing hellow world appear in slack channel)

### Step 4: Find a Tech News Feed
* For this demo we will use a [Tech News feed](https://rapidapi.com/athulsprakash-CxC2uBLxvsG/api/tech-news3/) from [Rapid API](https://rapidapi.com/hub ) — API Marketplace
* Generate RapidAPI keys
* Add the keys as environment variables in your lambda code

### Step 5: Let’s add the feed to our Lambda code
* Add the API keys to a header object 
* Test printing out the feed data to your lambda logs

### Step 6: Let’s send a sample story to slack
* Test sending one story from the API feed to slack with raw schema

### Step 7: Let’s format a sample data feed object using the slack [Block Kit Builder](https://api.slack.com/block-kit )
* Add the slack style formatted response template to your Lambda code (we called it response_body) & invoke to view sample output in slack

### Step 8: Create function to Loop through the data 
* Create a post_to_slack function that iterates through data posts and posts all the articles formatted to slack
* Add error handling

### Step 9: Create a database to check if an article was already sent by storing anything sent to slack
* Create a DynamoDB database and make the primary key a unique id (ex. we called it tech_news_id)
* Add the DynamoDB table name as an environment variable
* Update role linked in lambda with Dynamo permission
* Create a post_to_database function that posts the articles to the database & run "test" to verify it works

### Step 10: Update the post_to_database function to only post to slack if it's a new article
* add a condition that checks if the article is in the database by checking if the unique id is present - if it is not, it means it's a new article so post it to the database and to slack. Otherwise, don't post. 

### Step 11: Add a Cloudwatch event cron to automate triggering the Lambda 
* Allows you to pick an increment in which the lambda runs and checks if any new articles have been published. If there is a new article (the article does not appear in the database), it post to slack.
    

💡 Bonus: Add more tech news sources 

⭐ CONGRATS ON BUILDING A SLACK APP ON AWS! ⭐

_You can explore slack developer tools @ slack.dev_


