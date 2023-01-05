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

4) calculate the anomalies (WRT to 1991 - 2020 climatology) in mm and percentage of normal then plots (maps) the average rainfall and anomalies for a chosen date (year-month) from MSWEP: 

```
notebooks/plot_monthly_maps_MSWEP.ipynb 
```

5) calculate the longitudinal sectors averages from MSWEP and plots (x-axis = Rainfall in mm, y-axis = latitude)


```
notebooks/plot_sectors_MSWEP.ipynb 
```

6) calculate longitudinal sector averages as above and compares a chosen 3 months season to recent ENSO years composites (La Nina, El Nino and Neutral) based on the 3 months values of the Oceanic Nino Index (ONI) downloaded from NOAA at [https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt](https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt). 


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
