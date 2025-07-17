import subprocess
import socket
import os
import datetime

def run(target_url):
    print("\n🌐 Starting Subdomain Enumeration & Recon...\n")

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"subdomain_recon_{timestamp}.txt"

    # Step 1: Create a temp directory
    os.makedirs("temp_enum", exist_ok=True)

    print("🔎 Running subfinder...")
    subfinder_cmd = ["subfinder", "-d", target_url, ]
    subfinder_out = subprocess.run(subfinder_cmd, capture_output=True, text=True).stdout

    print("🔎 Running findomain...")
    findomain_cmd = ["findomain", "-t", target_url, ]
    findomain_out = subprocess.run(findomain_cmd, capture_output=True, text=True).stdout

    print("🔎 Running sublist3r...")
    sublist3r_cmd = ["sublist3r", "-d", target_url, "-o", "temp_enum/sublister.txt"]
    subprocess.run(sublist3r_cmd)

    with open("temp_enum/sublister.txt", "r") as f:
        sublist3r_out = f.read()

    all_subdomains = set(
        subfinder_out.splitlines() +
        findomain_out.splitlines() +
        sublist3r_out.splitlines()
    )

    print(f"✅ Total Subdomains Found: {len(all_subdomains)}")

    # Save all subdomains
    with open("temp_enum/all_subdomains.txt", "w") as f:
        f.write("\n".join(all_subdomains))

    # Step 2: Probe live domains
    print("\n⚡ Probing live domains with httpx...")
    httpx_cmd = ["httpx", "-l", "temp_enum/all_subdomains.txt", "-o", "temp_enum/live.txt"]
    subprocess.run(httpx_cmd)

    with open("temp_enum/live.txt", "r") as f:
        live_domains = f.read().splitlines()

    print(f"✅ Live Domains Found: {len(live_domains)}")

    # Step 3: Resolve IPs
    print("\n📡 Resolving IP addresses...")
    ip_map = {}
    for domain in live_domains:
        try:
            ip = socket.gethostbyname(domain)
            ip_map[domain] = ip
        except socket.gaierror:
            ip_map[domain] = "Resolution Failed"

    # Step 4: Basic Nmap Scan
    print("\n🔍 Running basic Nmap scan on live IPs...")
    nmap_results = {}
    for domain, ip in ip_map.items():
        if ip == "Resolution Failed":
            continue
        try:
            print(f"Scanning {domain} ({ip})...")
            nmap_cmd = ["nmap", "-T4", "-F", ip]
            result = subprocess.run(nmap_cmd, capture_output=True, text=True).stdout
            nmap_results[domain] = result
        except Exception as e:
            nmap_results[domain] = f"Error: {e}"

    # Step 5: Save to file
    with open(output_file, "w") as f:
        f.write(f"Subdomain Recon Results for: {target_url}\n")
        f.write("="*60 + "\n\n")

        f.write("🔍 Subdomains:\n")
        for s in all_subdomains:
            f.write(f"- {s}\n")

        f.write("\n✅ Live Domains:\n")
        for l in live_domains:
            f.write(f"- {l}\n")

        f.write("\n📡 IP Addresses:\n")
        for d, ip in ip_map.items():
            f.write(f"- {d}: {ip}\n")

        f.write("\n🛡️ Nmap Results:\n")
        for d, res in nmap_results.items():
            f.write(f"\n--- {d} ---\n")
            f.write(res + "\n")

    print(f"\n✅ Recon complete. Results saved to {output_file}\n")

    # Cleanup
    subprocess.run(["rm", "-rf", "temp_enum"])
