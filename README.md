#  eBay MacBook Air Price Tracker

This Python script enables users to track and analyze the average prices of M1 MacBook Air listings on eBay. It achieves this by scraping eBay search results, extracting price information, removing outliers, and saving the average price along with the current date to a CSV file.

# Getting Started

## Prerequisites
Before running the script, make sure you have the required libraries installed. You can install them using the following command:

'''bash
pip install beautifulsoup4 requests numpy

## Usage
1. Open the script in a Python environment (e.g., Jupyter Notebook, VSCode).
2. Run the script, and it will fetch the eBay search results for M1 MacBook Air listings, process the prices, and display the current average price without outliers.
3. The script also saves the date and the calculated average price to a CSV file named prices.csv for future reference.

## Code Structure

The script is organized into the following sections:

1. Import Libraries: Import necessary Python libraries, including BeautifulSoup, requests, numpy, csv, and datetime.

2. eBay Search URL: Define the eBay search URL for M1 MacBook Air listings.

3. Functions:

  - get_prices_by_link(link): Retrieves prices of M1 MacBook Air listings from the eBay search page.
  - remove_outliers(prices, m=2): Removes outliers from a list of prices using numpy.
  - get_average(prices): Calculates and returns the average price from a list of prices.
  - save_to_file(prices): Saves the date and the calculated average price to a CSV file.
  
4. Main Script:

  - Retrieves prices of M1 MacBook Air listings using the eBay search URL.
  - Removes outliers from the prices.
  - Prints the current average price without outliers.
  - Saves the current date and the calculated average price to a CSV file.

## Contributing
Feel free to contribute to the development of this script by opening issues or submitting pull requests.

## License
This script is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
  - Beautiful Soup - For HTML parsing.
  - NumPy - For numerical operations.
  - eBay - For providing the platform to retrieve MacBook Air prices.

## Screenshots

![image3](https://github.com/allysonpereira/ebay_price_tracker/assets/113621581/7e4fc00f-e95d-4cf5-b0a9-4eee2a78b4c9)
