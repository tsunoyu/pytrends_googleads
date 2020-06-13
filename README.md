# <WIP> Automate adding Google Trends Keyword to Google Ads Search Campaigns

## Overview

This solution was created to automate the process of adding relevant Google Trends keyword into Google Ads Search Campaigns. It would help reducing some manual daily work and errors who is working or monitoring Search Campaings and Google Trends keywords. Main code is written in Python 3.7.

<img width="767" alt="スクリーンショット 2020-06-13 16 55 20" src="https://user-images.githubusercontent.com/62479342/84573368-02184280-ad98-11ea-905f-fffa9e1c5d69.png">

Detail Setup Process written in Medium.com -- [LINK](https://pypi.org/project/pytrends/)

## Important Notes
- This solution will **NOT** guaranty any Search Ads performace 
- pytrends API is not a Google Official API but it can be used for free
- Running the Python code daily basis will incur some Google Cloud cost
- It will not work if the the query does not have any volume to capture the trend Try to adjust the filter. ex) target from Global
- Consider adding filter or alert in Google Ads side to avoid sudden ads spend increase


## Products and APIs used for this solution

- pytrends -- [LINK](https://pypi.org/project/pytrends/)

  - API to get Google Trends data (not an official API by Google)

- Google Cloud

  - Google Cloud Function -- [LINK](https://cloud.google.com/functions/docs)
 
  - Google Cloud Pub/Sub -- [LINK](https://cloud.google.com/pubsub/docs/)
 
  - Google Cloud Scheduler -- [LINK](https://cloud.google.com/scheduler/docs/quickstart)
  
- Google Sheets API -- [LINK](https://developers.google.com/sheets/api)

- Google Ads Script -- [LINK](https://developers.google.com/google-ads/scripts/docs/your-first-script)

## Setup Guide

### Setup Google Spreasheet API Credencial
Enable the Google Sheets API from below link in order to save data you get from pytreds.
https://developers.google.com/sheets/api/quickstart/python

Save the file credentials.json. This file needs to be uploaded later into Google Cloud Function.

[Sample Credencial JSON file](https://github.com/tsunoyu/pytrends_googleads/blob/master/CREDENTIALS.JSON)

### Setup Google Cloud Pub/Sub

Create Google Cloud Pub/Sub Topic so that Google Cloud Function can be triggered.
This Topic will recieve message from Google Cloud Scheduler which we will set up in the following section.

<img width="714" alt="スクリーンショット 2020-06-13 17 44 44" src="https://user-images.githubusercontent.com/62479342/84574445-5faf8d80-ad9e-11ea-8c00-cda46d72022f.png">



### Setup Google Cloud Scheduler


### Setup Google Cloud Function


### Setup Google Ads Script
