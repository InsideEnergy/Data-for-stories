import pandas as pd
import numpy as np
import csv
import urllib

# Download coal data files for 1984 through 2015
def DownloadFile(url, filename):
    testfile = urllib.URLopener()
    testfile.retrieve(url, filename)

# Takes in a list of the years you want, downloads the Excel data files from EIA
def DownloadMultipleYears(startyear, endyear):
    years = range(startyear,endyear+1)
    for item in years:
        link = "https://www.eia.gov/coal/production/weekly/archive/weekprod" + str(item) + "tot.xls"
        filename = str(item) + ".xls"
        DownloadFile(link,filename)

# Download data from 1984 to 2016
DownloadMultipleYears(1984,2016)