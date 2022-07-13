from django.shortcuts import redirect
from enviroment import keys

class CheckAutorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        
        self.request = request
        path = self.request.path_info.lstrip('/')
        if path == 'api/access_denied/':
            return

        self.req_header = self.request.META
        baerer_token = self.req_header.get('HTTP_AUTHORIZATION')
        
        if baerer_token == None:
            return redirect('/api/access_denied')
        
        token_real = keys.token

        if len(baerer_token.split('Bearer ')) == 1:
            return redirect('/api/access_denied')
        
        token = baerer_token.split('Bearer ')[1]

        if token != token_real:
            return redirect('/api/access_denied')
        

        


            


        