#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
import sys
import os
import yaml
import requests
import json
import csv


app = Flask(__name__)

#load api credentials
my_apiconfig_yaml = os.environ['API_CONFIG'] + "/api_credentials.yaml"


tasks = [
    {
        'id': 'census',
        'url': u'http://api.census.gov/data/2014/zbp?get=EMP,EMPSZES,ESTAB,EMPSZES_TTL,NAICS2012_TTL,GEO_TTL&for=zipcode:10017&&key={0}',
        'description': u'This is census data from 2014 for zip code 10017',
    },
    {
        'id': 'another_api',
        'url': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    '''outputs a list of all apis'''
    return jsonify({'api_calls': tasks})


@app.route('/todo/api/v1.0/tasks/<string:task_id>', methods=['GET'])
def get_task(task_id):
    '''performs api request'''

    #grab api URL
    task = [task for task in tasks if task['id'] == task_id]
    url = (task[0]['url'])

    #grab api key from your YAML file
    try:
        from pyyaml import CLoader as Loader, CDumper as Dumper
    except ImportError:
        from yaml import Loader, Dumper
    with open(my_apiconfig_yaml, 'r') as f:
        api_credentials = yaml.load(f, Loader=Loader)

    #perform the api request
    api_key = api_credentials[task_id]['key']
    r = requests.get(url.format(api_key))
    data = r.json()

    #error handling
    if len(task) == 0:
        abort(404)
    return jsonify({'result': data})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
