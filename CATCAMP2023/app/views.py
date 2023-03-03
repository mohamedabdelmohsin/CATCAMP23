from django.shortcuts import render
from .utils import USDEGPModule,IndomieModule

def index(request):
    return render(request, 'app/index.html')

def usd_to_egp(request):
 

 context={
        'usd_to_egp':USDEGPModule().get_price()
    }
 return render(request, 'app/usd-to-egp.html',context)

# psst, yes, you'll write code here :)


def live_indomie_price(request):
   

   x={
      'indomie_price':IndomieModule().get_price()
   }


   return render(request, 'app/live-indomie-price.html',x)


