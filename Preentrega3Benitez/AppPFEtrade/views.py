from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppPFEtrade.models import Market, Buyer, Seller
from django.shortcuts import render, redirect



# Create your views here.

def market(request):
     
     return render(request, "AppPFEtrade/market.html")

def buyer(request):
    
    return render(request, "AppPFEtrade/buyer.html")

def seller(request):
    
    return render(request, "AppPFEtrade/seller.html")

def inicio(request):
    
   return render(request, "AppPFEtrade/inicio.html")

def prueba(request):
    
    return render(request, "AppPFEtrade/padre.html")

def marketForm(request):
    
    if request.method == "POST":
        
      market = Market(position=request.POST["pos"],
                      ticker=request.POST["tck"],
                      price=request.POST["pri"])
      
      market.save()
      
      return render(request, "AppPFEtrade/market.html")

    
    return render(request,"AppPFEtrade/marketform.html" )


def buyerForm(request):
    
    if request.method == "POST":
        
      market = Buyer(nombre=request.POST["name"],
                    apellido=request.POST["srname"],
                    mail=request.POST["mail"],
                    ticker=request.POST["tcker"],
                    precio=request.POST["price"])
      
      market.save()
      
      return render(request, "AppPFEtrade/buyer.html")

    
    return render(request,"AppPFEtrade/buyerform.html" )


def sellerForm(request):
    
    if request.method == "POST":
        
      market = Seller(nombre=request.POST["name"],
                    apellido=request.POST["srname"],
                    mail=request.POST["mail"],
                    ticker=request.POST["tcker"],
                    precio=request.POST["price"])
      
      market.save()
      
      return render(request, "AppPFEtrade/seller.html")

    
    return render(request,"AppPFEtrade/sellerform.html" )
  
  
def searchTicker(request):
  
  return render(request, "AppPFEtrade/market.html")
  
  
def matches(request): 
  
  if request.GET["ticker"]:
    
    ticker=request.GET["ticker"]
    markets = Market.objects.filter(ticker__iexact=ticker)
    
    return render(request, "AppPFEtrade/market.html", {"ticker" : ticker, "markets" : markets})
  
  else:
    
    res = "No fullfilled data!"
    
  return HttpResponse(res)

#Buscar / Mostrar

def searchSeller(request):
  
  ticker = Seller.objects.all()
  context = {"tickers" : ticker}

  return render(request, "AppPFEtrade/sellerupdate.html", context)

def searchBuyer(request):
  
  ticker = Buyer.objects.all()
  context = {"tickers" : ticker}

  return render(request, "AppPFEtrade/buyerupdate.html", context)

def searchMarket(request):
  
  ticker = Market.objects.all()
  context = {"tickers" : ticker}

  return render(request, "AppPFEtrade/marketupdate.html", context)


#Eliminar

def deleteMarket(request, marketPosition):
  
  position = Market.objects.get(position=marketPosition)
  position.delete()
  
  positions = Market.objects.all()

  context = {"position" : positions}
  
  return render(request,"AppPFE/marketupdate.html", context)


def deleteBuyer(request, buyerTicker):
  
  ticker = Buyer.objects.get(mail=buyerTicker)
  ticker.delete()
  
  tickers = Buyer.objects.all()

  context = {"ticker" : tickers}
  
  return render(request,"AppPFE/buyerupdate.html", context)

def deleteSeller (request, sellerTicker):
  
  ticker = Seller.objects.get(mail=sellerTicker)
  ticker.delete()
  
  tickers = Seller.objects.all()

  context = {"ticker" : tickers}
  
  return render(request,"AppPFE/sellerupdate.html", context)


#Editar


from django.views.generic.edit import UpdateView
from .models import Market
from .forms import MarketForm, SellerForm, BuyerForm

class MarketUpdateView(UpdateView):
  
    model = Market
    
    form_class = MarketForm
    
    template_name = 'AppPFEtrade/edit_market.html' 
    
    success_url = '/APPFE/market/'
    
    
class BuyerUpdateView(UpdateView):
  
    model = Buyer
    
    form_class = BuyerForm
    
    template_name = 'AppPFEtrade/edit_buyer.html' 
    
    success_url = '/APPFE/buyer/'
    

class SellerUpdateView(UpdateView):
  
    model = Seller
    
    form_class = SellerForm
    
    template_name = 'AppPFEtrade/edit_seller.html' 
    
    success_url = '/APPFE/seller/'



