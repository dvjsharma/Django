from django.http import HttpResponse

class MiddleWareLifeCycle:
    # Involed only once for the entire applicaton
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time initialization")
        
    # This is called for every request
    def __call__(self, request):
        print("This is before view")
        response = self.get_response(request)
        print("This is after view")
        return response
    
class ExceptionHandlingMiddleware:
    # Involed only once for the entire applicaton
    def __init__(self, get_response):
        self.get_response = get_response
        
    # This is called for every request
    def __call__(self, request):
        return self.get_response(request)
    
    def process_exception(self, request, exception):
        return HttpResponse("<h1>We are facing some issues, please check back in a few minutes</h1>")