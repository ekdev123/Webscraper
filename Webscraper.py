import requests
from bs4 import BeautifulSoup


URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")
results = soup.find(id="ResultsContainer")
print(results.prettify())

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

job_elements = results.find_all("div", class_="card-content")
for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
    title_element = job_element.find("h2",class_="title")
    company_element = job_element.find("h3",class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

# Step through a web scraping pipeline from start to finish
# Inspect the HTML structure of your target site with your browser’s developer tools
# Decipher the data encoded in URLs
# Download the page’s HTML content using Python’s requests library
# Parse the downloaded HTML with Beautiful Soup to extract relevant information
# Build a script that fetches job offers from the Web and displays relevant information in your console





