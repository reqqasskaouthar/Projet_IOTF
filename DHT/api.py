from .models import Dht11
from .serializers import DHT11serialize
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import rest_framework
@api_view(["GET","POST"])
def dhtser(request):
    if request.method=="GET":
        all=Dht11.objects.all()
        dataSer=DHT11serialize(all,many=True) # les donnée se form fichier JSON
        return Response(dataSer.data)
    elif request.method=="POST":
        serial=DHT11serialize(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.id, status=status.HTTP_400_CREATED)
from twilio.rest import Client
# Alertwhatsapp
account_sid = 'AC3e59d7204310fbfc850a1b64e5bbf1f0'
auth_token = 'e79e60a45d661390bfb47388ee901253'
client = Client(account_sid, auth_token)

message = client.messages.create(
 from_='whatsapp:+14155238886',
 body='Il y a une alerte importante sur votre Capteur la température dépasse le seuil',
 to='whatsapp:+212762742600'
)