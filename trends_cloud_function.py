################################################################################
# * Created a service account
# * Give SA access to the sheet
# * pip install -U gspread pytrends
# * pip freeze > requirements.txt
################################################################################

import datetime
import json
import base64
import gspread
from pytrends.request import TrendReq

DEFAULT_PARAMS = {
    'language': 'en-US',
    'location': 'US',
    'timezone': 360,
    'time_frame': 'now 1-d'
}


def get_params(json_message):
    params = {}
    params.update(DEFAULT_PARAMS)
    params.update(json_message)
    return params


def google_trend_data(query, params):
    pytrends = TrendReq(hl=params['language'],
                        tz=int(params['timezone']))

    kw_list = [query]
    pytrends.build_payload(kw_list,
                           timeframe=params['time_frame'],
                           geo=params['location'])
    daily_related_q = pytrends.related_queries()

    # Rising Trend Queries
    rising_q = daily_related_q[query]['rising']
    # Top Trend Queries
    top_q = daily_related_q[query]['top']

    results = {}

    if rising_q is None:
        print("no rising query")
    else:
        # exclude special characters
        rising_cleaned_q = rising_q.query('query.str.match("[a-zA-Z0-9\s]*$")', engine='python')
        # get data only for brand term
        rising_brand_kw = rising_cleaned_q.query(f'query.str.contains("{query}")', engine='python')
        # get data only for non-brand term
        rising_nonbrand_kw = rising_cleaned_q.query(f'query.str.match(\"(?!.*{query}.*)")', engine='python')

        results['rising_brand'] = rising_brand_kw['query'].tolist()
        results['rising_nonbrand'] = rising_nonbrand_kw['query'].tolist()

    if top_q is None:
        print("no top query")
    else:
        # same action for Top Trend Queries
        top_cleaned_q = top_q.query('query.str.match("[a-zA-Z0-9\s]*$")', engine='python')
        top_brand_kw = top_cleaned_q.query(f'query.str.contains("{query}")', engine='python')
        top_nonbrand_kw = top_cleaned_q.query(f'query.str.match(\"(?!.*{query}.*)")', engine='python')

        results['top_brand'] = top_brand_kw['query'].tolist()
        results['top_nonbrand'] = top_nonbrand_kw['query'].tolist()

    return results


def save_trends_to_ss(trends_obj, spreadsheet_key):
    if not trends_obj:
        return

    gc = gspread.service_account(filename='./credentials.json')
    workbook = gc.open_by_key(spreadsheet_key)
    today = datetime.date.today()

    if 'rising_brand' in trends_obj:
        sheet = workbook.worksheet('rising_brand')
        sheet.insert_row([str(today)] + trends_obj['rising_brand'], 2)

    if 'rising_nonbrand' in trends_obj:
        sheet = workbook.worksheet('rising_nonbrand')
        sheet.insert_row([str(today)] + trends_obj['rising_nonbrand'], 2)

    if 'top_brand' in trends_obj:
        sheet = workbook.worksheet('top_brand')
        sheet.insert_row([str(today)] + trends_obj['top_brand'], 2)

    if 'top_nonbrand' in trends_obj:
        sheet = workbook.worksheet('top_nonbrand')
        sheet.insert_row([str(today)] + trends_obj['top_nonbrand'], 2)


def handle_request(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    try:
        json_message = json.loads(pubsub_message)
    except:
        print('ERROR: I couldn\'t parse the message as JSON')
        return
    
    params = get_params(json_message)

    if 'query' not in params:
        print('query param is missing')
        return 'query param is missing', 400
    trends = google_trend_data(params['query'], params)

    if 'ss_key' in params:
        save_trends_to_ss(trends, params['ss_key'])
    return json.dumps(trends)
