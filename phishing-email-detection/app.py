try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from io import BytesIO
import csv
import sys, os, base64, datetime, hashlib, hmac 
from chalice import Chalice
from chalice import NotFoundError, BadRequestError


import sys, os, base64, datetime, hashlib, hmac 
app = Chalice(app_name='phishing-email-detection')
app.debug = True

try:
    from urlparse import urlparse, parse_qs
except ImportError:
    from urllib.parse import urlparse, parse_qs

import boto3
sagemaker = boto3.client('sagemaker-runtime')

@app.route('/', methods=['POST'], content_types=['application/x-www-form-urlencoded'])
def handle_data():
    d = parse_qs(app.current_request.raw_body)
    # data to csv

    try:
        my_dict = {k:float(v[0]) for k, v in d.iteritems()}
    except AttributeError:
        my_dict = {k:float(v[0]) for k, v in d.items()}
    f = StringIO()
    w = csv.DictWriter(f, my_dict.keys())
    #w.writeheader()
    w.writerow(my_dict)
    res = sagemaker.invoke_endpoint(
                    EndpointName='phishing-email-detection',
                    Body=f.getvalue(),
                    ContentType='text/csv',
                    Accept='Accept'
                )
    return res['Body'].read()
