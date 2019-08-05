import json


def check_category():
    file = "final.json"
    f = open(file)
    jlist = json.load(f)
    f.close()
    category_list = ['dining', 'lifestyle', 'electronics', 'others']
    for data in jlist['offers']:
        offer_category = data['offer_Category'].lower()
        if offer_category not in category_list:
            print data['offer_Category']
            print data['store_name']
            print data['offer']
            new_cat = 'others'
            data['offer_Category'] = new_cat
    print "After category cleanup:"+str(len(jlist['offers']))
    f = open(file, "w")
    f.write(json.dumps(jlist, indent=4))
    f.close()