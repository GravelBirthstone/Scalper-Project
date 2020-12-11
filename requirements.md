# Scalper Project Software Requirements

## Vision
The vision of this product is to analyze price history data to determine price hikes caused by scalping.  Data will be gathered via web scraping and third party datasets.  An attempt will be made to compare products and model the behavior of the prices.

The analysis provides relief to consumer pain experienced while shopping for items that have surged in price.  It will offer insight into inflatted prices, their behavior, and offer similar examples.

Understanding this analysis will better help consumers make decisions regarding when to purchase hot, in-demand items.


## Scope (In/Out)

*In*
- A web scrapper will provide current and historical secondary market price information.
- Data will be analyzed using pandas.
- Visual of price history will be displayed.
- Regression will be used to forecast price.
- Compare a different item's price.

*Out*
- The user will not be able to input a product they are interested in.  (Static analysis)
- Price forecasting will likely not be too accurate.
- Webscrapping for price will not span more four sites.
- There will be no GUI.

*MVP*
- Web scrapper to find current and historical price data
- Data visualization for price history
- Calculate price to MSRP ratio
- Use regression to chacterize price trend
- Illustrate price increase by comparing to typical household items
- Plot historical PS4 secondary market price actuals
- Compare PS5 and PS4 to see what impacts the pandemic may have on the price

*Stretch*
- Create module to pull in datasets
- Attempt to predict future prices
- Try to predict PS5 future costs
- Test prediction algorithm:  Try to predict PS4 costs using a first segment of data as train and second half as test
- Bring in toilet paper price scalping data
- Bring in hand sanitizer price scalping data
- Function to enter product and current price with output of graph showing its price if it was affected by the same scalping margins
- Test data collection:  Compare data from web scrapping to data from stockx.com's API

## Functional Requirements

*Functionality*
A data scientist can run the web scrapper Python module and Jupyter notebook to generate an analysis report to inform readers about secondary scalping market price increases and patterns.

*Data Flow*
Python web scrapper module combs an internet site for price information by requesting data from the site.  The module receives the requested data and parses it to find targeted content.  The data is structured in the appropriate convention as a CSV file for consumption by the Jupyter notebook.  The notebook intakes the csv file and stores it as a pandas dataframe.  Analysis is performed on the data and data visualizations are created.  Markdown text describes the story to the reader.

## Non-Functional Requirements
- Usability:  The team will have a person not associated with the project review the notebook ahead of the presentation to offer candid feedback on their ability to easily comprehend the notebook as written.  The reviewer may provide helpful insight as to where more explanation or an additional data visualization tool is needed.
- Testability:  Through plotting data during the development of the Jupyter notebook and as the final product, it will be apparent to the human developers if the data is corrupted or is vastly different than expected.