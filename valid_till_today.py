import json
from datetime import date

def validate():
    file = "final.json"
    discarded_file = "discarded/experied.json"
    f = open(file)
    jlist = json.load(f)
    f.close()
    result = {}
    result['offers'] = []
    discarded = {}
    discarded['offers'] = []
    today = date.today()
    d = today.strftime("%Y-%m-%d")
    for data in jlist['offers']:
        iso_date = data['validity_date_iso']
        if iso_date >= d:
            data['valid_offer'] = True
            result['offers'].append(data)
        else:
            discarded['offers'].append(data)
    print "Valid deals till today:" + str(len(result['offers']))
    f = open(file, "w")
    f.write(json.dumps(result, indent=4))
    f.close()

    f = open(discarded_file, "w")
    f.write(json.dumps(discarded, indent=4))
    f.close()