# Sonifying Weekly U.S. Coal Production
Data and notes on data cleaning and sonifying of U.S. weekly coal production data.

## What's in this repository?

This repository includes the data used in the story, ["Listen To U.S. Coal Production Fall Off A Cliff"](http://insideenergy.org/2016/05/03/listen-to-u-s-coal-production-fall-off-a-cliff/).

The data files *coal_prod_1984_2016_weeks_summed.csv* and *coal_prod_1984_2016_weeks_summed.xlsx* contain weekly data for U.S. coal production, in tons, from the beginning of 1984 through the first quarter of 2016 (week 16). (Note that the csv file does not include headers).:
* *Year* 
* *Week* - 1 through 53 (in some cases)
* *Coal Production (tons)*

The iPython notebook *Sonification.ipynb* contains the Python script used to map the weekly coal production data onto a MIDI file.

The scripts for bulk downloading the weekly coal production files from the Energy Information Administration are in *EIA_coal_download.py*.


## Data Sources

Weekly coal production data is from the Energy Information Administration, available [here](https://www.eia.gov/coal/production/weekly/includes/archive.cfm).

## Notes and Methods

Data Processing:
* Downloaded data files for weekly coal production (EIA archives files annually), 1984 through 2016
* Selected U.S. total coal production
* Some weeks were split into two records (i.e., because the week spanned two separate quarters), so those weeks were summed
* Compiled all of the data into one file, *coal_prod_1984_2016_weeks_summed.csv*
* Removed outlier weeks, which were caused by short weeks at the beginning/end of the year or holiday weeks (Fourth of July)
* Adapted [MIDITime](https://github.com/cirlabs/miditime) package to produce MIDI file where each week is mapped to a tone (5 octaves, roughly 9 weeks per second)

Note: The EIA releases new coal production estimates every week. After the data has been published, they go back and adjust those numbers based on quarterly Mining Safety and Health Administration data. Typically, those revisions result in very minor adjustments in the national production totals. [(More information about the revision process from the EIA.)](https://www.eia.gov/coal/production/weekly/includes/archive.cfm) Note that, because they are so recent, the 2016 weekly coal production data has not yet been revised.

Special thanks to Mike Corey, who developed [MIDITime](https://github.com/cirlabs/miditime).
