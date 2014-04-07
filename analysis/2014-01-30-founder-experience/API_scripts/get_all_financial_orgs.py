def get_all_financial_orgs():
    url = "http://api.crunchbase.com/v/1/financial-organizations.js?api_key=duv4frwccxgyjwh5d8w5zm32"
    req = urllib2.Request(url)
    j = urllib2.urlopen(req)
    js = json.load(j)
    
    financial_orgs = []
    
    for f in js:
        financial_orgs.append(f['permalink'])
    
    return financial_orgs