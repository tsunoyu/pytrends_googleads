# <WIP> Automate adding Google Trends Keyword to Google Ads Search Campaigns

## Overview

This solution was created to automate the process of adding relevant Google Trends Rising and Top related queries into Google Ads Search Campaigns. It would help reducing some manual daily work and errors who is working or monitoring Search Campaings and Google Trends keywords. Main code is written in Python 3.7.

<img width="767" alt="スクリーンショット 2020-06-13 16 55 20" src="https://user-images.githubusercontent.com/62479342/84573368-02184280-ad98-11ea-905f-fffa9e1c5d69.png">

<img width="1009" alt="スクリーンショット 2020-06-13 18 24 59" src="https://user-images.githubusercontent.com/62479342/84575247-a3f15c80-ada3-11ea-92e3-dd9310b36c35.png">

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

### Setup Google Spreasheet and API Credencial

Create New Spreadsheet (or copy [this sample Spreadsheet](https://docs.google.com/spreadsheets/d/1JNCdYSTR_fenS6AB0_RJAZ50nmt96tTPG1WMVgOkBx4/edit#gid=0)) to store trending keywords you get from Google Trends.
The Spreadsheet needs following four tabs. 

- rising_brand
- rising_nonbrand
- top_brand
- top_nonbrand

The brand tab stores the queries which includes the keyword you are referencing and the non brand will store which doesn't include it.


**exammple)** You want to get Rising and Top related queries for **"toyota"**

In this case the brand keyword you reference is **"toyota"**
- rising_brand → "**toyota** camry 2020, ..."
- rising_nonbrand → "nissan sentra 2020, ..."
- top_brand → "**toyota** prius, ..."
- top_nonbrand → "hybrid car, ..."


Enable the Google Sheets API from below link in order to save data you get from pytreds.

https://developers.google.com/sheets/api/quickstart/python

Save the file credentials.json. This file needs to be uploaded later into Google Cloud Function.

[Sample Credencial JSON file](https://github.com/tsunoyu/pytrends_googleads/blob/master/CREDENTIALS.JSON)

### Setup Google Cloud Pub/Sub

Create Google Cloud Pub/Sub Topic so that Google Cloud Function can be triggered.
This Topic will recieve message from Google Cloud Scheduler which we will set up in the following section.

<img width="714" alt="スクリーンショット 2020-06-13 17 44 44" src="https://user-images.githubusercontent.com/62479342/84574445-5faf8d80-ad9e-11ea-8c00-cda46d72022f.png">



### Setup Google Cloud Scheduler

<img width="540" alt="スクリーンショット 2020-06-13 18 50 13" src="https://user-images.githubusercontent.com/62479342/84575766-aa81d300-ada7-11ea-94d4-2461c270ec27.png">


### Setup Google Cloud Function

<img width="545" alt="スクリーンショット 2020-06-13 19 14 26" src="https://user-images.githubusercontent.com/62479342/84576168-8d023880-adaa-11ea-82b6-698de4ab05f1.png">

### Setup Google Ads Script

<img width="907" alt="スクリーンショット 2020-06-13 19 08 30" src="https://user-images.githubusercontent.com/62479342/84576036-8c1cd700-ada9-11ea-92b9-4d59f04fdc9d.png">

Spreadsheet needs following four tabs. 

- rising_brand
- rising_nonbrand
- top_brand
- top_nonbrand

