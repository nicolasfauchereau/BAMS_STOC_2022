<!-- #region -->
# code to produce the figures included in the BAMS "State of the Climate" report section on Pacific Convergence Zones 

1) update the MSWEP daily dataset: 

```
rclone sync -v --exclude 3hourly/ --exclude Monthly/ --drive-shared-with-me GoogleDrive:/MSWEP_V280 /media/nicolasf/END19101/ICU/data/glo2ho/MSWEP280
```

2) calculate the MSWEP monthly climatology (1991 - 2020): 

```
notebooks/calculate_MSWEP_monthly_from_daily_climatology.ipynb
```

3) calculate the monthly averages for each year, as well as the anomalies: 

```
notebooks/calculate_MSWEP_monthly_from_daily.ipynb
```

4) calculate and plots the monthly / seasonal precipitation anomalies maps from MSWEP: 

```
notebooks/plot_monthly_maps_MSWEP.ipynb 
```

5) calculate and plots the sector plots from MSWEP: 


```
notebooks/plot_sectors_MSWEP.ipynb 
```

6) calculate and plot the longitudinal averages for ENSO years and neutral years + current year: 

```
notebooks/plot_ENSOs_vs_current_year_MSWEP.ipynb
```


### Additional notebooks: 

```
notebooks/ERSST_Pacific_anomalies.ipynb: 
```

calculates and plot the ERSST SST anomalies for each month of the year to process

There are also some versions of the above notebooks using CMAP (downloaded from ) for comparison with MSWEP ... 












<!-- #endregion -->

2) in `notebooks`: 

+ [plot_monthly_maps.ipynb](https://github.com/nicolasfauchereau/BAMS_SOTC_2019/blob/master/notebooks/plot_monthly_maps.ipynb) calculates the anomalies (WRT to 1998 - 2018 climatology) in mm and percentage of normal then plots (maps) the average rainfall and anomalies for a chosen date (year-month) 
+ [plot_sectors.ipynb](https://github.com/nicolasfauchereau/BAMS_SOTC_2019/blob/master/notebooks/plot_sectors.ipynb) calculates the longitudinal sectors averages and plots (x-axis = Rainfall in mm, y-axis = latitude)
+ [plot_ENSOs_vs_current_year.ipynb](https://github.com/nicolasfauchereau/BAMS_SOTC_2019/blob/master/notebooks/plot_ENSOs_vs_current_year.ipynb) calculates longitudinal sector averages as above and compares a chosen 3 months season to recent ENSO years composites (La Nina, El Nino and Neutral) based on the 3 months values of the Oceanic Nino Index (ONI) downloaded from NOAA at [https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt](https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt). 

