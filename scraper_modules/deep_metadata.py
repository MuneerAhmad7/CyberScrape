import requests
from bs4 import BeautifulSoup
import os

def run(url):
    print("\n🚀 Running: deep_metadata\n")

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        output_lines = []

        # Meta Tags Extraction
        print("🔍 Meta Tags:\n")
        output_lines.append("🔍 Meta Tags:\n")

        for tag in soup.find_all("meta"):
            name = tag.get("name") or tag.get("property") or "unknown"
            content = tag.get("content")
            if content:
                line = f"{name}: {content}"
                print(line)
                output_lines.append(line)

        # File Link Extraction
        print("\n📁 Downloadable Files:\n")
        output_lines.append("\n📁 Downloadable Files:\n")

        file_extensions = ['.pdf', '.docx', '.zip', '.xls']
        found = False

        for link in soup.find_all("a", href=True):
            href = link['href']
            if any(href.lower().endswith(ext) for ext in file_extensions):
                file_url = href if href.startswith('http') else requests.compat.urljoin(url, href)
                print(file_url)
                output_lines.append(file_url)
                found = True

        if not found:
            print("No downloadable files found.")
            output_lines.append("No downloadable files found.")

        # Save to file
        output_file = os.path.join(os.getcwd(), "output_deep_metadata.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(output_lines))

        print(f"\n✅ Results saved to: {output_file}")

    except Exception as e:
        print(f"❌ Error occurred: {e}")
