### Filling In The Natual Gas Gaps

The map shows populations of North Dakota communities with and without natural gas, as well as the natural gas pipeline network.

### What's in this folder?

This is the raw data used to make the map in the Inside Energy story [Filling In The Natural Gas Gaps](http://insideenergy.org/2017/04/06/filling-in-the-natural-gas-gaps/).

* **nd_places_1000_greater:** names, locations and populations of all communities in North Dakota with a population of 1,000 or more that do not have natural gas service. Communities with fewer than 1,000 residents were eliminated because many have dozens or only a few hundred residents, and are less likely to be feasible options for extending natural gas service.
* **nd_small_nat_gas_communities:** names, locations and populations of all communities in North Dakota with natural gas service

### Where does this data come from?

* Cities listed in "nd_places_1000_greater" and "nd_small_nat_gas_communities": [North Dakota Public Service Commission](http://www.psc.nd.gov/) -- The PSC maintains a list of cities with and without natural gas service, which were verified by looking at [MDU](https://www.montana-dakota.com/utility-menu/about-us/communities-served) and [Xcel Energy](https://www.xcelenergy.com/staticfiles/xe/Regulatory/Regulatory%20PDFs/rates/ND/Ng_Section_3.pdf)'s websites.
* Populations listed in "nd_places_1000_greater" and "nd_small_nat_gas_communities": [U.S. Census Bureau American Fact Finder](https://factfinder.census.gov/faces/nav/jsf/pages/index.xhtml) -> Advanced Search -> Show Me All -> Geographies -> Place - 160 -> North Dakota -> All places within North Dakota -> Add To Your Selections -> Topics -> People -> Basic Count/Estimate -> Population Total -> TOTAL POPULATION in row with B01003 and 2015 ACS 5-year estimates
* Pipeline network: [Energy Information Administration](https://www.eia.gov/maps/layer_info-m.php) -- Find on page "Natural Gas Interstate and Intrastate Pipelines" and click on "Shapefile" to download data.

### How did we make the map?

We used [carto.com](https://carto.com/) to build the map.