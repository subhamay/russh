import json


def check():
    file = "final.json"
    discarded_file = "discarded/duplicate.json"
    # Read all records from final.json
    f = open(file)
    jlist = json.load(f)
    f.close()
    # result contain correct deals
    result = {}
    result['offers'] = []
    # discarded contain discarded deals
    discarded = {}
    discarded['offers'] = []
    for data in jlist['offers']:
        flag = 0
        for res in result['offers']:
            # A deal is duplicate if following condition matches
            if (data['geo_hash'] == res['geo_hash'] and
                    data['bank_name'] == res['bank_name'] and
                    data['store_addr'] == res['store_addr'] and
                    data['store_name'] == res['store_name'] and
                    data['offer'] == res['offer']):
                if ('offer_day' in data.keys() and
                        'offer_day' in res.keys() and
                        data['offer_day'] == res['offer_day']):
                    discarded['offers'].append(res)
                    flag = 1
                    continue
        if flag == 0:
            result['offers'].append(data)
    print "After removing duplicate" + str(len(result['offers']))
    f = open(file, "w")
    f.write(json.dumps(result, indent=4))
    f.close()

    f = open(discarded_file, "w")
    f.write(json.dumps(discarded, indent=4))
    f.close()