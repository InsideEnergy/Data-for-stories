# U.S. Coal Basins Snapshot
This repository contains basic data about the major U.S. coal basins (Powder River Basin, Uinta, Illinois, Central Appalachia, Northern Appalachia), as well as shape files of the basin areas.

## What's in this repository?

This repository includes the data used for the graphics in the Inside Energy story, ["To Mine Or Not To Mine? Is That The Question?"](http://insideenergy.org/2015/08/24/to-mine-or-not-to-mine-is-that-the-question/).

## Data dictionary

The data files *coal-basins-snapshot.csv* and *coal-basins-snapshot.xlsx* include the following information, as of August 14, 2015, for the major U.S. coal basins:
* *Basin* is the name of the coal basin (Powder River, Uinta, Illinis, Central and Northern Appalachia)
* *price-per-ton-dollars* is the price, in dollars, for a ton of coal from that basin. Note from the EIA: "Coal prices shown are for a relatively high-Btu coal selected in each region, for delivery in the "prompt quarter." The prompt quarter is the quarter following the current quarter. For example, from January through March, the 2nd quarter is the prompt quarter."
* *Btu-per-pound* is the amount of energy, in Btu, in a typical pound of coal from that basin.
* *S02-percent-per-pound* is the percent value of sulfer contained in a typical pound of coal from that basin. 

Shape files for each of the coal basins were created by creating composites of the individual coal fields shape files available from the USGS. This repository has a zip file for each basin, which contains the required shape files (.dbf, .shp, .shx, .prj, .qpj).

## Data Sources

The original source of the general coal data is the Energy Information Administration's [Coal News and Markets page](http://www.eia.gov/coal/news_markets/). Note that the EIA updates coal prices weekly, and cannot publish historical price data.

The original source of the shape files is the U.G. Geological Survey's ["Coal Fields of the Coterminous United States"](http://pubs.usgs.gov/of/2012/1205/) which Inside Energy used to make composite basins that align with the EIA's definitions.
