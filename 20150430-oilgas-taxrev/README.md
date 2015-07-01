# Oil and Gas Tax Revenue

This is the raw data behind the story [Amidst Low Prices, North Dakota Scrambles To Change Oil Tax Rate](http://insideenergy.org/2015/04/30/amidst-low-prices-north-dakota-scrambles-to-change-oil-tax-rate/)

Source for data: [Annual Survey of State Government Tax Collections](http://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=bkmk)
Source for top 10 oil producing states: [U.S. Energy Information Administration](http://www.eia.gov/state/rankings/?sid=US#/series/46)

`taxes-collected`: total tax revenue for each state

`severance_taxes`: revenue from severance taxes, or taxes incurred when extracting non-renewable resources

`percent_severance`: `severance_taxes`/`taxes-collected`

Our story includes a visualization of `percent_severance` for the top 10 oil producing states. In this dataset, we include this information for all 50 states and the country as a whole. 

The dataset does not list severance tax revenue for all states (indicated by `X`). According to the Census, this means that data point is "[not applicable](http://factfinder.census.gov/faces/affhelp/jsf/pages/metadata.xhtml?lang=en&type=table&id=table.en.STC_2014_STC005#main_content)" for that state.