from datetime import datetime
from domain.SystemMessages import SystemMessages
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from enviroment import keys

@api_view(['GET'])
def get_titles(request):

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

    if len(data_req) < 20:
        res_final = format_response(data_req)
        res_final.append({'Alert': 'The API return only '+ len(data_req)+' objects.'})
    else:
        firt_titles = data_req[0:20]
        res_final = format_response(firt_titles)
    
    with open('./logs/'+logs_name+'.txt', 'x') as f:
        f.write('timestamp: '+str_date+', HTTP status code: 200, raw: '+str(data_req))

    return Response(data=res_final, status=status.HTTP_200_OK)

@api_view (['GET'])
def invalid_token_response(request):
    return Response(status=status.HTTP_401_UNAUTHORIZED, data=SystemMessages.General.INVALID_TOKEN)
            
def format_response(api_response):
    response = []
    for item in api_response:
        formated_item = {
            'id': item['id'],
            'title': item['title']
        }
        response.append(formated_item)

    return response
