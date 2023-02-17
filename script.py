import requests
def status_qb(circuito):
    headers = {
        'QB-Realm-Hostname': 'ignetworks.quickbase.com',
        'User-Agent': '{User-Agent}',
        'Authorization': 'QB-USER-TOKEN b2hjmh_w4i_b2ytd7mdi8jjrpdg8khp8cmwkm6n'
    }
    #"{47.CT." + f"'{circuito}'"+"}"}
    body = {"from":"bfwgbisz4","select":[],"where":"{7.CT." + f"'{circuito}'"+"}"}
    print(body)
    r = requests.post(
    'https://api.quickbase.com/v1/records/query',
    headers = headers,
    json = body
    )
    #print(json.dumps(r.json(),indent=4))
    resultado = r.json()
    print(resultado)
    status = resultado['data'][0]['']['value']
    return status

status_qb("RNG.54266.A001")

cadena="LV3.54266.A001"

palabras = cadena.split(".")
print(palabras[0])
parseo = str(palabras[0])

if parseo == "VZB" or parseo == "TSY" or parseo == "TTA" or parseo == "TLS" or parseo == "TWS" or parseo == "VTL" or parseo == "BRT" or parseo == "EVO" or parseo == "RNG" or parseo == "GTT" or parseo == "EMB":
    print("ESTE CLIENTE ES CLAVE")
else:
    print("NO ES CLAVE")