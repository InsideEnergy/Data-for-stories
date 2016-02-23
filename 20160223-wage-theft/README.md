# Analysis of Wage Theft Lawsuits in Colorado and Texas
Data and notes on Fair Labor Standards Act lawsuits from Colorado and Texas filed in federal courts, with oil and gas companies flagged.

## What's in this repository?

This repository includes the data used in the story, ["Wage Theft Claims Surge As Oil Prices Fall"](http://insideenergy.org/2016/02/22/wage-theft-claims-surge-as-oil-prices-fall/).

## Data dictionary

The data files *tx-flsa-20102015-classified.csv*, *tx-flsa-20102015-classified.xlsx*, *co-flsa-20102015-classified.csv* and *co-flsa-20102015-classified.xlsx* include Fair Labor Standards Act lawsuits - from Texas and Colorado, respectively - and filed in federal courts, classified as oil and gas, not oil and gas, or ambiguous:
* *cs_title* is the case title
* *court_id* is the court the case was filed in (first two digits indicate state, second two digits indicate the court abbreviation, last two digits are always "ce"); see a full [list of courts](http://www.pacer.gov/cgi-bin/links.pl)
* *cs_year* is the year in which the case was filed
* *case_no* is the case number (note that this number is not unique - cases from different courts could share the same case number) 
* *case_link* is the URL of the case record in PACER (requires login to view)
* *oil_gas* is a classification we the company involved in each suit: y = oil and gas; n = not oil and gas; m = ambiguous
* *company_name* is the name of company involved in the suit

## Data Sources

Inside Energy downloaded from [PACER](http://www.pacer.gov) (login required to access case search):
* Fair Labor Standards Act lawsuits from Colorado filed in federal courts between January 1, 2010 and December 31, 2015
* Fair Labor Standards Act lawsuits from Texas filed in federal courts between January 1, 2010 and December 31, 2015

## Notes and Methods

Inside Energy determined whether companies involved in the FLSA lawsuits were oil and gas companies, not oil and gas companies, or ambiguous. 

For Colorado, which had 440 FLSA lawsuits, Inside Energy staff examined each company (defendant) name. This process included flagging known oil and gas companies and doing web searches.

For Texas, which had nearly 5,000 FLSA lawsuits, we first used Mechanical Turk to classify 500 companies, which Inside Energy staff examined for accuracy. Next, we used a search algorithm (code and notes [here](https://github.com/InsideEnergy/TX-flsa-lawsuits)) to classify companies by keyword. Finally, Inside Energy staff examined the remaining company names via web searches.

To determine whether a company was oil and gas, we used this definition outlined by the Burea of Labor Statistics:

"Industries in the Oil and Gas Extraction subsector operate and/or develop oil and gas field properties. Such activities may include exploration for crude petroleum and natural gas; drilling, completing, and equipping wells; operating separators, emulsion breakers, desilting equipment, and field gathering lines for crude petroleum and natural gas; and all other activities in the preparation of oil and gas up to the point of shipment from the producing property. This subsector includes the production of crude petroleum, the mining and extraction of oil from oil shale and oil sands, and the production of natural gas, sulfur recovery from natural gas, and recovery of hydrocarbon liquids."

This also includes support activities for oil and gas, such as: 
"Services included are exploration (except geophysical surveying and mapping); excavating slush pits and cellars, well surveying; running, cutting, and pulling casings, tubes, and rods; cementing wells, shooting wells; perforating well casings; acidizing and chemically treating wells; and cleaning out, bailing, and swabbing wells."

Refineries, utilities and oil- and gas-fired power plants are not typically included in this definition and should not be considered oil and gas companies.
