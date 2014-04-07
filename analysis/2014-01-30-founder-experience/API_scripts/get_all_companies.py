def get_all_companies():
    url = "http://api.crunchbase.com/v/1/companies.js?api_key=duv4frwccxgyjwh5d8w5zm32"
    req = urllib2.Request(url)
    j = urllib2.urlopen(req)
    js = json.load(j)
    
    companies = []
    
    for c in js:
        companies.append(c['permalink'])
    
    return companies