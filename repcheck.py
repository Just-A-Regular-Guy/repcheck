import sys
import json
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Usage: python3 {sys.argv[0]} <filename>')
    else:
        s = "ip;count\n"
        for ip in [x for x in open(sys.argv[1], "r").read().split("\n") if x.strip()!=""]:
            headers = {
                'x-apikey': 'xxxxxxxxxxxxxx',
                "accept": "application/json"
            }
            response = requests.get('https://www.virustotal.com/api/v3/ip_addresses/' + ip.strip(), headers=headers)
            if response.status_code == 200:
                json_data = json.loads(response.text)
                s += f'{ip};{json_data["data"]["attributes"]["last_analysis_stats"]["malicious"]}\n'
            else:
                print("Errore: " + str(response.status_code))
        open("out_ips.csv", "w+").write(s.strip())
    