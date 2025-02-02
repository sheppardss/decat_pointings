import matplotlib.pyplot as plt
import numpy as np
from astropy.time import Time
from astroplan import FixedTarget, Observer
from astroplan.plots import plot_airmass
from astropy import units as u
from astropy.coordinates import SkyCoord, get_moon, EarthLocation

def doplot(timestr='2021-04-29',ra=125.203408,dec=-12.598140,name='2021koj',site='CTIO',block=True):
    
    time = Time(timestr) + 24*u.hour + np.linspace(-3.0, 14, 100)*u.hour

    apo = Observer.at_site(site)
    
    SN_coord = SkyCoord(ra=ra*u.deg, dec=dec*u.deg)
    moon_coord = get_moon(time,location=EarthLocation.of_site('CTIO'))
    
    sn_moon_sep = min(moon_coord.separation(SN_coord).degree)
    
    SN_target = FixedTarget(coord=SN_coord, name='%s: %d deg moon sep'%(name,sn_moon_sep))
    print('%s: %d deg moon sep'%(name,sn_moon_sep))
    moon_target = FixedTarget(coord=moon_coord, name='Moon')

    moon_styles = {'linestyle': ':', 'color': 'grey'}
    SN_styles = {'color': 'k', 'linewidth': 3}
    
    plot_airmass(moon_target, apo, time, brightness_shading=True, altitude_yaxis=True,style_kwargs=moon_styles)
    plot_airmass(SN_target, apo, time, brightness_shading=True, altitude_yaxis=True,style_kwargs=SN_styles)
    
    plt.legend(shadow=True,loc=4)
    plt.tight_layout()
    plt.show(block=block)

if __name__ == '__main__':    
    doplot()
