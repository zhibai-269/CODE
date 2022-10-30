def save_text(filename,edges):
    def save_txt():
        with open(filename, "w") as f:
            for edge in edges:
                f.write(str(edge[0]) + " " + str(edge[1]) + "\n")
import paraview
from paraview.simple import *
import os
import numpy as np
# trace generated using paraview version 5.11.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
input_surface_115017vtk = LegacyVTKReader(registrationName='input_surface_115017.vtk', FileNames=['D:\\PROJECT\\CODE\\matfile\\surfaces\\input_surface_115017.vtk'])

# find source
a115219_114823vtk = FindSource('115219_114823.vtk')

# find source
a116726_114823vtk = FindSource('116726_114823.vtk')

# find source
input_surface_114823vtk = FindSource('input_surface_114823.vtk')

# find source
a116221_114823vtk = FindSource('116221_114823.vtk')

# find source
a116524_114823vtk = FindSource('116524_114823.vtk')

# find source
input_surface_115017vtk_1 = FindSource('input_surface_115017.vtk')

# find source
a115825_114823vtk = FindSource('115825_114823.vtk')

# find source
input_surface_115219vtk = FindSource('input_surface_115219.vtk')

# find source
input_surface_115320vtk = FindSource('input_surface_115320.vtk')

# find source
input_surface_115825vtk = FindSource('input_surface_115825.vtk')

# find source
input_surface_116221vtk = FindSource('input_surface_116221.vtk')

# find source
input_surface_116726vtk = FindSource('input_surface_116726.vtk')

# find source
input_surface_116524vtk = FindSource('input_surface_116524.vtk')

# find source
input_surface_117122vtk = FindSource('input_surface_117122.vtk')

# find source
a114823_115017vtk = FindSource('114823_115017.vtk')

# find source
a114823_115219vtk = FindSource('114823_115219.vtk')

# find source
a114823_115825vtk = FindSource('114823_115825.vtk')

# find source
a114823_116221vtk = FindSource('114823_116221.vtk')

# find source
a114823_116524vtk = FindSource('114823_116524.vtk')

# find source
a114823_116726vtk = FindSource('114823_116726.vtk')

# find source
a114823_117122vtk = FindSource('114823_117122.vtk')

# find source
a115017_114823vtk = FindSource('115017_114823.vtk')

# find source
a117122_114823vtk = FindSource('117122_114823.vtk')
   
# find source
glyph11 = FindSource('Glyph11')

# find source
glyph3 = FindSource('Glyph3')

# find source
glyph12 = FindSource('Glyph12')

# find source
glyph13 = FindSource('Glyph13')

# find source
glyph9 = FindSource('Glyph9')

# find source
glyph1 = FindSource('Glyph1')

# find source
glyph0 = FindSource('Glyph0')

# find source
glyph10 = FindSource('Glyph10')

# find source
glyph2 = FindSource('Glyph2')

# find source
glyph4 = FindSource('Glyph4')

# find source
glyph7 = FindSource('Glyph7')

# find source
glyph6 = FindSource('Glyph6')

# find source
glyph5 = FindSource('Glyph5')

# find source
glyph8 = FindSource('Glyph8')

# get active view
renderView5 = GetActiveViewOrCreate('RenderView')

# show data in view
input_surface_115017vtkDisplay = Show(input_surface_115017vtk, renderView5, 'GeometryRepresentation')

# get color transfer function/color map for 'aparc'
aparcLUT = GetColorTransferFunction('aparc')

# trace defaults for the display properties.
input_surface_115017vtkDisplay.Representation = 'Surface'
input_surface_115017vtkDisplay.ColorArrayName = ['POINTS', 'aparc']
input_surface_115017vtkDisplay.LookupTable = aparcLUT
input_surface_115017vtkDisplay.SelectTCoordArray = 'None'
input_surface_115017vtkDisplay.SelectNormalArray = 'None'
input_surface_115017vtkDisplay.SelectTangentArray = 'None'
input_surface_115017vtkDisplay.OSPRayScaleArray = 'aparc'
input_surface_115017vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
input_surface_115017vtkDisplay.SelectOrientationVectors = 'None'
input_surface_115017vtkDisplay.ScaleFactor = 16.25130310058594
input_surface_115017vtkDisplay.SelectScaleArray = 'aparc'
input_surface_115017vtkDisplay.GlyphType = 'Arrow'
input_surface_115017vtkDisplay.GlyphTableIndexArray = 'aparc'
input_surface_115017vtkDisplay.GaussianRadius = 0.8125651550292969
input_surface_115017vtkDisplay.SetScaleArray = ['POINTS', 'aparc']
input_surface_115017vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
input_surface_115017vtkDisplay.OpacityArray = ['POINTS', 'aparc']
input_surface_115017vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
input_surface_115017vtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
input_surface_115017vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
input_surface_115017vtkDisplay.SelectInputVectors = [None, '']
input_surface_115017vtkDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
input_surface_115017vtkDisplay.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 35.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
input_surface_115017vtkDisplay.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 35.0, 1.0, 0.5, 0.0]

# show color bar/color legend
input_surface_115017vtkDisplay.SetScalarBarVisibility(renderView5, True)

# update the view to ensure updated data information
renderView5.Update()

# get opacity transfer function/opacity map for 'aparc'
aparcPWF = GetOpacityTransferFunction('aparc')

# get 2D transfer function for 'aparc'
aparcTF2D = GetTransferFunction2D('aparc')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1585, 789)

#-----------------------------------
# saving camera placements for views
 
# current camera placement for renderView5
renderView5.CameraPosition = [-28.639852388677443, 319.9704500525068, 313.60663196986286]
renderView5.CameraFocalPoint = [0.07288169860844552, 234.6419982910157, 11.2241649627684]
renderView5.CameraViewUp = [-0.12167888163684891, 0.9521844205822853, -0.28024824524693037]
renderView5.CameraParallelScale = 119.55477554582536

#--------------------------------------------
# uncomment the following to render all views
RenderAllViews()
Interact()
# alternatively, if you want to write images, you can use SaveScreenshot(...).                                                                                                                                                                                                                                             
.0