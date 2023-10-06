from django import forms
from .models import Market, Buyer, Seller



class MarketForm(forms.ModelForm):
    
    class Meta:
        
        model = Market
        fields = '__all__'
        

class BuyerForm(forms.ModelForm):
    
    class Meta:
        
        model = Buyer
        fields = '__all__'

class SellerForm(forms.ModelForm):
    
    class Meta:
        
        model = Seller
        fields = '__all__'