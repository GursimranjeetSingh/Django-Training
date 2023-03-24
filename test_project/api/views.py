from rest_framework.viewsets import ViewSet
from rest_framework.response import Response



class TestViewSet(ViewSet):
    #get
    def list(self,request):
        
        return Response({'test':'list'})
    
    #post
    def create(self,request):
        
        return Response({'test':'post'})
    
    #get
    def retrieve(self,request,pk=None):
        print(pk)
        
        return Response({'test':'restrieve'})
    
    # put 
    def update(self,request,pk=None):
        return Response({'test':'test'})
    
    #delete
    def destroy(self,request,pk=None):
        return Response({'test':'test'})


    #patch
    def partial_update(self,request,pk=None):
        return Response({'test':'partail_update'})
    





