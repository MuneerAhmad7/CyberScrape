import requests

def run(target_url=None, proxy=None):
    if not target_url:
        target_url = input("Enter target URL: ")
    if not proxy:
        proxy = input("Enter proxy (ip:port): ")

    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        print("\n🔌 Connecting via proxy:", proxy)
        r = requests.get(target_url, headers=headers, proxies=proxies, timeout=10)
        print("✅ Status Code:", r.status_code)
        print("📄 Page Title:", r.text.split("<title>")[1].split("</title>")[0])
    except requests.exceptions.ProxyError:
        print("❌ Proxy connection failed! Try another IP:Port.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Request error: {e}")
