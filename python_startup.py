import sys
import os
if os.path.exists(os.environ['HOME']+'/TurbPlasma'):
   sys.path.insert(0,os.environ['HOME']+'/TurbPlasma/')
if os.path.exists(os.environ['HOME']+'/Py3D'):
   sys.path.insert(0,os.environ['HOME']+'/Py3D/')
import numpy as np
import scipy as sp
#import pyqtgraph as pg
import matplotlib.pyplot as plt
plt.ion()
from p3d import p3d
from p3do import p3do
import AnalysisFunctions as af
from scipy.ndimage import gaussian_filter as gf
from CFLIB.lib import faf


## Quick fix for imshow to show images in IDL like orientation
def imsh(a,**kwargs): plt.imshow(a.T,origin='low',**kwargs)

###################################################
###################################################
def read_block(input_file, i, nsp, sp , nlines, file_head_count,block_head_count):
   syscomm("head -"+str((sum(nlines)+nsp-1+block_head_count)*(i-1)+file_head_count\
   +(block_head_count+sp-1+sum(nlines[0:sp])))+" "\
   +input_file+" | tail -"+str(nlines[sp-1])+" >/tmp/dist.dat")
   c=np.fromfile("/tmp/dist.dat",dtype=float,count=-1,sep=" ")
   c=np.reshape(c,(nlines[sp-1],4))
   return c
###################################################
###################################################
def calc_dist(a,b,nbins):
   N=len(a)
   out=np.zeros((nbins,nbins),order='F')+1
   ax=np.linspace(a.min(),a.max(),nbins)
   bx=np.linspace(b.min(),b.max(),nbins)
   da=(a.max()-a.min())/nbins; db=(b.max()-b.min())/nbins
   for k in range(0,N):
      i=(a[k]-a.min())/da-0.5; i=int(i)
      j=(b[k]-b.min())/db-0.5; j=int(j)
      out[j,i]=out[j,i]+1
   
   return ax,bx,out
##################################################
##################################################

from subs import *


Py3D_path = '/glade/u/home/subash/Py3D/'
sys.path.append(Py3D_path)
import py3d as pd

which_code = 'p3dthon'
#which_code = 'Py3D'

if which_code == 'Py3D':
    Py3D_path = '/glade/u/home/subash/Py3D/'
    sys.path.append(Py3D_path)
    #from vdist_plotter import VDistPlotter
    #from movie import Movie
    #from sub import *
    #from PartTrace.testparticle import TPRun

    from Py3D.vdist_plotter import VDistPlotter
    from Py3D.movie import Movie
    from Py3D.sub import *
    from PartTrace.testparticle import TPRun

elif which_code == 'p3dthon':
    p3dthon_path = '/glade/u/home/subash/p3dthon/'
    sys.path.append(p3dthon_path+'objects/')
    sys.path.append(p3dthon_path+'scripts/')
    from p3d_runs import p3d_run
    import sub
    from  sub import *
