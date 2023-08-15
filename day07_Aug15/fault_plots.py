# -*- coding: utf-8 -*-
# Eric Lindsey, 04/2016

from mpl_toolkits.mplot3d import art3d
#from mpl_toolkits.mplot3d import Axes3D,art3d
#from mpl_toolkits.mplot3d import proj3d
#from matplotlib.colors import colorConverter
from matplotlib import collections

import matplotlib.pyplot as plt
import numpy as np
#import geod_transform

class FaultPlot3D:
    
    def __init__(self):
        self.fig = plt.figure(figsize=plt.figaspect(1.)*1.)
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_xlabel('Longitude')
        self.ax.set_ylabel('Latitude')
        
        self.ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
        self.ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
        self.ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))        
        self.set_zlim(-4,100)
        self.ax.set_zlabel('Depth (km)')
    
    def get_ax(self):
        return self.ax
    
    def showmap(self):
        #self.ax.auto_scale_xyz([0,1],[0,1],[0,1]) #doesn't work
        plt.show()

    def set_zlim(self,zmin,zmax):
        self.ax.set_zlim3d(zmin,zmax)
        self.ax.invert_zaxis()
        
    def set_lims(self,xlims,ylims,zlims):
        self.ax.set_xlim3d(xlims[0],xlims[1])        
        self.ax.set_ylim3d(ylims[0],ylims[1])
        self.set_zlim(zlims[0],zlims[1])
        
    def plot_outlines(self,lon,lat,elev,*args,**kwargs):
        self.ax.plot(lon,lat,elev,*args,**kwargs)
        
    def plot_shapefile(self,fname):
        import shapefile # requires shapefile.py, from pyshp package
        #note, if you need to crop the shapefile use ogr2ogr, e.g.:
        #ogr2ogr -f "ESRI Shapefile" <output>.shp <input>.shp -clipsrc 94 107 -6 6
        coast = shapefile.Reader(fname)     
        for shape in coast.shapes():   
            x, y = zip(*shape.points)
            self.ax.plot(x,y,color='k')
        # another attempt that doesn't quite work:
        #shp = shapereader.Reader('./data/GSHHS/bts_GSHHS_f_L1')
        #for record, geometry in zip(shp.records(), shp.geometries()):
        #    self.ax.add_geometries([geometry], ccrs.PlateCarree(), facecolor='lightgray',edgecolor='black')
        
    def plot_symbols(self,lon,lat,elev,*args,**kwargs):
        self.ax.plot(lon,lat,elev,*args,**kwargs)
    
    def plot_vectors(self,lon,lat, veast,vnorth, *args,**kwargs):
        self.ax.quiver(lon,lat, veast, vnorth, angles='xy',scale_units='xy', *args, **kwargs)
    
    def plot_up_vectors(self,lon,lat, vup, *args,**kwargs):
        self.ax.quiver(lon,lat, 0, vup, angles='xy',scale_units='xy', *args, **kwargs)
            
    def plot_slip_patches(self,Fmodel,slip,clim=[],*args,**kwargs):
        verts=Fmodel.get_patch_verts_center_3d()
        
        poly=art3d.Poly3DCollection(verts)
        poly.set_zsort('min')
        colset = np.array(slip) 
        poly.set_array(colset)
        if (len(clim)==2):
            poly.set_clim(clim[0],clim[1])
        else:
            poly.set_clim(min(slip),max(slip))  
        self.ax.add_collection3d(poly,*args,**kwargs)
        self.fig.colorbar(poly)
        
class FaultPlot2D:
    
    def __init__(self,figsize):
        self.fig = plt.figure(figsize=figsize)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel('Longitude')
        self.ax.set_ylabel('Latitude') 
        self.ax.axis('equal')
       
    def get_ax(self):
        return self.ax
    
    def showmap(self):
        #self.ax.auto_scale_xyz([0,1],[0,1],[0,1]) #doesn't work
        plt.show()
     
    def set_lims(self,xlims,ylims):
        self.ax.set_xlim(xlims[0],xlims[1])        
        self.ax.set_ylim(ylims[0],ylims[1])
        
    def plot_outlines(self,lon,lat,*args,**kwargs):
        self.ax.plot(lon,lat,*args,**kwargs)
        
    def plot_shapefile(self,fname):
        import shapefile # requires shapefile.py, from pyshp package
        #note, if you need to crop the shapefile use ogr2ogr, e.g.:
        #ogr2ogr -f "ESRI Shapefile" <output>.shp <input>.shp -clipsrc 94 107 -6 6
        coast = shapefile.Reader(fname)     
        for shape in coast.shapes():   
            x, y = zip(*shape.points)
            self.ax.plot(x,y,color='k')
        # another attempt that doesn't quite work:
        #shp = shapereader.Reader('./data/GSHHS/bts_GSHHS_f_L1')
        #for record, geometry in zip(shp.records(), shp.geometries()):
        #    self.ax.add_geometries([geometry], ccrs.PlateCarree(), facecolor='lightgray',edgecolor='black')
        
    def plot_symbols(self,lon,lat,*args,**kwargs):
        self.ax.plot(lon,lat,*args,**kwargs)
    
    def plot_vectors(self,lon,lat, veast,vnorth, *args,**kwargs):
        self.ax.quiver(lon,lat, veast, vnorth, angles='xy',scale_units='xy', *args, **kwargs)
    
    def plot_up_vectors(self,lon,lat, vup, *args,**kwargs):
        self.ax.quiver(lon,lat, 0*vup, vup, angles='xy',scale_units='xy', *args, **kwargs)

    def plot_slip_outlines(self,Fmodel,*args,**kwargs):
        verts=Fmodel.get_patch_verts_center_2d()
        # Extract segments and corresponding colors
        segments = []
        colors = []
        for poly in verts:
            n=len(poly)
            for i in range(n):
                start_point = poly[i]
                end_point = poly[(i + 1) % n]  # Use modulo to wrap back to the first point
                segment = [start_point, end_point]
                segments.append(segment)
                # If it's the first segment of the polygon, color it green, otherwise red
                if i == 0:
                    colors.append('black')
                else:
                    colors.append('red')
        # Create a LineCollection
        line_collection = collections.LineCollection(segments, colors=colors, linewidths=2)
        self.ax.add_collection(line_collection,*args,**kwargs)

        
        
    def plot_slip_patches(self,Fmodel,slip,clim=[],colorbar=True,*args,**kwargs):
        verts=Fmodel.get_patch_verts_center_2d()
        poly=collections.PolyCollection(verts)
        colset = np.array(slip)
        poly.set_array(colset)
        if (len(clim)==2):
            poly.set_clim(clim[0],clim[1])
        else:
            poly.set_clim(min(slip),max(slip))  
        self.ax.add_collection(poly,*args,**kwargs)
        if colorbar:
            self.fig.colorbar(poly)
        