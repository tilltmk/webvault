import os
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from weasyprint import HTML

def extract_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

def download_website(website):
    response = requests.get(website.url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Create a directory for the website
    directory = f"archived_websites/{website.domain}/{website.version}"
    os.makedirs(directory, exist_ok=True)

    # Save the main HTML file
    with open(f"{directory}/index.html", 'w', encoding='utf-8') as file:
        file.write(str(soup))

    # Download and save linked files (e.g., CSS, JavaScript, images)
    for link in soup.find_all(['link', 'script', 'img']):
        if link.has_attr('href'):
            url = link['href']
        elif link.has_attr('src'):
            url = link['src']
        else:
            continue

        if url.startswith('http'):
            file_url = url
        else:
            file_url = website.url + url

        file_name = os.path.basename(file_url)
        file_path = f"{directory}/{file_name}"

        with open(file_path, 'wb') as file:
            file.write(requests.get(file_url).content)

def generate_pdf(website):
    directory = f"archived_websites/{website.domain}/{website.version}"
    html_file = f"{directory}/index.html"
    pdf_file = f"{directory}/website.pdf"

    HTML(html_file).write_pdf(pdf_file)