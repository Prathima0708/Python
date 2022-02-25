import json
import os
from unittest import result
import requests
import pandas
from copy import deepcopy
import time


url = "https://api.traceable.ai/graphql"

payload="{\"query\":\"{\\r\\n  events(\\r\\n    limit: 1\\r\\n    between: {startTime: \\\"2022-01-03T07:13:42.277Z\\\", endTime: \\\"2022-02-03T07:13:42.277Z\\\"}\\r\\n    filterBy: [{keyExpression: {key: \\\"id\\\"}, operator: EQUALS, value: \\\"6347097f-3115-46fc-94b7-3ebb8d4eab47\\\", type: ATTRIBUTE}, {keyExpression: {key: \\\"securityEventCategory\\\"}, operator: NOT_EQUALS, value: \\\"INTERNAL\\\", type: ATTRIBUTE}, {keyExpression: {key: \\\"securityEventCategory\\\"}, operator: NOT_EQUALS, value: \\\"TAGGED\\\", type: ATTRIBUTE}]\\r\\n  ) {\\r\\n    results {\\r\\n      id\\r\\n      name: attribute(expression: {key: \\\"name\\\"})\\r\\n      timestamp: attribute(expression: {key: \\\"timestamp\\\"})\\r\\n      type: attribute(expression: {key: \\\"type\\\"})\\r\\n      spanId: attribute(expression: {key: \\\"spanId\\\"})\\r\\n      apiId: attribute(expression: {key: \\\"apiId\\\"})\\r\\n      apiName: attribute(expression: {key: \\\"apiName\\\"})\\r\\n      apiUri: attribute(expression: {key: \\\"apiUri\\\"})\\r\\n      category: attribute(expression: {key: \\\"category\\\"})\\r\\n      serviceId: attribute(expression: {key: \\\"serviceId\\\"})\\r\\n      serviceName: attribute(expression: {key: \\\"serviceName\\\"})\\r\\n      eventDescription: attribute(expression: {key: \\\"eventDescription\\\"})\\r\\n      actorEntityId: attribute(expression: {key: \\\"actorEntityId\\\"})\\r\\n      actorName: attribute(expression: {key: \\\"actorName\\\"})\\r\\n      actorIpAddress: attribute(expression: {key: \\\"actorIpAddress\\\"})\\r\\n      actorDevice: attribute(expression: {key: \\\"actorDevice\\\"})\\r\\n      actorSession: attribute(expression: {key: \\\"actorSession\\\"})\\r\\n      securityScoreCategory: attribute(expression: {key: \\\"securityScoreCategory\\\"})\\r\\n      securityEventCategory: attribute(expression: {key: \\\"securityEventCategory\\\"})\\r\\n      securityEventTypeId: attribute(expression: {key: \\\"securityEventTypeId\\\"})\\r\\n      spanStartTimestamp: attribute(expression: {key: \\\"spanStartTimestamp\\\"})\\r\\n      actorCountry: attribute(expression: {key: \\\"actorCountry\\\"})\\r\\n      actorState: attribute(expression: {key: \\\"actorState\\\"})\\r\\n      actorCity: attribute(expression: {key: \\\"actorCity\\\"})\\r\\n      SERVICE: entity(type: \\\"SERVICE\\\") {\\r\\n        id: attribute(expression: {key: \\\"id\\\"})\\r\\n        name: attribute(expression: {key: \\\"name\\\"})\\r\\n        __typename\\r\\n      }\\r\\n      API: entity(type: \\\"API\\\") {\\r\\n        id: attribute(expression: {key: \\\"id\\\"})\\r\\n        name: attribute(expression: {key: \\\"name\\\"})\\r\\n        isAuthenticated: attribute(expression: {key: \\\"isAuthenticated\\\"})\\r\\n        hasPii: attribute(expression: {key: \\\"hasPii\\\"})\\r\\n        changeLabel: attribute(expression: {key: \\\"changeLabel\\\"})\\r\\n        changeLabelTimestamp: attribute(expression: {key: \\\"changeLabelTimestamp\\\"})\\r\\n        __typename\\r\\n      }\\r\\n      __typename\\r\\n    }\\r\\n    total\\r\\n    __typename\\r\\n  }\\r\\n}\",\"variables\":{}}"



headers = {
  'Authorization': 'c615fc6a3b63d3ec404dd6b7c6d769c8da4e69f2fe4be0f24f9b69ede3ecb866825aa3c50fdddadd1fb62d3f5d3a30db03d8a7c9862d17bd66ef183aaa5e970c',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

# with open("test.json","w")as test1:
#     json_response=response.json()
#     print(json.dump(json_response,test1))

    # data = json.dump(response,test1)
    # data = json.loads(data)
    # print(data)
# data=json.loads(response.text)
# data_serialized=json.dump(data,open('test.json',"w"),indent=2)

Allresults = json.loads(json.dumps(response.json()))
print(Allresults)

df=pandas.DataFrame(Allresults)
df.to_csv('output.csv')



# myjson=response.json()
# ourdata=[]
# csvheader=['SYMBOL','NAME','PRICEUSD']
# for x in myjson['data']['events']['results']:
#     listing=[x['id'],x['name'],x['timestamp']]
#     ourdata.append(listing)
# # print(ourdata)

# with open('output.csv','w',encoding='UTF8',newline='')as f:
#     writer=csv.writer(f)
#     writer.writerow(csvheader)
#     writer.writerow(ourdata)

# print("done")




# myjson=response.json()
# ourdata=[]
# csvheader=['ID','NAME','TIMESTAMP','TYPE','SPANID','APIID','APINAME','APIURI','CATEGORY','SERVICEID','ACTORCOUNTRY','ACTORSTATE','ACTORCITY','SERVICEID','SERVICENAME','SERVICETYPENAME','APIID','APINAME','ISAUTHENTICATED','TYPENAME']

# for x in myjson['data']['events']['results']:
#   listing=[x['id'],x['name'],x['timestamp'],x['type'],x['spanId'],x['apiId'],x['apiName'],x['apiUri'],x['category'],x['serviceId'],x['actorCountry'],x['actorState'],x['actorCity'],x['SERVICE']['id'],x['SERVICE']['name'],x['SERVICE']['__typename'],x['API']['id'],x['API']['name'],x['API']['isAuthenticated'],x['__typename']]

    
#   ourdata.append(listing)

# with open('output.csv','w',encoding='UTF8',newline='')as f:
#     writer=csv.writer(f)
#     writer.writerow(csvheader)
#     writer.writerow(ourdata)

# print("done")




