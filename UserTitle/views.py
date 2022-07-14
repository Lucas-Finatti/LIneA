from domain.SystemMessages import SystemMessages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from services import api_sort, api_search, get_titles


@api_view(['GET'])
def api(request):
    url_params = request.query_params
    type_function = url_params['type_function'] 
    type_param = url_params['type_param']
    param = url_params['param']

    if type_function == 'sort':
        res_final = api_sort(type_param)

        if res_final == []:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=SystemMessages.General.INVALID_QUERY_PARAMETER)

        return Response(data=res_final, status=status.HTTP_200_OK)

    elif type_function == 'search':

        res_final = api_search(type_param, param)

        if res_final == 400:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=SystemMessages.General.INVALID_QUERY_PARAMETER)

        if res_final == []:
            return Response(status=status.HTTP_200_OK, data=SystemMessages.General.QUERY_PARAMETER_NOT_FOUND)

        return Response(data=res_final, status=status.HTTP_200_OK)

    elif type_function == 'all':
        res_final = get_titles()

        return Response(data=res_final, status=status.HTTP_200_OK)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data=SystemMessages.General.INVALID_QUERY_PARAMETER)

@api_view (['GET'])
def invalid_token_response(request):
    return Response(status=status.HTTP_401_UNAUTHORIZED, data=SystemMessages.General.INVALID_TOKEN)
            

