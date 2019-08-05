import json
from validator_collection import checkers
import urllib2
import time


def validate():
    # Read all records from final.json validates the links
    # present in tnc and url_bank_offer_page.
    # If requesting that url does not return 404 then that link is valid
    file = "final.json"
    f = open(file)
    jlist = json.load(f)
    f.close()
    for data in jlist['offers']:
        offer_url = data['url_bank_offer_page']
        tnc_url = data['tnc']
        if checkers.is_url(offer_url):
            stat1 = is_valid_url(offer_url)
            if not stat1:
                data['url_bank_offer_page'] = None
        else:
            data['url_bank_offer_page'] = None
        if checkers.is_url(tnc_url):
            stat2 = is_valid_url(tnc_url)
            if not stat2:
                data['tnc'] = None
    f = open(file, "w")
    f.write(json.dumps(jlist, indent=4))
    f.close()


def is_valid_url(url):
    try:
        req = urllib2.Request(url)
        uClient = urllib2.urlopen(req)
        page_html = uClient.read()
        return True
    except Exception as e:
        if "404" in str(e):
            return False
        elif "403" in str(e):
            # 403 means that server is not allowing our request. Thus sleep
            time.sleep(10)
            return True



