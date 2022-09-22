# Let's Build a SlackApp on AWS 
Build on Weekly show on Twitch.tv/aws - episode 11

## Description

Building a [slack app](https://slack.com/apps) that shares Tech News articles when published to slack. This is a webhook app. We will use [AWS Lambda](https://aws.amazon.com/lambda/), [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon CloudWatch Events](https://aws.amazon.com/cloudwatch/) to build out the functionality. We will use tech news feeds from [Rapid API](https://rapidapi.com/hub)  

## Steps to follow along with Stream

### Step 1: Create a webhook app on slack 

* Create a slack workspace for testing
* Create a “channel” within the workspace
* Navigate to https://.slack.com/services/new
* Choose webhook app & add to a channel

### Step 2: Run the generated Curl command
* Copy the   curl  command generated by slack and run it in your Command Line App (ex. Terminal) to verify it’s working. You should see “Hello World” appear on slack.

### Step 3: Let’s create a Lambda function and send a “Hello World” message via lambda 

* Create a  new Lambda function with a Python runtime 
* Increase the default timeout of the lambda function


### Step 4: Find a Tech News Feed

* For this demo we will use a [Tech News feed] (https://rapidapi.com/athulsprakash-CxC2uBLxvsG/api/tech-news3/) from [Rapid API](https://rapidapi.com/hub ) — API Marketplace
* Generate RapidAPI keys

### Step 5: Let’s add the feed to our Lambda code

* Test printing out the feed data to lambda logs

### Step 6: Let’s send a sample story to slack

### Step 7: Let’s format a sample data feed object using the slack [Block Kit Builder] (https://api.slack.com/block-kit )

* Add the formatted response template to Lambda code & invoke to view sample in slack

### Step 8: Create function to Loop through the data 

* Create a post_to_slack function that posts all the articles to slack
* Add error handling

### Step 9: Create a database to check if an article was already sent by storing anything sent to slack

* Create. DynamoDB database and make the primary key a unique id (ex. we called it tech_news_id
* Add env table name variable
* Update role with dynamo permission
* Create a post_to_database function

### Step 10: Add a Cloudwatch event cron to automate triggering the Lambda 

* Allows you to pick an increment in which the lambda runs and checks if any new articles have been published. If there is a new article (the article does not appear in the database), it post to slack.
    

💡 Bonus: Add more tech news sources 

⭐ CONGRATS ON BUILDING A SLACK APP ON AWS! ⭐

_You can explore slack developer tools @ slack.dev_


