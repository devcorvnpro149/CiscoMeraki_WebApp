import json
import pgpd


def GET_OG():
    resp = pgpd.get(api = "/organizations")
    print (resp)
    print (type(resp))
    resp = resp.json()
    print (resp)
    print (type(resp))
    og_list = json.dumps(resp, indent=4)
    print(og_list)
    print (type(og_list))
    return og_list

result = GET_OG()
result = json.loads(result)
print (result)
print (type(result))
