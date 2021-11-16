# Visual Finance Tool

## A GUI for accessing and assessing portfolios and watchlists of stocks with tools for financial data and stock research

#### **Technologies**
- Python
  - requests
  - flask
  - GUI
- JavaScript
  - Node.js
    - express
    - cheerio
    - axios
- SQLite
  - scratch-built query builder
  - scratch built input sanitizer
  - CRUD

#### Watchlists and Portfolios
While both of these databases hold information about stocks, they differ in the scope of information.

A portfolio can be used for stocks you want to track quantity, price basis, and return for.
You can have as many portfolios as you want.
The idea is that you could use this to track hypothetical portfolios alongside your own, or if you have multiple brokerage accounts you could set up a portfolio for each.

A watchlist only keeps track of the ticker and the last price.
You can make as many watchlists as you want.
The idea is that you can treat these lists as reminders to check in on stocks you might be interested in. You could also use it to track a basket of stocks that you use as indicators.
