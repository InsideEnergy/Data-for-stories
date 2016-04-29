# U.S. Small Wind Capacity

Total distributed wind capacity in the U.S. for generators 100kW or smaller, from 2003-2014.

### What's in this folder?

This is the raw data used in the Inside Energy story [IE Questions: What Size Wind Generator Does An Average House Need?](ie-questions-what-size-wind-generator-does-an-average-house-need)

### Where does this data come from?

Source: [The Department of Energy's 2014 Distributed Wind Market Report](http://energy.gov/eere/wind/downloads/2014-distributed-wind-market-report)

### Data Dictionary

In our data, the columns `year`, `total-us-distributed-wind-cumulative-MW`, `annual-additional-capacity-MW` and `annual-additional-capacity-100-kw-or-smaller-MW` come directly from the [Data Table](http://energy.gov/sites/prod/files/2015/08/f26/2014%20DW%20Market%20Report%20Data%20Tables-082415.xlsx) that accompanies the report. (There is a lot of great stuff there if you're interested.)

To generate the `total-capacity-100kw-or-smaller-MW`, which drives the chart in our story, we summed each successive amount of additional capacity (from `annual-additional-capacity-100-kw-or-smaller-MW`).

### Note

These figures are only for small distributed wind installations, of 100KW capacity or smaller. Distributed wind describes localized projects, as opposed to utility-scale installations. 