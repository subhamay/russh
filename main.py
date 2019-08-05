import json
import os
import must_have
import category
import display_date
import valid_till_today
import duplicate
import create_geo_hash_index
import url_validity


def merge_all_deals():
    # Merger all deals present in ./deals and create final.json
    directory = "./deals"
    result = {}
    result['offers'] = []
    for filename in os.listdir(directory):
        file = directory + '/' + filename
        f = open(file)
        jlist = json.load(f)
        f.close()
        for data in jlist['offers']:
            result['offers'].append(data)
    print 'total deal:' + str(len(result['offers']))
    out_file = 'final.json'
    f = open(out_file, "w")
    f.write(json.dumps(result, indent=4))
    f.close()

'''
All the deals are in ./deals. First we merge them all and run validation
on those merged deals
'''
if __name__ == "__main__":
    merge = raw_input("Do you Want to merge all deals?(y/n)")
    if merge == "y":
        merge_all_deals()
    # Some fileds should not be null. This check is done here
    must_have_field = raw_input("Check must have fields are not null?(y/n)")
    if must_have_field == "y":
        must_have.validate()
    # Category validation
    cat = raw_input("Do you Want to cleanup category?(y/n)")
    if cat == "y":
        category.check_category()
    # Date formating for display_valid_until is done here
    date_formatting = raw_input("Do you Want to create display_date for deals?(y/n)")
    if date_formatting == "y":
        display_date.fill_display_date()
    # validity_date_iso should be greater than todays date
    valid_till = raw_input("Do you check valid_iso field?(y/n)")
    if valid_till == "y":
        valid_till_today.validate()
    # Duplicate deal deletion is done here
    dup = raw_input("Do you want to check for duplicate deals?(y/n)")
    if dup == "y":
        duplicate.check()
    # geo_hash_index field is populated here
    index = raw_input("want to create geo_hash_index?(y/n)")
    if index == "y":
        create_geo_hash_index.get_geo_index()
    # checking for links present in json are checked here
    url_check = raw_input("Want to check if links are valid?(y/n)")
    if url_check == "y":
        url_validity.validate()





