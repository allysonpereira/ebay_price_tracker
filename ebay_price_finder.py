# Import necessary libraries and modules.
from bs4 import BeautifulSoup
import requests 
import numpy as np
import csv
from datetime import datetime

# Define the eBay search URL for M1 MacBook Air listings.
LINK = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=m1+macbook+air&_sacat=0"

# Function to retrieve prices of M1 MacBook Air listings from the eBay search page.
def get_prices_by_link(link):
    # Send an HTTP GET request to the eBay search page.
    r = requests.get(link)

    # Parse the HTML content of the page using BeautifulSoup.
    page_parse = BeautifulSoup(r.text, 'html.parser')

    # Find and extract all list items containing search results.
    search_results = page_parse.find("ul", {"class": "srp-results"}).find_all("li", {"class": "s-item"})

    # Initialize an empty list to store item prices.
    item_prices = []

    # Iterate through search results to extract and clean item prices.
    for result in search_results:
        price_as_text = result.find("span", {"class": "s-item__price"}).text

        # Skip items with a price range (e.g., "to") in their price text.
        if "to" in price_as_text:
            continue

        # Extract and convert the price to a float.
        price = float(price_as_text[1:].replace(",", ""))
        item_prices.append(price)

    return item_prices

# Function to remove outliers from a list of prices using numpy.
def remove_outliers(prices, m=2):
    data = np.array(prices)
    return data[abs(data - np.mean(data)) < m * np.std(data)]

# Function to calculate and return the average price from a list of prices.
def get_average(prices):
    return np.mean(prices)

# Function to save the date and the calculated average price to a CSV file.
def save_to_file(prices):
    # Define the data fields to be written to the CSV file, including the current date.
    fields = [datetime.today().strftime("%B-%D-%Y"), np.around(get_average(prices), 2)]

    # Open the CSV file in append mode and write the data to it.
    with open('prices.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

# Entry point of the program.
if __name__ == "__main__":
    # Retrieve prices of M1 MacBook Air listings from the eBay search page.
    prices = get_prices_by_link(LINK)

    # Remove outliers from the prices using the remove_outliers function.
    prices_without_outliers = remove_outliers(prices)

    print("The average price in this moment is: ")

    # Calculate and print the average price of MacBook Air listings without outliers.
    print(get_average(prices_without_outliers))

    # Save the current date and the calculated average price to a CSV file.
    save_to_file(prices)
