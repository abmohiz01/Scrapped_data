import os
import openpyxl

import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
# Function
current_directory = os.getcwd()

url = "https://priceoye.pk/power-banks"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
print(soup.find_all('title'))


# divs = soup.find_all(class_="productBox b-productBox")

divs = soup.find_all(class_="productBox b-productBox")
for div in divs:
    title = div.find(class_="p-title bold h5").text.strip()
    price = div.find(class_="price-box p1").text.strip()

    data.append([title, price])

    # Create a pandas DataFrame with the extracted data
df = pd.DataFrame(data, columns=["Title", "Price"])

# Save data to Excel
df.to_excel("output.xlsx", index=False)

# Save data to CSV
# df.to_csv("output.csv", index=False)

