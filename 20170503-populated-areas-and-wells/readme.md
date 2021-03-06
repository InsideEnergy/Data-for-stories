# How Many People In Colorado Live In Oil And Gas Zones?

This repository explains the methods Inside Energy used to determine how many Coloradoans are living in areas with a high density of wells. We used this method to do analysis for the story, ["Colorado Governor Orders Review Of All Oil And Gas Operations"](http://insideenergy.org/2017/05/02/colorado-governor-orders-review-of-all-oil-and-gas-operations/). Our earlier investigation into the issue of [housing developements encroaching into historical oil and gas areas](http://insideenergy.org/2016/02/09/living-on-top-of-forgotten-oil-and-gas-wells/) used a similar analysis, and you can see those results [here](http://insideenergy.org/2016/02/09/where-people-meet-oil-and-gas-a-colorado-story-in-3-maps/).

![Animated gif of neighborhood where home explosion ocurred from 1999 to 2015](https://raw.githubusercontent.com/InsideEnergy/Data-for-stories/master/20170503-populated-areas-and-wells/images/Twilight-Ave-Images/twilight-ave-timelapse-slowed-small.gif)
*The fatal Oak Meadows home explosion occurred in an area with many wells that had been drilled in the 1990s, indicated by orange markers. In this time-lapse aerial view, from 1999 through 2015 new housing developments encroach upon the old wells. Data sources: COGCC, Google Earth. Image by Jordan Wirfs-Brock for Inside Energy.*

## Overview
We wanted to answer the question, "How many people in Colorado live in areas with a lot of oil and gas development, and how has that number changed over time?" To do this, we identified geographic areas that were both a) densely populated, which we defined as more than 500 people per square kilometer, and b) dense with wells, which we defined as more than 1 well per square kilometer. We then looked at how the number of people living in those zones changed over time.

## Files in this repository
You'll find shapefiles for 2010 and 2015 census tracts that include tract area (km^2), well count, ACS population estimates, margin of error, well density (wells/km^2), and population density (people/km^2). This data is also available as a CSV file.

Relevant field names 2010 file:
* area_km2 - land plus water area, in square kilometers
* geoid10 - unique identifier
* intersect_ - well count
* well_den - well density, in wells per square kilometer
* popden2 - population density, in people per square kilometer
* 2010_pop_3 - ACS population estimate
* 2010_pop_4 - ACS margin of error

Relevant field names 2015 file:
* area_km2 - land plus water area, in square kilometers
* geoid - unique identifier
* intersect_ - well count
* well_den - well density, in wells per square kilometer
* pop_den - population density, in people per square kilometer
* ACS_15_5_3 - ACS population estimate
* ACS_15_5_4 - ACS margin of error

This respositiory also includes images of the neighborhood where the April 17, 2017 home explosion in Firestone occurred, with an overlay of well locations, dating from 1999 to 2015, as well as an animated gif showing the expansion of homes. These are in the images --> Twilight-Ave-Images folder. Time-series images of other high-growth areas are in Greeley and Thornton are also included.

## Data Sources
* **Oil and gas wells** - Colorado Oil and Gas Conservation Commission's (COGCC) [database of oil and gas well surface locations](http://cogcc.state.co.us/data2.html#/downloads)
* **Population data** - U.S. Census Bureau American Community Survey 5-year estimates for [2015](https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=ACS_15_5YR_B01003&prodType=table) (2011-2015) and [2010](https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=ACS_15_5YR_B01003&prodType=table) (2006-2010), at the census tract level
* **Geographics** - U.S. Census Bureau Tiger/LINE shape files, census tracts for [2010](https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2010&layergroup=Census+Tracts) and [2015](https://www.census.gov/cgi-bin/geo/shapefiles/index.php)

## Methods
Here is a high-level description of our methods, which we repeated for both 2010 and 2015.
* *Calculate area of each census tract* - The geography files include land area and water area, in square meters. We added these together to come up with the total area of each census tract, and then converted to square kilometers.
* *Filter wells by spud date* - We filtered the wells file for those with null spud dates or dates through December 31, 2010 and December 31, 2015, respectively. Most null spud dates indicate that the well is old and data on it no longer exists, so we assumed that these were drilled prior to 2010.
* *Join wells with census tracts* - We joined the wells layer to the census tracts layer, counting the number of wells within each tract.
* *Calculate population density* - Divide the number of wells by the tract area to come up with wells per square kilometer.
* *Join with population data* - Using the unique geoid, join the ACS population data to the geographics.
* *Calculate population density* - Divide the population estimate by the tract area to come up with people per square kilometer.

We then filtered for census tracts that had both a well density greater than 1 / square kilomter and a population density greater than 500 / square kilometer. For the front range, those regions are shown below, in yellow:

![Areas dense with people and wells](https://raw.githubusercontent.com/InsideEnergy/Data-for-stories/master/20170503-populated-areas-and-wells/images/2010-2015-high-density-areas.gif)
*On Colorado’s Front Range, regions that are dense with both people and wells are increasing. On this map, yellow areas have more than 500 people per square kilometer and more than one well per square kilometer, based on Inside Energy analysis of U.S. Census Bureau and Colorado Oil and Gas Conservation Commission data. Image credit: Jordan Wirfs-Brock | Inside Energy.*

We found that in 2015, there were **177,622 people** living in these densely populated, high oil and gas activity zones, compared to **127,110** in 2010.

We also looked at the number of people living in all high oil and gas activity zones, and found 466,619 people in 2015, compared to 409,141 people in 2010.


*Note: Inside Energy did a similar analysis looking at the time period from 1990 to 2010. Note that in that analysis, we used decennial census data as opposed to ACS. In that analysis, we found that in 2010, 150,993 people live in dense oil and gas zones. It makes sense that this number would be higher than our ACS number, because the ACS data covers a 5-year period from 2006 to 2010.*

## Aerial Images

Inside Energy also made time-series images that show suburban development in former oil and gas areas, which you can view in this article, [Fatal Home Explosion In Colorado Reignites Setback Debate](http://insideenergy.org/2017/05/05/fatal-home-explosion-in-colorado-reignites-setback-debate/).

### Locations

The **North Thortnon** location is the intersection of E 128th Ave and Quebec St. [View full screen](https://cdn.knightlab.com/libs/juxtapose/latest/embed/index.html?uid=4adc995a-304e-11e7-a6aa-0edaf8f81e27)_

The **West Greeley** location is Miliken Rd/65th south of W 28th St. [View full screen](https://cdn.knightlab.com/libs/juxtapose/latest/embed/index.html?uid=3b2c65f2-3054-11e7-a6aa-0edaf8f81e27)

The **Firestone** location (animated gif) is at 6312 Twilight Ave, which is the location of the April 2017 home explosion.

### Tools and Data

Inside Energy used Knight Lab's [JuxtaposeJS](https://juxtapose.knightlab.com/) tool, Google Earth Pro, and the COGCC wells database.


## Contact

This analysis was done by Jordan Wirfs-Brock for [Inside Energy](http://insideenergy.org). For more info, email jordanwb@gmail.com or Inside Energy's executive editor Alisa Barba, alisabarba@rmpbs.org.

## License

This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nc-nd/4.0/).
![cc-by-nd-4.0](https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png)
