# Busines Details Scraper Bot Using Scrapy

[Finelib.com](https://www.finelib.com/) is an online directory and search engine for Nigerian businesses. Businesses are stored on the site within their city and niche sub-directories. 

## Example Detail
[Arrowhead Automobiles](https://www.finelib.com/listing/Arrowhead-Automobiles/34868/) is an [automotive](https://www.finelib.com/cities/lagos/automotive) business in the city of [Lagos](https://www.finelib.com/cities/lagos). 

By searching first, the city of Lagos, and then the automotive niche/category in the city of Lagos, you'd be able to see the business name. This name can then be clicked to get more info about the business. This info includes the:
+ Business name
+ Address
+ Phone numbers
+ Email address
+ Website

## Bot Details
The scrapy bot begins crawling from the [Finelib homepage](https://www.finelib.com/). Then it identifies the links to each city's directory. It follows this directory to each city's page, where it finds the links to the different business categories in the city. Following the category links, it identifies the links to the business detail page. Finally, it scours the business detail page where the business details mentioned above are collected, if available, and stored in a `.csv` file.

## Scraped Data
The scraped data is stored in the `business_details.csv` file in the home directory. 