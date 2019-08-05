import json


def validate():
    # Read all records from final.json
    file = "final.json"
    discarded_file = "discarded/must_have.json"
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
        # store_geo_loc can not be null or its len should not be less than 5 char
        if data['store_geo_loc'] is None or len(data['store_geo_loc']) < 5:
            discarded['offers'].append(data)
            continue
        # validity_date_iso can not be null
        if data['validity_date_iso'] is None:
            discarded['offers'].append(data)
            continue
        # bank_name can not be null
        if data['bank_name'] is None:
            discarded['offers'].append(data)
            continue
        # geo_hash can not be null
        if data['geo_hash'] is None:
            discarded['offers'].append(data)
            continue
        # offer can not be null
        if data['offer'] is None:
            discarded['offers'].append(data)
            continue
        result['offers'].append(data)
    print "Deals having all required field:" + str(len(result['offers']))
    f = open(file, "w")
    f.write(json.dumps(result, indent=4))
    f.close()

    f = open(discarded_file, "w")
    f.write(json.dumps(discarded, indent=4))
    f.close()