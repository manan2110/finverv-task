from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Meme
from .serializers import MemeSerializer

import requests

# Create your views here.


@api_view(["GET"])
def home(request):
    url = "https://api.imgflip.com/get_memes"
    response = requests.get(url)
    data = response.json()["data"]
    memes = data["memes"]
    for meme in memes:
        meme_object = Meme(
            id=meme["id"],
            name=meme["name"],
            url=meme["url"],
            width=meme["width"],
            height=meme["height"],
            box_count=meme["box_count"],
        )
        meme_object.save()
    memes = Meme.objects.all()
    serializer = MemeSerializer(memes, many=True)
    return Response(serializer.data)
