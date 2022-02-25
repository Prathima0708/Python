import json
import os
from unittest import result
import requests
import pandas
from copy import deepcopy
import time

if os.path.isfile("tenablehost.csv"):
    os.remove("tenablehost.csv")
if os.path.isfile("tenablevulnerabilities.csv"):
    os.remove("tenablevulnerabilities.csv")

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

id = [82,129]

for scanid in id:
    print('processing scanid--',scanid)
    url = "https://cloud.tenable.com/scans/"+ str(scanid) +""

    headers = {
        "Accept": "application/json",
        "X-ApiKeys": "accessKey=b2baf02724f55530010b09f3db06423d8f50dc50a1dff8c7ae121b07c023e25b;secretKey=43826d382638537b79087d10987ee9f5aa7e57eda22da6db99e8c6b774cbc0c4"
    }

    response = requests.request("GET", url, headers=headers)

    Allresults = json.loads(json.dumps(response.json()))
    # print(Allresults)

    print(Allresults['info']['timestamp'])
    eventdate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(Allresults['info']['timestamp']))


    df = pandas.DataFrame(columns=['accountname','scanname','eventdate','scanner_name','policyname'])
    df.loc[0] = [Allresults['info']['owner'],Allresults['info']['name'],eventdate,Allresults['info']['scanner_name'],Allresults['info']['policy']]

    print(eventdate)
    # print(df)

    host = Allresults['hosts']
    # print(host)

    dfhost = json_to_dataframe(host)
    # print(dfhost)

    dfhost = dfhost.drop('severitycount.item.severitylevel',1)
    dfhost = dfhost.drop('severitycount.item.count',1)
    dfhost = dfhost.drop('asset_id',1)
    dfhost = dfhost.drop('host_id',1)
    dfhost = dfhost.drop('uuid',1)
    dfhost = dfhost.drop('progress',1)
    dfhost = dfhost.drop('scanprogresscurrent',1)
    dfhost = dfhost.drop('scanprogresstotal',1)
    dfhost = dfhost.drop('numchecksconsidered',1)
    dfhost = dfhost.drop('totalchecksconsidered',1)
    dfhost = dfhost.drop('host_index',1)
    dfhost = dfhost.drop('score',1)
    dfhost = dfhost.drop_duplicates()
    dfhost = dfhost.rename(columns = {'severity': 'totalseveritycount'}, inplace = False)

    vulnerabilities = Allresults['vulnerabilities']

    # print(vulnerabilities)

    dfvulnerabilities = json_to_dataframe(vulnerabilities)

    # print(dfvulnerabilities)

    dfvulnerabilities = dfvulnerabilities.drop('count',1)
    dfvulnerabilities = dfvulnerabilities.drop('vuln_index',1)
    dfvulnerabilities = dfvulnerabilities.drop_duplicates()

    dfhosts = pandas.merge(df.assign(A=1), dfhost.assign(A=1), on='A').drop('A', 1)
    dfvulnerability = pandas.merge(df.assign(A=1), dfvulnerabilities.assign(A=1), on='A').drop('A', 1)

    dfvulnerability['severity'] = dfvulnerability['severity'].replace({0: 'info'})
    dfvulnerability['severity'] = dfvulnerability['severity'].replace({1: 'low'})
    dfvulnerability['severity'] = dfvulnerability['severity'].replace({2: 'medium'})
    dfvulnerability['severity'] = dfvulnerability['severity'].replace({3: 'high'})
    dfvulnerability['severity'] = dfvulnerability['severity'].replace({4: 'critical'})

    if not os.path.isfile("tenablehost.csv"):
        dfhosts.to_csv("tenablehost.csv", index=False, header=True)
    else:
        dfhosts.to_csv("tenablehost.csv", index=False, mode='a', header=False)
    if not os.path.isfile("tenablevulnerabilities.csv"):
        dfvulnerability.to_csv("tenablevulnerabilities.csv", index=False, header=True)
    else:
        dfvulnerability.to_csv("tenablevulnerabilities.csv", index=False, mode='a', header=False)