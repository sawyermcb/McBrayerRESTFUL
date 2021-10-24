import requests
r = requests.get('https://duckduckgo.com/?q=presidents+of+the+united+states&format=json')
for i in r.json()['RelatedTopics']:
    #print( r.json()['RelatedTopics'][0]['Text'])
    print(i['Text'])

#r_data = str(r).splitlines()[-2]
#print(r_data_)