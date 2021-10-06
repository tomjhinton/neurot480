from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import random
from dotenv import load_dotenv
import tweepy
import os
import io
import sys
import numpy as np
import PIL
from PIL import Image, ImageFont
import matplotlib.pylab as plt
import matplotlib.colors as mclr
from random import randint


from quote import quote

search = 'William Gibson'
result = quote(search)


quote_font = ImageFont.truetype('FerriteCoreDX-Regular.ttf', 52)
quote_text = result[randint(0, len(result)-1)]['quote']



def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

def create(CL, rshift):


    imarray = np.random.rand(900,1600,3) * 255

    im2 = Image.fromarray(imarray.astype('uint8')).convert('RGBA')




    draw = ImageDraw.Draw(im2)
    for i in range(randint(0, 500)):
        draw.rectangle(((randint(0, 1000), randint(0, 1600)), (randint(0, 1000), randint(0, 1600))), outline= tuple(np.random.randint(256, size=3)) + (60,), width=100)
        draw.ellipse((randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000)), outline=tuple(np.random.randint(256, size=3)), width=100)
        draw.arc([ (randint(0, 1000), randint(0, 1000)), (randint(0, 1000), randint(0, 1000))], randint(0, 360), randint(0, 360), fill=tuple(np.random.randint(256, size=3)), width=20)


    for i in range(randint(50, 100)):
        im2 = im2.filter(ImageFilter.BLUR)
        im2 = im2.filter(ImageFilter.DETAIL)
        im2 = im2.filter(ImageFilter.EDGE_ENHANCE_MORE)


    offset = 0
    draw = ImageDraw.Draw(im2)
    i = quote_text.split(" ")
    for ix in i:
            draw.multiline_text((15+offset,15+ offset), ix, (255, 255, 255), font=quote_font)
            offset += 50


    c_k = os.getenv("API_key")
    c_s = os.getenv("API_secret_key")
    a_k = os.getenv("Access_token")
    a_s = os.getenv("access_token_secret")
    auth = tweepy.OAuthHandler(c_k, c_s)
    auth.set_access_token(a_k, a_s)
    api = tweepy.API(auth)

    buf = io.BytesIO()
    im2.save(buf, format='PNG')
    thing = buf.getvalue()
    test = api.media_upload('28.png',file= buf)
    api.update_status(status='#creativecoding #codeart #generativeart #computerart #glitchart', media_ids=[test.media_id])

create(CL=181, rshift=3)
