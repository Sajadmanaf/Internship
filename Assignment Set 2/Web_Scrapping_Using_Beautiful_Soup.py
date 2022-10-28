#!/usr/bin/env python
# coding: utf-8

# ## Assignement 2 - Webscrapping using Beautiful Soup

# # 1. python program to display all the header tags from wikipedia.org.

# In[162]:


#importing Beautifulsoup
from bs4 import BeautifulSoup
import requests


# In[5]:



pg=requests.get('https://en.wikipedia.org/wiki/Main_Page')
pg


# In[6]:


soup=BeautifulSoup(pg.content)
soup


# In[7]:


headers=[]
for i in soup.find_all('span',class_='mw-headline'):
    headers.append(i.text.replace("'", '"'))

headers


# #  2. python program to display IMDB’s Top rated 100 movies

# In[8]:


pg1=requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')
pg1
pg2=requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt')
pg2


# In[9]:


soup1=BeautifulSoup(pg1.content)
print('*'*100, 'first 50', '*'*100)
print(soup1,'\n ')
print('*'*100, 'Second 50', '*'*100)
soup2=BeautifulSoup(pg2.content)
print(soup2,'\n ')


# In[14]:


movie_name = []
movie_year=[]

for i in soup1.find_all('h3',class_='lister-item-header'):
    movie_name.append(i.text.replace('\n','').split('.')[1][:-6])
    movie_year.append(i.text.replace('\n','').split('(')[1].replace(')',''))
for i in soup2.find_all('h3',class_='lister-item-header'):
    movie_name.append(i.text.replace('\n','').split('.')[1][:-6])
    movie_year.append(i.text.replace('\n','').split('(')[1].replace(')',''))
    
print(movie_name)
print('-*'*50)
print(movie_year)


# In[21]:


rating=[]
for i in soup1.find_all('div',class_="inline-block ratings-imdb-rating"):
    rating.append(i.text.replace('\n',''))
for i in soup2.find_all('div',class_="inline-block ratings-imdb-rating"):
    rating.append(i.text.replace('\n',''))
rating
len(rating)


# In[80]:


import pandas as pd
imdb= pd.DataFrame({'Movie Name':movie_name,'Year':movie_year,'IMDB rating':rating})
imdb


# # 3.Python program for IMDB’s Top rated 100 Indian movies’

# In[29]:


pg1= requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
pg1


# In[35]:


soup1=BeautifulSoup(pg1.content)
soup1


# In[71]:


movie_name = []
year=[]
j=0
for i in soup1.find_all('td',class_='titleColumn'):
    movie_name.append(i.text.replace('\n','').strip().split('.')[1].strip().split('(')[0])
    year.append(i.text.replace('\n','').strip().split('.')[1].strip().replace('(','').replace(')','')[-4:])
    j=j+1
    if j==100:
        break
movie_name
year


# In[74]:


ind_rating = []
j=0
for i in soup1.find_all('td', class_='ratingColumn imdbRating'):
    ind_rating.append(i.text.replace('\n',''))
    j=j+1
    if j==100:
        break
ind_rating


# In[79]:


df1= pd.DataFrame({'Movie_Name':movie_name, 'Release year':year, 'IMDB Rating':ind_rating})
df1


# # 4. python program to display list of respected former presidents of India

# In[81]:


pg4= requests.get('https://presidentofindia.nic.in/former-presidents.htm')
pg4


# In[82]:


soup1=BeautifulSoup(pg4.content)
soup1


# In[94]:


presidents =[]
duration=[]

for i in soup1.find_all('div',class_='presidentListing'):
    presidents.append(i.text.replace('\n','').split('(')[0])
    duration.append(i.text.replace('\n','').split('(')[1].split(':')[1].replace(' https','').replace(' http',''))
presidents
duration


# In[96]:


presidents_India = pd.DataFrame({'Name Of Indian Presidents':presidents,
                                'Duration(s) in Office': duration})
presidents_India


# # 5 a. Python Program for checking the ICC Cricket Team Ranking

# In[97]:


pg5= requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
pg5


# In[98]:


soup1=BeautifulSoup(pg5.content)
soup1


# In[144]:


odi_Team = []
matches = []
points=[]
rating=[]
l=0
m=0
n=0
for i in soup1.find_all('span',class_='u-hide-phablet'):
    odi_Team.append(i.text)
    l+=1
    if l==10:
        break
x=soup1.find('td',class_='rankings-block__banner--matches').text
y=soup1.find('td',class_='rankings-block__banner--points').text
z=soup1.find('td',class_='rankings-block__banner--rating u-text-right').text.replace('\n','').strip()
#matches.append(x)
realmatch=[]
realpoint=[]
realmatch.append(x) #points
realpoint.append(y) #matches
#points.append(y)
rating.append(z)
for j in soup1.find_all('td',class_='table-body__cell u-center-text'):
    matches.append(j.text)  
    m+=1
    if m==18:
        break    
count=0
for d in matches:
    if count %2==1:
        realpoint.append(d)
        count+=1
    elif count %2==0:
        realmatch.append(d)
        count+=1
for s in soup1.find_all('td',class_='table-body__cell u-text-right rating'):
    rating.append(s.text)
    del rating[10:]
    
print(odi_Team,'\n', realmatch,'\n',realpoint,'\n',rating)


# In[147]:


icc_top_ten=pd.DataFrame({'Team':odi_Team,
                         'Total Match':realmatch,
                         'Points':realpoint,
                         'Rating':rating})
icc_top_ten


# ## 5.b Program for Top 10 Batsman along with the Team

# In[167]:


pg6= requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')
pg6 


# In[168]:


soup1=BeautifulSoup(pg6.content)
soup1


# In[170]:


player=[]
player.append(soup1.find('div',class_="rankings-block__banner--name").text)
j=0
for i in soup1.find_all('td',class_="table-body__cell name"):
    if j==9:
        break
    else:
        player.append(i.text.replace('\n',""))
        j+=1
player


# In[181]:


team =[]
team.append(soup1.find('div',class_='rankings-block__banner--nationality').text.replace('\n','')[:-3].strip())
m=0
for i in soup1.find_all('span',class_='table-body__logo-text'):
    team.append(i.text.replace('\n',''))
    if len(team) ==10:
        break
team


# In[185]:


rating = []
rating.append(soup1.find('div',class_='rankings-block__banner--rating').text)
n=0
for i in soup1.find_all('td',class_='table-body__cell u-text-right rating'):
    rating.append(i.text)
    if len(rating)==10:
        break
rating


# In[186]:


odi_Batsman=pd.DataFrame({'Player Name':player, 
                         'Country':team,
                         'Rating':rating})
odi_Batsman


# ## 5.c Program to find the Bowler Name

# In[188]:


page=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')
page


# In[189]:


soup=BeautifulSoup(page.content)


# In[203]:


bowlers=[]
k=0
for i in soup.find_all('div',class_="rankings-block__banner--name"):
    k+=1
    bowlers.append(i.text)
    if k==2:
        break
bowlers.pop(0)
    
    
k=0
n=0
for i in soup.find_all('td',class_="table-body__cell name"):
    k+=1
    if k<10:
        continue
    bowlers.append(i.text.replace('\n',""))
    n+=1
    if n==9:
        break
    
bowlers


# In[205]:


point=[]

for i in soup.find_all('div',class_="rankings-block__banner--rating"):
    point.append(i.text)
        
wp=[]
wp=point[1]
point=[]
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    point.append(i.text.replace('\n',""))
        


point=point[9:18]
point.insert(0,wp)



point


# In[206]:


xteam=[]

for i in soup.find_all('div',class_="rankings-block__banner--nationality"):
    xteam.append(i.text.split('\n')[2])
        
wp=[]
wp=xteam[1]
xteam=[]
for i in soup.find_all('span',class_="table-body__logo-text"):
    xteam.append(i.text.replace('\n',""))
        
xteam=xteam[9:18]
xteam.insert(0,wp)
xteam


# In[207]:


df=pd.DataFrame({'Bowler':bowlers,'Team':xteam,'Rate':point})
df


# # 6a Womens ICC Cricket Team
# #WOmens Cricket Team
# 

# In[208]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
page


# In[209]:


soup=BeautifulSoup(page.content)


# In[210]:


wimrank=[]
#rank=soup.find('tr',class_="rankings-block__banner")
j=0
for i in soup.find_all('span',class_="u-hide-phablet"):
    if(j==10):
        break
    else:
        wimrank.append(i.text.replace('\n',""))
        j+=1

wimrank


# In[211]:


matches=[]
new_matches=[]
match=[]
j=0
match=( soup.find('td',class_="rankings-block__banner--matches").text)

for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    if(j==18):
        break
    else:
        new_matches.append(i.text.replace('\n',''))
        j+=1

matches=new_matches[::2]
matches.insert(0,match)
matches


# In[212]:


point=[]
new_point=[]
point_one=[]
j=0
point_one= soup.find('td',class_="rankings-block__banner--points").text

for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    if(j==18):
        break
    else:
        new_point.append(i.text.replace('\n',''))
        j+=1

point=new_point[1::2]
point.insert(0,point_one)
point


# In[213]:


rating=[]
rate=[]
j=0
rate=( soup.find('td',class_="rankings-block__banner--rating u-text-right").text.replace('\n','').replace('                            ',""))

for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    if(j==9):
        break
    else:
        rating.append(i.text.replace('\n',''))
        j+=1


rating.insert(0,rate)
rating


# In[216]:



data=pd.DataFrame({'Team Name':wimrank,'No of Matches':matches,'Point':point,'Rating':rating})
data


# # 6.b Top 10 women’s ODI Batting Players list

# In[217]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")
page


# In[218]:


soup=BeautifulSoup(page.content)


# In[219]:


people=[]
people.append(soup.find('div',class_="rankings-block__banner--name").text)
j=0
for i in soup.find_all('td',class_="table-body__cell name"):
    if j==9:
        break
    else:
        people.append(i.text.replace('\n',""))
        j+=1
people


# In[220]:


team=[]
team.append(soup.find('div',class_="rankings-block__banner--nationality").text.split('\n')[2])
j=0
for i in soup.find_all('span',class_="table-body__logo-text"):
    if j==9:
        break
    else:
        team.append(i.text.replace('\n',""))
        j+=1
team


# In[221]:


point=[]
point.append(soup.find('div',class_="rankings-block__banner--rating").text)
j=0
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    if j==9:
        break
    else:
        point.append(i.text.replace('\n',""))
        j+=1
point


# In[222]:


data=pd.DataFrame({'Player':people,'Team':team,'Point':point})
print("Top 10 players Team and Point")
data


# # 6c Top 10 ICC women All rounder 

# In[223]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")
page


# In[224]:


soup=BeautifulSoup(page.content)


# In[237]:


wplayers=[]
for i in soup.find_all('div',class_="rankings-block__banner--name"):
    wplayers.append(i.text)
del wplayers[0:2]


for i in soup.find_all('td',class_="table-body__cell name"):
    wplayers.append(i.text.replace('\n',""))
    
del wplayers[1:19]
#wplayers.insert(0,wp)
wplayers


# In[242]:


wteam=[]

for i in soup.find_all('div',class_="rankings-block__banner--nationality"):
    wteam.append(i.text.split('\n')[2])
del wteam[0:2]         


for i in soup.find_all('span',class_="table-body__logo-text"):
    wteam.append(i.text.replace('\n',""))
        
del wteam[1:19]
wteam


# In[243]:


wrate=[]

for i in soup.find_all('div',class_="rankings-block__banner--rating"):
    wrate.append(i.text)
del wrate[0:2]        

for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    wrate.append(i.text.replace('\n',""))
        
del wrate[1:19]

wrate


# In[244]:


data=pd.DataFrame({'Bowler':wplayers,'Team':wteam,'Rate':wrate})
data


# # 7. Python program to scrape mentioned news details from CNBC

# In[255]:


page=requests.get('https://www.cnbc.com/world/?region=world')
page


# In[256]:


soup=BeautifulSoup(page.content)
soup


# In[305]:


time= []
for i in soup.find_all('time', class_ = 'LatestNews-timestamp'):
    #print(i.text)
    time.append(i.text)


headline = []
for i in soup.find_all('a', class_ = 'LatestNews-headline'):
    #print(i.text)
    headline.append(i.text)
headline


# In[307]:


news_url= []
for i in soup.find_all('a', class_='LatestNews-headline' ):
    news_url.append(i['href'])
news_url


# In[308]:


cnbc=pd.DataFrame({'News':headline,
                  'Time':time,
                  'URL':news_url})
cnbc


# #    8.Python program to scrape the details of most downloaded articles from AI in last 90 days

# In[309]:


page=requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page


# In[310]:


soup=BeautifulSoup(page.content)
soup


# In[315]:


article_name =[]
for i in soup.find_all('h2',class_='sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR'):
    article_name.append(i.text)
article_name


# In[317]:


authors=[]
for j in soup.find_all('span',class_='sc-1w3fpd7-0 pgLAT'):
    authors.append(j.text)
authors


# In[318]:


published_date =[]
for k in soup.find_all('span',class_='sc-1thf9ly-2 bKddwo'):
    published_date.append(k.text)
    
published_date


# In[323]:


paper_url =[]
for m in soup.find_all('a',class_='sc-5smygv-0 nrDZj'):
    paper_url.append(m['href'])
paper_url


# In[324]:


ai = pd.DataFrame({'Article Name':article_name,
                  'Authors':authors,
                  'Published Date':published_date,
                  'Paper URL':paper_url})
ai


# # 9. Python program to scrape mentioned details from dineout.co.in

# In[325]:


page=requests.get('https://www.dineout.co.in/')
page


# In[326]:


soup=BeautifulSoup(page.content)
soup


# In[327]:


## I am  unable to access dineout.com, as I am located overseas.


# # 10. Python program to scrape the details of top publications from Google Scholar form

# In[328]:


page=requests.get('https://scholar.google.com/citations?view_op=top_venues&hl=en')
page


# In[329]:


soup=BeautifulSoup(page.content)
soup


# In[340]:


rank =[]
for i in soup.find_all('td',class_='gsc_mvt_p'):
    rank.append(i.text)
rank
publication = []
for j in soup.find_all('td',class_='gsc_mvt_t'):
    publication.append(j.text)
publication

h5_index=[]
for k in soup.find_all('a',class_='gs_ibl gsc_mp_anchor'):
    h5_index.append(k.text)
h5_index    
    
h5_median = []
for l in soup.find_all('span',class_='gs_ibl gsc_mp_anchor'):
    h5_median.append(l.text)
h5_median 

print(len(h5_median))


# In[341]:


gf=pd.DataFrame({'Rank':rank,
                'Publication':publication,
                'h5_index':h5_index,
                'h5_Mesian':h5_median})
gf


# In[ ]:




