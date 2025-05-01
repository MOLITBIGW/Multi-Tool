import requests

def e(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        if data['status'] == 'fail':
            print(f"[!] Error: {data['message']}")
            return

        print(f"\nIP Address: {data['query']}")
        print(f"[+] Country: {data['country']} ({data['countryCode']})")
        print(f"[+] Region: {data['regionName']}")
        print(f"[+] City: {data['city']}")
        print(f"[+] ZIP: {data['zip']}")
        print(f"[+] Latitude: {data['lat']}")
        print(f"[+] Longitude: {data['lon']}")
        print(f"[+] ISP: {data['isp']}")
        print(f"[+] Org: {data['org']}")
        print(f"[+] Timezone: {data['timezone']}")
    except Exception as e:
        print(f"[!] Failed to fetch IP data: {e}")

if __name__ == "__main__":
    ip = input("Enter IP address to lookup: ").strip()
    e(ip)
