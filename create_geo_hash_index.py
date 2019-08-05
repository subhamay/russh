import json
import pygeohash


def geo_hash_validity(data):
    val = data['geo_hash']
    # if geo_hash contain a single char
    # then its not valid. Thus create geo hash again
    # from lat long val
    if len(set(val)) == 1:
        lat_lng = data['store_geo_loc']
        pos = lat_lng.find(',')
        lat = float(lat_lng[0:pos])
        long = float(lat_lng[pos + 1:])
        hash = pygeohash.encode(lat, long)
        if len(set(hash)) == 1:
            print data
            raw_input("geo_hash is wrong")
        data[u'geo_hash'] = hash


def get_geo_index():
    file = "final.json"
    f = open(file)
    jlist = json.load(f)
    f.close()
    result = {}
    result['offers'] = []
    # key to this map is geo_hash and value is occurrence count
    geo_map = {}
    for data in jlist['offers']:
        val = data['geo_hash']
        #if val is "zzzzzzz" then its invalid
        geo_hash_validity(data)
        if val in geo_map.keys():
            geo_map[val] = geo_map[val] + 1
        else:
            geo_map[val] = 0
        data['geo_hash_index'] = geo_map[val]
        result['offers'].append(data)

    print "Geo hash Index created deals:" + str(len(result['offers']))
    f = open(file, "w")
    f.write(json.dumps(result, indent=4))
    f.close()