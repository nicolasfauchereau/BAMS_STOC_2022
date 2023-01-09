from matplotlib import pyplot as plt 
import numpy as np 
from cartopy import crs as ccrs 
from cartopy import feature as cfeature 
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter


def plot_map(dataset, date, varname='precipitation', fname=None, units="Rainfall anomalies (mm.day$^{-1}$)", title=None, vmin=-12, vmax=12, step=2, cmap=plt.cm.RdBu_r, norm=None, contour=None, colors=None):
    
    f, ax = plt.subplots(subplot_kw={'projection':ccrs.PlateCarree(central_longitude=180)}, figsize=(12,10))

    if norm is not None: 
    
        im = ax.contourf(dataset.lon, dataset.lat, dataset.sel(time=date)[varname], \
                         transform = ccrs.PlateCarree(central_longitude=0), \
                         levels = np.arange(vmin, vmax + step, step), \
                         extend = 'both', \
                         cmap = cmap, norm=norm)
    else:
        
        im = ax.contourf(dataset.lon, dataset.lat, dataset.sel(time=date)[varname], \
                         transform = ccrs.PlateCarree(central_longitude=0), \
                         levels = np.arange(vmin, vmax + step, step), \
                         extend = 'both', \
                         cmap = cmap, norm=norm)

    if contour is not None: 
        
        if type(contour) is not list: 
            contour = [contour]
            
        if colors is None: 
            colors = 'k'
        
        cb = ax.contour(dataset.lon, dataset.lat, dataset.sel(time=date)[varname], \
                         transform = ccrs.PlateCarree(central_longitude=0), \
                         levels = contour, colors=colors)
        
    cb = plt.colorbar(im, shrink=0.8, pad=0.09, orientation='horizontal', aspect=30)

    cb.set_label(units, fontsize=14)

    [l.set_fontsize(13) for l in cb.ax.xaxis.get_ticklabels()]

    xticks = np.arange(0, 360, 40)
#     xticks = np.arange(0, 360, 10)

    yticks = [-30., 0, 30.]
#     yticks = np.arange(-40, 50, 10)

    gl = ax.gridlines(draw_labels=False, linewidth=0., linestyle='--', xlocs=xticks, ylocs=yticks, crs=ccrs.PlateCarree())

    ax.set_xticks(xticks, crs=ccrs.PlateCarree())

    ax.set_yticks(yticks, crs=ccrs.PlateCarree())

    ax.coastlines(resolution='50m', zorder=10, lw=1)

    lon_formatter = LongitudeFormatter(zero_direction_label=True, dateline_direction_label=True) 

    lat_formatter = LatitudeFormatter()

    ax.xaxis.set_major_formatter(lon_formatter)

    ax.yaxis.set_major_formatter(lat_formatter)

    #     [l.set_fontsize(13) for l in ax.yaxis.get_ticklabels()]
    #     [l.set_fontsize(13) for l in ax.xaxis.get_ticklabels()]

    [l.set_fontsize(10) for l in ax.yaxis.get_ticklabels()]
    [l.set_fontsize(10) for l in ax.xaxis.get_ticklabels()]
    
    ax.set_extent([dataset.lon.data.min(), dataset.lon.data.max(), dataset.lat.data.min(), dataset.lat.data.max()], crs=ccrs.PlateCarree())

    if title is not None: 
        ax.set_title(title, fontsize=14) 

    if fname is not None: 
        f.savefig(fname, dpi=400, bbox_inches='tight', facecolor='w')  
        f.savefig(fname.replace(".png",".ps"), facecolor='w')
        f.savefig(fname.replace(".png",".pdf"), facecolor='w')
        f.savefig(fname.replace(".png",".svg"), facecolor='w')

def plot_clim(dataset, month, varname='precipitation', fname=None, units="Rainfall (mm.day$^{-1}$)", title=None, vmin=-12, vmax=12, step=2, contour=10, colors=None, cmap=plt.cm.RdBu_r, norm=None):
        
    f, ax = plt.subplots(subplot_kw={'projection':ccrs.PlateCarree(central_longitude=180)}, figsize=(12,10))

    if norm is not None: 
    
        im = ax.contourf(dataset.lon, dataset.lat, dataset.sel(month=month)[varname], \
                         transform = ccrs.PlateCarree(central_longitude=0), \
                         levels = np.arange(vmin, vmax + step, step), \
                         extend = 'both', \
                         cmap = cmap, norm=norm)
    else:
        
        im = ax.contourf(dataset.lon, dataset.lat, dataset.sel(month=month)[varname], \
                         transform = ccrs.PlateCarree(central_longitude=0), \
                         levels = np.arange(vmin, vmax + step, step), \
                         extend = 'both', \
                         cmap = cmap, norm=norm)
    
    if contour is not None: 
        
        if type(contour) is not list: 
            contour = [contour]
 
        if colors is None: 
            colors = 'k'
        
        cb = ax.contour(dataset.lon, dataset.lat, dataset.sel(month=month)[varname], \
                         transform = ccrs.PlateCarree(central_longitude=0), \
                         levels = contour, colors=colors)       

    cb = plt.colorbar(im, shrink=0.8, pad=0.09, orientation='horizontal', aspect=30)

    cb.set_label(units, fontsize=14)

    [l.set_fontsize(13) for l in cb.ax.xaxis.get_ticklabels()]

    xticks = np.arange(0, 360, 40)
#     xticks = np.arange(0, 360, 10)

    yticks = [-30., 0, 30.]
#     yticks = np.arange(-40, 50, 10)

    gl = ax.gridlines(draw_labels=False, linewidth=0., linestyle='--', xlocs=xticks, ylocs=yticks, crs=ccrs.PlateCarree())

    ax.set_xticks(xticks, crs=ccrs.PlateCarree())

    ax.set_yticks(yticks, crs=ccrs.PlateCarree())

    ax.coastlines(resolution='50m', zorder=10, lw=1)

    lon_formatter = LongitudeFormatter(zero_direction_label=True, dateline_direction_label=True) 

    lat_formatter = LatitudeFormatter()

    ax.xaxis.set_major_formatter(lon_formatter)

    ax.yaxis.set_major_formatter(lat_formatter)

    #     [l.set_fontsize(13) for l in ax.yaxis.get_ticklabels()]
    #     [l.set_fontsize(13) for l in ax.xaxis.get_ticklabels()]

    [l.set_fontsize(10) for l in ax.yaxis.get_ticklabels()]
    [l.set_fontsize(10) for l in ax.xaxis.get_ticklabels()]
    
    ax.set_extent([dataset.lon.data.min(), dataset.lon.data.max(), dataset.lat.data.min(), dataset.lat.data.max()], crs=ccrs.PlateCarree())

    if title is not None: 
        ax.set_title(title, fontsize=14) 

    if fname is not None: 
        f.savefig(fname, dpi=400, bbox_inches='tight', facecolor='w')
        f.savefig(fname.replace(".png",".ps"), facecolor='w')
        f.savefig(fname.replace(".png",".pdf"), facecolor='w')




