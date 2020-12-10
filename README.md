# Scalper Project

## Authors

Lee Thomas, Taylor Johnson, Alex Pena, Paul Leonard

## Overview

The global pandemic is severely limiting the supply chain, and this has caused a massive rise to scalpers. Scalpers are people who buy a product with no intention of using it, only to turn around and sell the product online for double, triple, or quadruple its msrp. A scalpers goal is to take advantage of the products hype and limit of the supply chain for a quick profit. We will be using a web scraper to find the inflated prices of scalped products and graph them against the msrp. We will find historical data of similar scalped products and graph them as well. Then, we can compare the pre-covid scalping to todays scapling, amisdst a disrupted supply chain, and observe any differences.

## Wireframe

![Scalper Wireframe](assets/scalper-wireframe.png)

## Version 1.0.0

Basic scaffolding and dependencies.

## User Stories

**Price Check:**
As a consumer I want to see the current cost of an out-of-stock new product compared to its MSRP so I can choose to buy or not as an informed consumer.
Feature Tasks:

- Research product MSRP
- Scrape web for current average listing price
- Create CSV of price data
- Graph current prices vs MSRP in Notebook
Acceptance Tests:
- Able to find MSRP
- Able to scrape secondary market sites for prices
- Able to produce CSV a file with appropriate scraped data
- Able to generate graph in Jupyter Notebook

**Price History:**
As a consumer I want to know the historical trend in price scalping so I can understand what is happening today.
Feature Tasks:

- Research historical cases of product scalping
- Import historical data as CSV
- Present historical price trend vs current prices
Acceptance Tests:
- Able to find historical scalping data
- Able to import CSV
- Able to create visual comparison of historical vs current

**Price Change:**
As a consumer I want a graph so that I can see the price change over time of a product.
Feature Tasks:

- Create specific data sets from CSV
- Create graph to plot price change over time
Acceptance Tests:
- Able to extract price and time data from CSV
- Able to produce graph of price over time

**Inflated Price Perspective:**
As a user I want an app that will show me what scalping of common household items would look like so I can put the scalped prices into perspective.
Feature Tasks:

- Create a data visualization that shows a common consumer product and produces a scalped price based on current scalping trends.
- Create app that takes in a product and a price and produces a scalped price based on current scalping trends. (stretch goal)
Acceptance Tests:
- Able to display a sample of a different consumer item.
- Able to take user input (stretch goal)
- Able to make calculation on user input (stretch goal)
- Able to output scalped price to user. (stretch goal)

**Time to Settle:**
As a user I want to know how long I have to wait for an inflated price to return to MSRP so that I can save money.
Feature Tasks:

- Research time price data of products that have come down from a scalpers high.
- Graph trend in price descents back to MSRP
- Make conclusion based on data
- Present user average time of price to return to MSRP
- Make prediction of when product will return to MSRP (linear regression)
Acceptance Tests:
- Able to find data of price hike and fall
- Able to produce graph of product cycles
- Able to present conclusion in Notebook
- Able to present prediction of current products price cycle




## Data Sources
- [PS4 prices from camelcamelcamel](https://camelcamelcamel.com/PlayStation-4-Console/product/B00BGA9WK2?__cf_chl_jschl_tk__=8155a104c8d4bb2508a0acb50547d98736bd3348-1607377073-0-AbWXxCNwDvK7SQalO9hGORBG3Jd8kE_pyoX04gPfCaeBS7bAo8yjmFsL6mflW4tzVR2gfMWn2XpgFIIg1Kr-7myrKc9Gq3R68FwKZ4HpfkXwr8xIXZEEXtDMW5q_dSl5QOZdLwV_G_ttjSaeqg0b-RjCgNcqjktAPlU-03Z4-1a48-YyfG_YlCljh_F5sWcCbT0kn9hW4ZiXIFhD_1XuMkfTo3m8MUrB32sgs0EOqI2zzbt2FRaxGsBzonCRC5q8m9F6T4hqDmFdQKWyskrST8EyJSg1gcVzlIRCYxqaxg964g8IIhe9HpS3jHRwU2WXZu2r4aTI_g9SQk88dnDu8rruGujWYZB5BJKXNJI65QuL975LWxbdhYlP7usxFW8aM028XjHb6-mioxaW5AY_piYhAvxrGCcIDt7QffG74Wd5)
- [PS5 on StockX.com](https://stockx.com/sony-ps5-playstation-5-digital-edition-console-white)


## Credits and Resources
- [seaborn multiple line plots](https://towardsdatascience.com/a-step-by-step-guide-for-creating-advanced-python-data-visualizations-with-seaborn-matplotlib-1579d6a1a7d0)
- [axis labels](https://www.kite.com/python/answers/how-to-label-axes-in-a-seaborn-bar-plot-in-python)
- [add title](https://stackoverflow.com/questions/42406233/how-to-add-title-to-seaborn-boxplot)
- [enumerate for loop](https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/)
- [rounding](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.round.html)
- [second y axis](https://cmdlinetips.com/2019/10/how-to-make-a-plot-with-two-different-y-axis-in-python-with-matplotlib/)
- [ps4 historical sales](https://www.sie.com/en/corporate/data.html)
- [revert git commit](https://opensource.com/article/18/6/git-reset-revert-rebase-commands)
- [seaborn regression tutorial](https://seaborn.pydata.org/tutorial/regression.html)
- [change color of regression line in seaborn](https://stackoverflow.com/questions/35827268/how-to-change-the-line-color-in-seaborn-lmplot)
- [dataframe to list](https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column)
- [sklearn: plot svm regression](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html)
- [vertical x labels in matplotlib](https://matplotlib.org/3.1.1/gallery/ticks_and_spines/ticklabels_rotation.html)
- [rotated labels in seaborn](https://stackoverflow.com/questions/26540035/rotate-label-text-in-seaborn-factorplot)
- [string into datetime](https://stackoverflow.com/questions/466345/converting-string-into-datetime)
- [datetime.fromisoformat and datetime.strptime](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime)
- [ravel](https://www.javatpoint.com/numpy-ravel#:~:text=numpy.-,ravel()%20in%20Python,source%20array%20or%20input%20array.)
- [svm.svc inputs](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC.fit)
- [scikit-learn: support vector regression using linear and non-linear kernels](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html)

