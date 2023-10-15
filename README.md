# ebay_price_tracker

eBay Product Price Tracker

This Python script is a versatile eBay price tracker that can be used to monitor the prices of different products on eBay. By simply updating the LINK variable with the search URL for the desired product, users can track and analyze price trends over time. The script scrapes eBay search results, calculates the average price for the product listings without outliers, and saves this information, along with the current date, to a CSV file.

## Key Features:

1. Imports necessary libraries and modules, including BeautifulSoup, requests, numpy, csv, and datetime.
2. Defines the eBay search URL in the LINK variable, making it easy to adapt the script for tracking various products.
3. Implements a function get_prices_by_link(link) to retrieve and clean prices from eBay search results.
4. Provides a function remove_outliers(prices, m=2) to eliminate outliers using numpy.
5. Defines a function get_average(prices) to calculate and return the average price.
6. Implements a function save_to_file(prices) to save the date and average price to a CSV file.
7. The script can be executed as a standalone program.
8. It prints the current average price for the tracked product listings without outliers.
9. It appends the date and the average price to a CSV file for tracking historical prices.

This adaptable code empowers users to effortlessly track the prices of a wide range of products on eBay, helping them make well-informed purchasing decisions and monitor market trends for their desired items.

## Screenshots

![image3](https://github.com/allysonpereira/ebay_price_tracker/assets/113621581/7e4fc00f-e95d-4cf5-b0a9-4eee2a78b4c9)
