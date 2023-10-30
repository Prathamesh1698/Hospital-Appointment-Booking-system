def middleware(get_response):
    print("code need to be executed only once")
    
    def my_middleware(request):
        print("code to be executed before views function calls. ")
        print("Programcontrol is in my_middleware func")
        
        res=get_response(request)
        
        print("code to be executed  after view function called.")
        print("Program control is in my_middleware func after view called")
        
        return res
    
    return my_middleware