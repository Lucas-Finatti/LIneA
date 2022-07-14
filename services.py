import requests
from rest_framework.response import Response
from rest_framework import status
from domain.SystemMessages import SystemMessages
from datetime import datetime
from enviroment import keys
import json


def format_response_all(api_response):
    response = []

    for item in api_response:
        formated_item = {
            'userId': item['userId'],
            'id': item['id'],
            'title': item['title'],
            'completed': item['completed']
        }
        response.append(formated_item)

    return response

def format_response_id(api_response):
    response = []

    for item in api_response:
        formated_item = {
            'id': item['id'],
            'title': item['title']
        }
        response.append(formated_item)

    return response


def format_response_param_id(api_response):

    response = format_response_id(api_response)
    response_final = sorted(response, key=lambda x: x['id'])

    return response_final

def format_response_param_user_id(api_response):

    response = format_response_all(api_response)
    response_final = sorted(response, key=lambda x: x['userId'])

    return response_final

def format_response_param_completed(api_response):

    response = format_response_all(api_response)
    response_final = sorted(response, key=lambda x: x['completed'])

    return response_final

def verify_status_cd():
    date = datetime.now()
    str_date = date.strftime("%d/%m/%Y, %H:%M:%S")
    logs_name = date.strftime("%d_%m_%Y__hr_%H_min_%M_sec_%S")
    res_final = {}
    firt_titles = None 
    request = requests.get(f""+ keys.api_url)

    if request.status_code == 404:
         return Response(status=status.HTTP_404_NOT_FOUND, data=SystemMessages.General.SERVER_NOT_FOUND)
    
    if request.status_code == 500:
        with open('./logs/'+logs_name+'.txt', 'x') as f:
            f.write('timestamp: '+str_date+', HTTP status code: 500, raw: None')
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data=SystemMessages.General.COULD_NOT_CONNECT_TO_SERVER)
    
    data_req = json.loads(request.content)
    return data_req, logs_name, str_date

def search(response, type_param, param):
    
    res_final = []

    if type_param == 'id':
        for dict in response:
            if str(dict['id']) == param:
                res_final.append(dict)
    elif type_param == 'user_id':
        for dict in response:
            if str(dict['userId']) == param:
                res_final.append(dict)
    elif type_param == 'completed':
        for dict in response:
            if str(dict['completed']) == param:
                res_final.append(dict)
    else:
        response = 400
        return response

    res_final = format_response_id(res_final)

    return res_final

def sort_id():
    request = verify_status_cd()
    data_req = request[0]
    logs_name = request[1]
    str_date = request[2]

    if len(data_req) < 20:
        res_final = format_response_param_id(data_req)
        res_final.append({'Alert': 'The API return only '+ len(data_req)+' objects.'})
    else:
        firt_titles = data_req[0:20]
        res_final = format_response_param_id(firt_titles)

    with open('./logs/'+logs_name+'.txt', 'x') as f:
        f.write('timestamp: '+str_date+', HTTP status code: 200, raw: '+str(data_req))

    res_final = format_response_id(res_final)

    return res_final



def sort_user_id():
    request = verify_status_cd()
    data_req = request[0]
    logs_name = request[1]
    str_date = request[2]

    if len(data_req) < 20:
        res_final = format_response_param_user_id(data_req)
        res_final.append({'Alert': 'The API return only '+ len(data_req)+' objects.'})
    else:
        firt_titles = data_req[0:20]
        res_final = format_response_param_user_id(firt_titles)

    with open('./logs/'+logs_name+'.txt', 'x') as f:
        f.write('timestamp: '+str_date+', HTTP status code: 200, raw: '+str(data_req))
    
    res_final = format_response_id(res_final)

    return res_final

def sort_completed():
    request = verify_status_cd()
    data_req = request[0]
    logs_name = request[1]
    str_date = request[2]

    if len(data_req) < 20:
        res_final = format_response_param_completed(data_req)
        res_final.append({'Alert': 'The API return only '+ len(data_req)+' objects.'})
    else:
        firt_titles = data_req[0:20]
        res_final = format_response_param_completed(firt_titles)

    with open('./logs/'+logs_name+'.txt', 'x') as f:
        f.write('timestamp: '+str_date+', HTTP status code: 200, raw: '+str(data_req))
    
    res_final = format_response_id(res_final)

    return res_final

def get_titles():

    request = verify_status_cd()
    data_req = request[0]
    logs_name = request[1]
    str_date = request[2]

    if len(data_req) < 20:
        res_final = format_response_id(data_req)
        res_final.append({'Alert': 'The API return only '+ len(data_req)+' objects.'})
    else:
        firt_titles = data_req[0:20]
        res_final = format_response_id(firt_titles)
    
    with open('./logs/'+logs_name+'.txt', 'x') as f:
        f.write('timestamp: '+str_date+', HTTP status code: 200, raw: '+str(data_req))
    
    return res_final

def api_sort(type_param):
    if type_param == 'id':
        res_final = sort_id()

    elif type_param == 'user_id':
        res_final = sort_user_id() 

    elif type_param == 'completed':
        res_final = sort_completed()
    else:
        res_final = []

    return res_final
        
def api_search(type_param ,param):
    request = verify_status_cd()
    data_req = request[0]
    logs_name = request[1]
    str_date = request[2]

    if len(data_req) < 20:
        res_final = format_response_param_completed(data_req)
        res_final.append({'Alert': 'The API return only '+ len(data_req)+' objects.'})
    else:
        firt_titles = data_req[0:20]
        res_final = format_response_param_completed(firt_titles)
    
    res_final = search(res_final, type_param, param)

    with open('./logs/'+logs_name+'.txt', 'x') as f:
        f.write('timestamp: '+str_date+', HTTP status code: 200, raw: '+str(data_req))
    
    return res_final