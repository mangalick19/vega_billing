from pprint import pprint
from flask import render_template, url_for, flash, redirect, Response, request
from billing import app
from flask import request, Response, Flask
from environs import Env

#package imports
import os
import ast
import json
import logging


########################SWAGGER LIST#########################
#1. /api/v1/ping ----> health check
#2. /api/v1/
#############################################################


#test
@app.route("/api/v1/ping", methods = ['GET'])
def search_test():

    return_map = {}
    return_map['message'] = "pong"
    return Response(json.dumps(return_map), 200, mimetype='application/json')



@app.route("/api/v1/notebookcost", methods = ['GET'])
def getNotebookCost():
    notebook_type = request.args.get('type')
    notebook_region = request.args.get('region')
    cost = 0




    return str(cost)
