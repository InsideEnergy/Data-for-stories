# The Cost of Cleaning Up After Oil And Gas: Data on Well Depth and Well-Plugging Projects in Wyoming
This repository contains the data and code we used to do the analysis and graphics in the post ["The Rising Cost Of Cleaning Up After Oil And Gas"](http://insideenergy.org/2015/10/01/the-rising-cost-of-cleaning-up-after-oil-and-gas/), as well as additional data notes. We will be adding to this repository, so check back for more soon. 

## How did we estimate the cost to clean up Wyoming's newest wells that may potentially become orphaned?

Here's our basic methodology. The scripts we used (in the form of an IPython/Jupyter notebook) are coming soon.

* We looked at a database of wells in Wyoming to see how many that were first drilled in 2010 or earlier were designated as orphaned. Depending on the type of well, the orphan rate ranges from 3 to 4 percent.
* Based on information (well depth, cost) about the the well-plugging projects that Wyoming has completed in the past several years, we did a linear regression of cost and depth: cost = 12.3635*depth - 2211.21, p value < 0.0001.
* We looked at the wells drilled in Wyoming with a spud date (first drill date) that was 2011 or later (through August 2015).
* We set up a script to randomly select 3 percent (our estimated orphan rate) of those wells spudded from 2011 to 2015 and estimate the plugging costs of those wells based on their depth using our linear regression model.
* We ran this simulation 1,000 times and then looked at the average estimated cost to plug the orphaned wells, as well as the minimum and maximum estimated costs to plug the orphaned wells.
* We found that the average estimated cost to plug those of Wyoming's newest wells that may become orphaned is about $17 million, with a range from $15 to $19 million.