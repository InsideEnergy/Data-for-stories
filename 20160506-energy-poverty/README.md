# The Gap Between Energy Need and Available Energy Assistance
Data and notes on energy assistance available from the federal government's Low Income Housing Energy Assistance Program (LIHEAP).

## What's in this repository?

This repository includes the data used in the story, ["High Utility Costs Force Hard Decisions"](URL).

The data files *state_energy_assistance_shortfall.csv* and *state_energy_assistance_shortfall.xlsx* contain annual data for 2012 to 2015, by state, on the energy bill need, the number of low-income households, the LIHEAP funds allocated, the gap between the needs and the funds (total), and the average household gap:
* *YYYY_Need* -  Is the state energy bill shortfall, as defined by how much low-income families have to pay, annually, over 6% of their incomes on energy. (See notes below.)
* *YYYY_Households* - The number of households below 200% of the federal poverty level. 
* *YYYY_LIHEAP* - The total funds released in that fiscal year (defined as October 1 - September 30) from the LIHEAP program.
* *YYYY_total_gap* - The difference between YYYY_Need and YYYY_LIHEAP.
* *YYYY_household_gap* - The total gap divided by the number of households.

This data file also contains four-year averages (2012 - 2015) for the total energy need/assistance gap and the household need/assistance gap.

## Data Sources and Notes

* LIHEAP funding allocation data comes from the U.S. Department of Health and Human Services Low Income Home Energy Assistance Program, [available here](https://liheapch.acf.hhs.gov/Funding/funding.htm).
* Energy need and households comes from analysis by independent firm Accounting Insights, who shared their data with Inside Energy. Accounting Insights estimated annual energy bill in each U.S. county, modeled by combining energy data from the Energy Information Administration (eneryg mix, use, prices) and demographic data (household size, tenure) from the U.S. Census Bureau's American Community Survey. Then, based on an assumed "affordable" energy bill of 6% of household income, they calculated how much low-income families are spending each year above that affordable level. You can find a more detailed description of Accounting Insight's data methods [here](http://insideenergy.org/files/2016/05/2015-ConnecticutHEAG-11-30-15.pdf).