# Mapping the Start/End Points of Colorado Oil and Gas Flowlines

This repository contains the data, methods and code Inside Energy used to create an interactive map of the start/end points of Colorado oil and gas flowline locations. You can view the [completed map](https://jordanwb.carto.com/viz/546dd09b-f711-4729-a4b4-eb9dca4dcf99/public_map) and read the accompanying web article [here](http://insideenergy.org/2017/06/28/mapping-colorados-invisible-pipeline-network/).

## About

In the wake of a home explosion in Fireston, Colorado, Governor Hickenlooper requested that all oil and gas operators submit the locations of flowlines that are within 1000 ft. of buildings. On June 27, 2017, the Colorado Oil and Gas Conservation Commission made the start/end points of oil and gas flowlines available for the first time.

The original dataset is available for download from COGCC: [Flowline Inventory](https://cogcc.state.co.us/documents/data/downloads/Engineering/flowline/FlowlineDownload.html)

The data contains the start and end locations of different types of flowlines: process piping, wellsite flowlines, dump lines, etc. It does not include the actual routes of the flowlines. We played around with a few ways to visualize this data on a map, including just showing the point locations of the start and end of each line. Ultimately, Inside Energy decided to show a line connecting the start and end points. Note that this does not indicate the exact flowline route. However, we felt that this was the most useful way to quickly and visually identify where the flowlines are.

_Tools we used for this project: Python with Jupyter and pandas; QGIS with Points2One plugin; Carto._

## What's in this repository?

In this repository, you'll find:
* [COGCC-flowlines.ipynb](COGCC-flowlines.ipynb) - A Jupyter notebook with the Python code we used to clean the data before we created the flowline shape files
* [All_Start_End.csv](All_Start_End.csv) - The cleaned start and end point location file
* [All_Flowline_Info.csv](All_Flowline_Info.csv) - The flowline info lookup file
* [flowlines-info-length.zip](flowlines-info-length.zip) - The final shape files, zipped
* [Flowline](Flowline) - The original download from the COGCC (download date: June 27, 2017), unzipped containing .xls file and data dictionary (note: we removed the .mdb file).

## Basic method

Here are the rough steps we used to clean and map the data:
1. Clean and prepare data with Python/pandas (format, remove irregular/missing data points). View the full method and code [here](COGCC-flowlines.ipynb).
2. Import into QGIS and use Points2One plugin to draw straight lines between the start and end points. Calculate length of each line.
3. Map in Carto, filter out flowlines longer than 1500m.

By Jordan Wirfs-Brock for Inside Energy. Questions or comments? Contact jordanwb@gmail.com.
