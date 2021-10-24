import requests
def hmm():
    r = requests.get('https://duckduckgo.com/?q=presidents+of+the+united+states&format=json')
    for i in r.json()['RelatedTopics']:
        print(i['Text'])
    return r
url_ddg = "https://api.duckduckgo.com"
def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]
counter_correct = 0
def test_presidents():
    assert "Washington" in ['Text']
    assert "Adams" in ['Text']
    assert "Jefferson" in ['Text']
    assert "Madison" in ['Text']
    assert "Monroe" in ['Text']
    assert "Adams" in ['Text']
    assert "Jackson" in ['Text']
    assert "Buren" in ['Text']
    assert "Harrison" in ['Text']
    assert "Tyler" in ['Text']
    assert "Polk" in ['Text']
    assert "Taylor" in ['Text']
    assert "Fillmore" in ['Text']
    assert "Pierce" in ['Text']
    assert "Lincoln" in ['Text']
    assert "Buchanan" in ['Text']
    assert "Lincoln" in ['Text']
    assert "Johnson" in ['Text']
    assert "Grant" in ['Text']
    assert "Hayes" in ['Text']
    assert "Garfield" in ['Text']
    assert "Arthur" in ['Text']
    assert "Cleveland" in ['Text']
    assert "McKinley" in ['Text']
    assert "Harrison" in ['Text']
    assert "Roosevelt" in ['Text']
    assert "Taft" in ['Text']
    assert "Wilson" in ['Text']
    assert "Harding" in ['Text']
    assert "Coolidge" in ['Text']
    assert "Hoover" in ['Text']
    assert "Roosevelt" in ['Text']
    assert "Truman" in ['Text']
    assert "Eisenhower" in ['Text']
    assert "Kennedy" in ['Text']
    assert "Johnson" in ['Text']
    assert "Nixon" in ['Text']
    assert "Ford" in ['Text']
    assert "Carter" in ['Text']
    assert "Reagan" in ['Text']
    assert "Bush" in ['Text']
    assert "Clinton" in ['Text']
    assert "Obama" in ['Text']
    assert "Trump" in ['Text']
    assert "Biden" in ['Text']



#r_data = str(r).splitlines()[-2]
#print(r_data_)