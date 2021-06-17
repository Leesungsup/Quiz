import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapi.settings")
import django
django.setup()
from myapi.models import Player_info
import requests
from bs4 import BeautifulSoup
import pandas as pd
def crawler():
    headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x32) AppleWebKit/536.35 (KHTML, like Gecko) Chrome/100.0.0.7 Safari/536.28"}
    url="https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop"
    response=requests.get(url,headers=headers)
    player_list=[]
    if response.status_code==200:
        soup=BeautifulSoup(response.content,'html.parser')
        string=soup.find_all('tr',{'class':['odd','even']})
    for info in string:
        number=imformation[0].get_text()
        information=info.find_all('td')
        number=information[0].get_text()
        name=information[3].get_text()
        position=information[4].get_text()
        age=information[5].get_text()
        nation=information[6].img['alt']
        team=information[7].img['alt']
        value=information[8].span['title']
        player_list.append([number,name,position,age,nation,team,value])
    df=pd.DataFrame(player_list,columns=['number','name','position','age','nation','team','value'])
    return df
if __name__=='__main__':
    recipe_data = crawler()
    for item in recipe_data:
        Search_Recipe(recipe_ID = item['recipe_ID'], recipe_Name = item['recipe_Name'], ingredient_Key = item['ingredient_Key']).save()