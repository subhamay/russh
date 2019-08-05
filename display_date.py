import json
from datetime import datetime

month = {"01": "January",
         "02": "February",
         "03": "March",
         "04": "April",
         "05": "May",
         "06": "June",
         "07": "July",
         "08": "August",
         "09": "September",
         "10": "October",
         "11": "November",
         "12": "December"
         }
dat = ["th", "st", "nd", "rd", "th", "th", "th", "th", "th", "th",
       "th", "th", "th", "th", "th", "th", "th", "th", "th", "th",
       "th", "st", "nd", "rd", "th", "th", "th", "th", "th", "th",
       "th", "st"]


def fill_display_date():
    file = "final.json"
    discarded_file = "discarded/iso_date_none.json"
    f = open(file)
    jlist = json.load(f)
    f.close()
    result = {}
    result['offers'] = []
    discarded = {}
    discarded['offers'] = []
    for data in jlist['offers']:
        iso_date = data['validity_date_iso']
        if iso_date is None:
            discarded['offers'].append(data)
        else:
            try:
                datetime.strptime(iso_date, "%Y-%m-%d")
            except ValueError:
                print data
                iso_date = raw_input("Enter iso (YYYY-MM-DD) format:")
                data['validity_date_iso'] = iso_date
            year = iso_date[0:4]
            mm = iso_date[5:7]
            dd = iso_date[8:10]
            if dd[0] == '0':
                dd = dd[1:]
            suf = dat[int(dd)]
            dis_date = dd + suf + " " + month[mm] + " " + year
            data['display_valid_until'] = dis_date
            result['offers'].append(data)
    print "Creating display date available deals count:" + str(len(result['offers']))
    f = open(file, "w")
    f.write(json.dumps(result, indent=4))
    f.close()

    f = open(discarded_file, "w")
    f.write(json.dumps(discarded, indent=4))
    f.close()
