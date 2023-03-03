from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usd-to-egp/',views.usd_to_egp,name='usd_to_egp'),
    path('live-indomie-price/',views.live_indomie_price,name='live_indomie_price')

    # pssst, yes, you'll write code here :)
]