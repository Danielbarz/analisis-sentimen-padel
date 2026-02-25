import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def check_site(name, url):
    print(f"\n{'='*60}")
    print(f"CHECKING: {name}")
    print(f"URL: {url}")
    r = requests.get(url, headers=HEADERS, verify=False, timeout=15)
    print(f"Status: {r.status_code}")
    soup = BeautifulSoup(r.text, 'lxml')

    # Find all elements with links that look like articles
    all_links = soup.find_all('a', href=True)
    article_links = [a for a in all_links if a.get_text(strip=True) and len(a.get_text(strip=True)) > 20]

    print(f"Links with text > 20 chars: {len(article_links)}")
    for a in article_links[:5]:
        parent = a.parent
        grandparent = parent.parent if parent else None
        print(f"  Title: {a.get_text(strip=True)[:60]}")
        print(f"  Href: {a.get('href','')[:80]}")
        print(f"  Parent: <{parent.name}> class={parent.get('class',[])}")
        if grandparent:
            print(f"  Grandparent: <{grandparent.name}> class={grandparent.get('class',[])}")
        # Check for nearby date
        container = grandparent if grandparent else parent
        if container:
            date = container.find(['time', 'span', 'div'], class_=lambda c: c and ('date' in str(c).lower() or 'time' in str(c).lower()))
            if date:
                print(f"  Date: <{date.name}> class={date.get('class',[])} text={date.get_text(strip=True)[:40]}")
        print()

# Check each site
check_site("Detik", "https://www.detik.com/search/searchall?query=padel&page=1")
