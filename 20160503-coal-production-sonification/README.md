# Sonifying Weekly U.S. Coal Production
Data and notes on data cleaning and sonifying of U.S. weekly coal production data.

## What's in this repository?

This repository includes the data used in the story, ["TK Story Title"](URL).

The data files *coal_prod_1984_2016_weeks_summed.csv* and *coal_prod_1984_2016_weeks_summed.xlsx* contain weekly data for U.S. coal production, in tons, from the beginning of 1984 through the first quarter of 2016 (week 16). (Note that the csv file does not include headers).:
* *Year* 
* *Week* - 1 through 53 (in some cases)
* *Coal Production (tons)*

The iPython notebook *Sonification.ipynb* contains the Python script used to map the weekly coal production data onto a MIDI file.

The scripts for bulk downloading the weekly coal production files from the Energy Information Administration are in *EIA_coal_download.py*.


## Data Sources

Weekly coal production data is from the Energy Information Administration, available [here]("https://www.eia.gov/coal/production/weekly/includes/archive.cfm").

## Notes and Methods

Data Processing:
* Downloaded data files for weekly coal production (EIA archives files annually), 1984 through 2016
* Selected U.S. total coal production
* Some weeks were split into two records (i.e., because the week spanned two separate quarters), so those weeks were summed
* Compiled all of the data into one file, *coal_prod_1984_2016_weeks_summed.csv*
* Removed outlier weeks, which were caused by short weeks at the beginning/end of the year or holiday weeks (Fourth of July)
* Adapted [MIDITime]("https://github.com/cirlabs/miditime") package to produce MIDI file where each week is mapped to a tone (5 octaves, roughly 9 weeks per second)
