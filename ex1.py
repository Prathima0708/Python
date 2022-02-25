# import json
# import os
# from unittest import result
# import requests
# import pandas
# from copy import deepcopy
# import time

# if os.path.isfile("output.csv"):
#     os.remove("output.csv")

# def cross_join(left, right):
#     new_rows = [] if right else left
#     for left_row in left:
#         for right_row in right:
#             temp_row = deepcopy(left_row)
#             for key, value in right_row.items():
#                 temp_row[key] = value
#             new_rows.append(deepcopy(temp_row))
#     return new_rows

# def flatten_list(data):
#     for elem in data:
#         if isinstance(elem, list):
#             yield from flatten_list(elem)
#         else:
#             yield elem

# def json_to_dataframe(data_in):
#     def flatten_json(data, prev_heading=''):
#         if isinstance(data, dict):
#             rows = [{}]
#             for key, value in data.items():
#                 rows = cross_join(rows, flatten_json(value, prev_heading + '.' + key))
#         elif isinstance(data, list):
#             rows = []
#             for i in range(len(data)):
#                 [rows.append(elem) for elem in flatten_list(flatten_json(data[i], prev_heading))]
#         else:
#             rows = [{prev_heading[1:]: data}]
#         return rows

#     return pandas.DataFrame(flatten_json(data_in))




# url = "https://api.traceable.ai/graphql"

# payload="{\"query\":\"{\\r\\n  events(\\r\\n    limit: 1\\r\\n    between: {startTime: \\\"2022-01-03T07:13:42.277Z\\\", endTime: \\\"2022-02-03T07:13:42.277Z\\\"}\\r\\n    filterBy: [{keyExpression: {key: \\\"id\\\"}, operator: EQUALS, value: \\\"6347097f-3115-46fc-94b7-3ebb8d4eab47\\\", type: ATTRIBUTE}, {keyExpression: {key: \\\"securityEventCategory\\\"}, operator: NOT_EQUALS, value: \\\"INTERNAL\\\", type: ATTRIBUTE}, {keyExpression: {key: \\\"securityEventCategory\\\"}, operator: NOT_EQUALS, value: \\\"TAGGED\\\", type: ATTRIBUTE}]\\r\\n  ) {\\r\\n    results {\\r\\n      id\\r\\n      name: attribute(expression: {key: \\\"name\\\"})\\r\\n      timestamp: attribute(expression: {key: \\\"timestamp\\\"})\\r\\n      type: attribute(expression: {key: \\\"type\\\"})\\r\\n      spanId: attribute(expression: {key: \\\"spanId\\\"})\\r\\n      apiId: attribute(expression: {key: \\\"apiId\\\"})\\r\\n      apiName: attribute(expression: {key: \\\"apiName\\\"})\\r\\n      apiUri: attribute(expression: {key: \\\"apiUri\\\"})\\r\\n      category: attribute(expression: {key: \\\"category\\\"})\\r\\n      serviceId: attribute(expression: {key: \\\"serviceId\\\"})\\r\\n      serviceName: attribute(expression: {key: \\\"serviceName\\\"})\\r\\n      eventDescription: attribute(expression: {key: \\\"eventDescription\\\"})\\r\\n      actorEntityId: attribute(expression: {key: \\\"actorEntityId\\\"})\\r\\n      actorName: attribute(expression: {key: \\\"actorName\\\"})\\r\\n      actorIpAddress: attribute(expression: {key: \\\"actorIpAddress\\\"})\\r\\n      actorDevice: attribute(expression: {key: \\\"actorDevice\\\"})\\r\\n      actorSession: attribute(expression: {key: \\\"actorSession\\\"})\\r\\n      securityScoreCategory: attribute(expression: {key: \\\"securityScoreCategory\\\"})\\r\\n      securityEventCategory: attribute(expression: {key: \\\"securityEventCategory\\\"})\\r\\n      securityEventTypeId: attribute(expression: {key: \\\"securityEventTypeId\\\"})\\r\\n      spanStartTimestamp: attribute(expression: {key: \\\"spanStartTimestamp\\\"})\\r\\n      actorCountry: attribute(expression: {key: \\\"actorCountry\\\"})\\r\\n      actorState: attribute(expression: {key: \\\"actorState\\\"})\\r\\n      actorCity: attribute(expression: {key: \\\"actorCity\\\"})\\r\\n      SERVICE: entity(type: \\\"SERVICE\\\") {\\r\\n        id: attribute(expression: {key: \\\"id\\\"})\\r\\n        name: attribute(expression: {key: \\\"name\\\"})\\r\\n        __typename\\r\\n      }\\r\\n      API: entity(type: \\\"API\\\") {\\r\\n        id: attribute(expression: {key: \\\"id\\\"})\\r\\n        name: attribute(expression: {key: \\\"name\\\"})\\r\\n        isAuthenticated: attribute(expression: {key: \\\"isAuthenticated\\\"})\\r\\n        hasPii: attribute(expression: {key: \\\"hasPii\\\"})\\r\\n        changeLabel: attribute(expression: {key: \\\"changeLabel\\\"})\\r\\n        changeLabelTimestamp: attribute(expression: {key: \\\"changeLabelTimestamp\\\"})\\r\\n        __typename\\r\\n      }\\r\\n      __typename\\r\\n    }\\r\\n    total\\r\\n    __typename\\r\\n  }\\r\\n}\",\"variables\":{}}"

# headers = {
#   'Authorization': 'c615fc6a3b63d3ec404dd6b7c6d769c8da4e69f2fe4be0f24f9b69ede3ecb866825aa3c50fdddadd1fb62d3f5d3a30db03d8a7c9862d17bd66ef183aaa5e970c',
#   'Content-Type': 'application/json'
# }

# response = requests.request("POST", url, headers=headers,data=payload)
# # print(response.text)

# Allresults = json.loads(json.dumps(response.json()))
    


# df = pandas.DataFrame(columns=['id','name','type','spanId'])
# df.loc[0] = [Allresults['data']['events']['results'][0]['id'],Allresults['data']['events']['results'][0]['name'],Allresults['data']['events']['results'][0]['type'],Allresults['data']['events']['results'][0]['spanId']]


 

# host = Allresults['data']['events']['results']

# dfhost = json_to_dataframe(host)



# dfhosts = pandas.merge(df.assign(A=1), dfhost.assign(A=1), on='A').drop('A', 1)

# if not os.path.isfile("output.csv"):
#     dfhosts.to_csv("output.csv", index=False, header=True)



import json
import os
from unittest import result
import requests
import pandas
from copy import deepcopy
import time

if os.path.isfile("output.csv"):
    os.remove("output.csv")
# if os.path.isfile("D:\Cetas\Scripts\TenableIntegration\\tenablevulnerabilities.csv"):
#     os.remove("D:\Cetas\Scripts\TenableIntegration\\tenablevulnerabilities.csv")

def cross_join(left, right):
    new_rows = [] if right else left
    for left_row in left:
        for right_row in right:
            temp_row = deepcopy(left_row)
            for key, value in right_row.items():
                temp_row[key] = value
            new_rows.append(deepcopy(temp_row))
    return new_rows

def flatten_list(data):
    for elem in data:
        if isinstance(elem, list):
            yield from flatten_list(elem)
        else:
            yield elem

def json_to_dataframe(data_in):
    def flatten_json(data, prev_heading=''):
        if isinstance(data, dict):
            rows = [{}]
            for key, value in data.items():
                rows = cross_join(rows, flatten_json(value, prev_heading + '.' + key))
        elif isinstance(data, list):
            rows = []
            for i in range(len(data)):
                [rows.append(elem) for elem in flatten_list(flatten_json(data[i], prev_heading))]
        else:
            rows = [{prev_heading[1:]: data}]
        return rows

    return pandas.DataFrame(flatten_json(data_in))

# id = [82,129]

# for scanid in id:
print('processing scanid--')
url = "https://api.traceable.ai/graphql"

payload="{\"query\":\"{\\r\\n  events(\\r\\n    limit: 1\\r\\n    between: {startTime: \\\"2022-01-03T07:13:42.277Z\\\", endTime: \\\"2022-02-03T07:13:42.277Z\\\"}\\r\\n    filterBy: [{keyExpression: {key: \\\"id\\\"}, operator: EQUALS, value: \\\"6347097f-3115-46fc-94b7-3ebb8d4eab47\\\", type: ATTRIBUTE}, {keyExpression: {key: \\\"securityEventCategory\\\"}, operator: NOT_EQUALS, value: \\\"INTERNAL\\\", type: ATTRIBUTE}, {keyExpression: {key: \\\"securityEventCategory\\\"}, operator: NOT_EQUALS, value: \\\"TAGGED\\\", type: ATTRIBUTE}]\\r\\n  ) {\\r\\n    results {\\r\\n      id\\r\\n      name: attribute(expression: {key: \\\"name\\\"})\\r\\n      timestamp: attribute(expression: {key: \\\"timestamp\\\"})\\r\\n      type: attribute(expression: {key: \\\"type\\\"})\\r\\n      spanId: attribute(expression: {key: \\\"spanId\\\"})\\r\\n      apiId: attribute(expression: {key: \\\"apiId\\\"})\\r\\n      apiName: attribute(expression: {key: \\\"apiName\\\"})\\r\\n      apiUri: attribute(expression: {key: \\\"apiUri\\\"})\\r\\n      category: attribute(expression: {key: \\\"category\\\"})\\r\\n      serviceId: attribute(expression: {key: \\\"serviceId\\\"})\\r\\n      serviceName: attribute(expression: {key: \\\"serviceName\\\"})\\r\\n      eventDescription: attribute(expression: {key: \\\"eventDescription\\\"})\\r\\n      actorEntityId: attribute(expression: {key: \\\"actorEntityId\\\"})\\r\\n      actorName: attribute(expression: {key: \\\"actorName\\\"})\\r\\n      actorIpAddress: attribute(expression: {key: \\\"actorIpAddress\\\"})\\r\\n      actorDevice: attribute(expression: {key: \\\"actorDevice\\\"})\\r\\n      actorSession: attribute(expression: {key: \\\"actorSession\\\"})\\r\\n      securityScoreCategory: attribute(expression: {key: \\\"securityScoreCategory\\\"})\\r\\n      securityEventCategory: attribute(expression: {key: \\\"securityEventCategory\\\"})\\r\\n      securityEventTypeId: attribute(expression: {key: \\\"securityEventTypeId\\\"})\\r\\n      spanStartTimestamp: attribute(expression: {key: \\\"spanStartTimestamp\\\"})\\r\\n      actorCountry: attribute(expression: {key: \\\"actorCountry\\\"})\\r\\n      actorState: attribute(expression: {key: \\\"actorState\\\"})\\r\\n      actorCity: attribute(expression: {key: \\\"actorCity\\\"})\\r\\n      SERVICE: entity(type: \\\"SERVICE\\\") {\\r\\n        id: attribute(expression: {key: \\\"id\\\"})\\r\\n        name: attribute(expression: {key: \\\"name\\\"})\\r\\n        __typename\\r\\n      }\\r\\n      API: entity(type: \\\"API\\\") {\\r\\n        id: attribute(expression: {key: \\\"id\\\"})\\r\\n        name: attribute(expression: {key: \\\"name\\\"})\\r\\n        isAuthenticated: attribute(expression: {key: \\\"isAuthenticated\\\"})\\r\\n        hasPii: attribute(expression: {key: \\\"hasPii\\\"})\\r\\n        changeLabel: attribute(expression: {key: \\\"changeLabel\\\"})\\r\\n        changeLabelTimestamp: attribute(expression: {key: \\\"changeLabelTimestamp\\\"})\\r\\n        __typename\\r\\n      }\\r\\n      __typename\\r\\n    }\\r\\n    total\\r\\n    __typename\\r\\n  }\\r\\n}\",\"variables\":{}}"



headers = {
  'Authorization': 'c615fc6a3b63d3ec404dd6b7c6d769c8da4e69f2fe4be0f24f9b69ede3ecb866825aa3c50fdddadd1fb62d3f5d3a30db03d8a7c9862d17bd66ef183aaa5e970c',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers,data=payload)
print(response.text)

Allresults = json.loads(json.dumps(response.json()))

# print(Allresults['results']['timestamp'])
# eventdate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(Allresults['results']['timestamp']))


df = pandas.DataFrame(columns=['ID','Name','Type','Spanid'])
df.loc[0] = [Allresults['data']['events']['results'][0]['id'],Allresults['data']['events']['results'][0]['name'],Allresults['data']['events']['results'][0]['type'],Allresults['data']['events']['results'][0]['spanId']]

# print(eventdate)

host = Allresults['data']['events']['results'][0] 

dfhost = json_to_dataframe(host)

# dfhost = dfhost.drop('severitycount.item.severitylevel',1)
# dfhost = dfhost.drop('severitycount.item.count',1)
# dfhost = dfhost.drop('asset_id',1)
# dfhost = dfhost.drop('host_id',1)
# dfhost = dfhost.drop('uuid',1)
# dfhost = dfhost.drop('progress',1)
# dfhost = dfhost.drop('scanprogresscurrent',1)
# dfhost = dfhost.drop('scanprogresstotal',1)
# dfhost = dfhost.drop('numchecksconsidered',1)
# dfhost = dfhost.drop('totalchecksconsidered',1)
# dfhost = dfhost.drop('host_index',1)
# dfhost = dfhost.drop('score',1)
# dfhost = dfhost.drop_duplicates()
# dfhost = dfhost.rename(columns = {'severity': 'totalseveritycount'}, inplace = False)

# vulnerabilities = Allresults['vulnerabilities']

# dfvulnerabilities = json_to_dataframe(vulnerabilities)

# dfvulnerabilities = dfvulnerabilities.drop('count',1)
# dfvulnerabilities = dfvulnerabilities.drop('vuln_index',1)
# dfvulnerabilities = dfvulnerabilities.drop_duplicates()

# dfhosts = pandas.merge(df.assign(A=1), dfhost.assign(A=1), on='A').drop('A', 1)
# dfvulnerability = pandas.merge(df.assign(A=1), dfvulnerabilities.assign(A=1), on='A').drop('A', 1)

# dfvulnerability['severity'] = dfvulnerability['severity'].replace({0: 'info'})
# dfvulnerability['severity'] = dfvulnerability['severity'].replace({1: 'low'})
# dfvulnerability['severity'] = dfvulnerability['severity'].replace({2: 'medium'})
# dfvulnerability['severity'] = dfvulnerability['severity'].replace({3: 'high'})
# dfvulnerability['severity'] = dfvulnerability['severity'].replace({4: 'critical'})

if not os.path.isfile("output.csv"):
    dfhost.to_csv("output.csv", index=False, header=True)
# else:
#     dfhosts.to_csv("D:\Cetas\Scripts\TenableIntegration\\tenablehost.csv", index=False, mode='a', header=False)
# if not os.path.isfile("D:\Cetas\Scripts\TenableIntegration\\tenablevulnerabilities.csv"):
#     dfvulnerability.to_csv("D:\Cetas\Scripts\TenableIntegration\\tenablevulnerabilities.csv", index=False, header=True)
# else:
#     dfvulnerability.to_csv("D:\Cetas\Scripts\TenableIntegration\\tenablevulnerabilities.csv", index=False, mode='a', header=False)
