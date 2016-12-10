
# coding: utf-8

# In[ ]:

import requests
import json
import sys

from operator import itemgetter

searchTerm=""

if len(sys.argv) < 2:
    print("Invalid Call to the Script/n")
    print("Usage: python <script_name> <search_term1> <search_term2>")
    sys.exit(2)
    
if len(sys.argv) > 5:
    print("Invalid Call to the Script/n")
    print("Usage: python <script_name> <search_term1> <search_term2> <search_term3> <search_term4>")
    print("You can specify a maximum of 4 search terms")
    sys.exit(2)        

flag=0
for i in range(1,len(sys.argv)):
    if not sys.argv[i].isalnum():
        flag=1
if flag==1:
    print("Invalid Search Term. Search Term can contain only Alphabets and Numbers")
    sys.exit(2)
        
    
if len(sys.argv) == 2:
    searchTerm = str(sys.argv[1])
elif len(sys.argv) == 3:
    searchTerm = str(sys.argv[1])+"%3B"+str(sys.argv[2])
elif len(sys.argv) == 4:
    searchTerm = str(sys.argv[1])+"%3B"+str(sys.argv[2])+"%3B"+str(sys.argv[3])
elif len(sys.argv) == 5:
    searchTerm = str(sys.argv[1])+"%3B"+str(sys.argv[2])+"%3B"+str(sys.argv[3])+"%3B"+str(sys.argv[4])
    
print(searchTerm)
temp=[]
listQuestions=[]

f=open('Analysis1.txt','w+')
f1=open('Analysis2.txt','w+')
f2=open('Analysis3.txt','w+')
f3=open('Analysis4.txt','w+')
f4=open('Analysis5.txt','w+')

for page in range(1,2):
    url="https://api.stackexchange.com/2.2/search?key=bSd75nhdHPb4nQOeqZnKpg((&intitle=pandas&site=stackoverflow&order=desc&sort=activity&pagesize=5&page="+str(page)
    response = requests.get(url)
    responseJson = response.json()
    list_json=responseJson["items"]
    temp+=list_json

for i in temp:
    dictQuestions={}
    dictQuestions["user_id"] = i["owner"]["user_id"]
    dictQuestions["title"] = i["title"]
    listQuestions.append(dictQuestions)
    
for i in range(0,5):
    urlProfile="https://api.stackexchange.com/2.2/users/"+str(listQuestions[i]["user_id"])+"/badges?order=desc&key=bSd75nhdHPb4nQOeqZnKpg((&sort=rank&site=stackoverflow&pagesize=10"
    responseProfile=requests.get(urlProfile)
    responseProfileJson=responseProfile.json()
    badgeCount=len(responseProfileJson["items"])
    badges=responseProfileJson["items"]
    silverCount=0
    bronzeCount=0
    goldCount=0
    for j in badges:
        if j["rank"]=="silver":
            silverCount+=1
        elif j["rank"]=="bronze":
            bronzeCount+=1
        elif j["rank"]=="gold":
            goldCount+=1
    listQuestions[i]["silverCount"]=silverCount            
    listQuestions[i]["goldCount"]=goldCount
    listQuestions[i]["bronzeCount"]=bronzeCount
    listQuestions[i]["badgeCount"]=badgeCount
    

print(listQuestions)    
sortedList=sorted(listQuestions,key=itemgetter("badgeCount"),reverse=True)
f.write(str(sortedList))


for i in range(0,len(listQuestions)):
    urlTags="https://api.stackexchange.com/2.2/users/"+str(listQuestions[i]["user_id"])+"/tags?order=desc&sort=popular&site=stackoverflow&key=bSd75nhdHPb4nQOeqZnKpg(("
    responseTags=requests.get(urlTags)
    responseTagsJson=responseTags.json()
    userTags=responseTagsJson["items"]
    tagsList=[]
    for j in userTags:
        tagsList.append(j["name"])
    listQuestions[i]["tags"]=tagsList
#print(listQuestions)


temp1=[]
for i in range(1,2):
    urlSearch="https://api.stackexchange.com/2.2/search?order=desc&key=bSd75nhdHPb4nQOeqZnKpg((&sort=activity&intitle="+searchTerm+"&pagesize=5&page="+str(i)+"&site=stackoverflow"
    #url="https://api.stackexchange.com/2.2/search?key=bSd75nhdHPb4nQOeqZnKpg((&intitle=pandas&site=stackoverflow&order=desc&sort=activity&pagesize=100&page="+str(page)
    responseSearch = requests.get(urlSearch)
    responseSearchJson = responseSearch.json()
    listSearchjson=responseSearchJson["items"]
    temp1+=listSearchjson

    
reputationList=[]    
for j in temp1:
    repuDict={}
    repuDict["reputation"]=j["owner"]["reputation"]
    repuDict["user_id"]=j["owner"]["user_id"]
    repuDict["link"]=j["owner"]["link"]
    reputationList.append(repuDict)
    

sortedReputationList=sorted(reputationList,key=itemgetter("reputation"),reverse=True)
f1.write(str(sortedReputationList))

totalSilverCount=0
totalGoldCount=0
totalBronzeCount=0
totalBadgesCount=0
for i in listQuestions:
    totalBadgesCount+=i["badgeCount"]
    totalBronzeCount+=i["bronzeCount"]
    totalGoldCount+=i["goldCount"]
    totalSilverCount+=i["silverCount"]
f2.write("Gold Count   : "+str(totalGoldCount))
f2.write("Silver Count : "+str(totalSilverCount))
f2.write("Bronze Count : "+str(totalBronzeCount))
f2.write("Badges Count : "+str(totalBadgesCount))

for i in range(0,len(listQuestions)):
    urlQue="https://api.stackexchange.com/2.2/users/"+str(listQuestions[i]["user_id"])+"/questions?order=desc&site=stackoverflow&pagesize=10&key=bSd75nhdHPb4nQOeqZnKpg(("
    urlAns="https://api.stackexchange.com/2.2/users/"+str(listQuestions[i]["user_id"])+"/answers?order=desc&site=stackoverflow&pagesize=10&key=bSd75nhdHPb4nQOeqZnKpg(("
    score=0
    scoreAns=0
    queResponse=requests.get(urlQue)
    ansResponse=requests.get(urlAns)
    jsonQue=queResponse.json()
    jsonAns=ansResponse.json()
    
    queUsers = jsonQue["items"]
    ansUsers = jsonAns["items"]
    for j in queUsers:
        score+=j["score"]
    for k in ansUsers:
        scoreAns+=k["score"]
    listQuestions[i]["score"]=score
    listQuestions[i]["scoreAns"]=scoreAns
mostDownVoted = sorted(listQuestions,key=itemgetter("score"),reverse=False)
mostUpVotedAns = sorted(listQuestions,key=itemgetter("scoreAns"),reverse=True)
f3.write(str(mostDownVoted))
f4.write(str(mostUpVotedAns))

