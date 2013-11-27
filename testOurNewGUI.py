#!/usr/bin/python
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------------------
# testOurNewGUI.py
#
# MVRL Techno-Cabal 2013-11-07
#
# AUTHOR NAME
# AUTHOR@EMAIL.ADDRESS
# --------------------------------------------------------------------------------------------------


## STANDARD IMPORTS
# --------------------------------------------------------------------------------------------------
import sys; # for python system
import math;
# --------------------------------------------------------------------------------------------------


## GUI IMPORTS
# --------------------------------------------------------------------------------------------------
from PySide import QtCore, QtGui;
# --------------------------------------------------------------------------------------------------


## PLOTTING IMPORTS
# --------------------------------------------------------------------------------------------------
import matplotlib as mpl
mpl.use( 'Qt4Agg' );
mpl.rcParams['backend.qt4'] = 'PySide';
mpl.rcParams['figure.autolayout'] = True;

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as MatplotlibFigureCanvasQTAgg;
from matplotlib.figure import Figure as MatplotlibFigure;
# --------------------------------------------------------------------------------------------------





## PLOTTING CANVAS WIDGET (also inherits from FigureCanvasQTAgg)
# --------------------------------------------------------------------------------------------------
class MyPlotWidget( MatplotlibFigureCanvasQTAgg ):

	## PERFORMED AT INSTANTIATION
	# ----------------------------------------------------------------------------------------------
	def __init__( self, plotFigureDPI= 72, myTopWindowReference= None ):
		
		super( MyPlotWidget, self ).__init__( MatplotlibFigure() ); # initialize the parent. 
																	# MatplotlibFigure() creates an oject

		self.myTopWindowReference = myTopWindowReference;
		

		# DEFINE FIGURE DEFAULTS
		plotFigureSizeInchesHW = [ 11, 8.5 ];
		
		plotFigureBackgroundColor = [ (237.0 / 255.0),
									  (237.0 / 255.0),
									  (237.0 / 255.0) ];

		plotFigureEdgeColor = [ (0.0 / 255.0),
								(0.0 / 255.0),
								(0.0 / 255.0) ];

		# DEFINE FIGURE (SIZE IN INCHES)
		self.figure = MatplotlibFigure( figsize=      plotFigureSizeInchesHW,
										dpi=          plotFigureDPI,
										facecolor=    plotFigureBackgroundColor,
										edgecolor=    plotFigureEdgeColor );


		# DEFINE A CANVAS
		self.canvas = MatplotlibFigureCanvasQTAgg( self.figure ); 

		self.clearPlot( );
		
		return None;
	#fed -------------------------------------------------------------------------------------------


	## UPDATE OUR PLOT BY PLOTTING THE PATH FROM CALCULATIONS
	# ----------------------------------------------------------------------------------------------
	def updatePlot( self ):
		self.axes.clear();

		self.axes.grid( 'on', color= ( 0.5, 0.5, 0.5, 0.05 ), linestyle= '-.', linewidth= 0.5 );
		
		theta = self.myTopWindowReference.centralWidget.phaseShiftSlider.value();

		numPointsToPlot = 100;

		ourSinusoid, ourTime = self.plotPathCalculationFunction( anglePhaseShift= theta,
													numSamples= numPointsToPlot );

		self.axes.plot( ourTime, ourSinusoid,
			marker='.',
			color= '#00FF00' );

		self.axes.set_xlim( [ 0,1] )
		self.axes.set_ylim([-1,1])

		# Refresh the plot
		self.fuckYouNokia();

		return None;
	#fed -------------------------------------------------------------------------------------------


	## CALCULATE THE PATH TO PLOT
	# ----------------------------------------------------------------------------------------------
	def plotPathCalculationFunction( self, anglePhaseShift, numSamples ):

		sinusoidData = [];
		timeData =[];

		for i in range( 0, numSamples ):

			phaseShiftRadians = math.radians( anglePhaseShift );

			timeData.append(float(i) / float(numSamples -1 ))

			sinusoidData.append( math.sin(timeData[-1] * 2.0*math.pi +
											phaseShiftRadians ) );

		return ( sinusoidData, timeData );
	#fed -------------------------------------------------------------------------------------------


	## CLEAR AND THEN SETUP THE BASIC PLOT CONDITIONS
	# ----------------------------------------------------------------------------------------------
	def clearPlot( self ):

		self.figure.clear();

		self.axes = self.figure.add_subplot( 1, 1, 1 );

		self.axes.grid( 'on', color= ( 0.5, 0.5, 0.5, 0.05 ), linestyle= '-.', linewidth= 0.5 );

		####
		#### CODE GOES HERE
		####
		
		# Set the plot titles
		self.axes.set_title( "PLOT TITLE GOES HERE", fontsize= 20 );
		self.axes.set_xlabel( "X-AXIS TITLE GOES HERE", fontsize= 20 );
		self.axes.set_ylabel( "Y-AXIS TITLE GOES HERE", fontsize= 20 );

		# Set the window status message
		ourDefaultMessage = self.myTopWindowReference.defaultStatusMessage;
		self.myTopWindowReference.statusBar().showMessage( ourDefaultMessage );

		# Refresh Plot
		self.fuckYouNokia( );

		return None;
	#fed -------------------------------------------------------------------------------------------


	
	## REFRESH THE PLOT
	# ----------------------------------------------------------------------------------------------
	def fuckYouNokia( self ):
		self.draw();
		QtCore.QCoreApplication.processEvents( );

		# windowSize = self.myTopWindowReference.size();
		# self.myTopWindowReference.resize( windowSize.width()-1, windowSize.height() );
		# self.myTopWindowReference.resize( windowSize.width(), windowSize.height() );

		return None;
	#fed -------------------------------------------------------------------------------------------

#ssalc ---------------------------------------------------------------------------------------------




## CENTRAL WIDGET IN MAIN WINDOW
# --------------------------------------------------------------------------------------------------
class MyCentralWidget( QtGui.QDialog ):
	
	## PERFORMED AT INSTANTIATION
	# ----------------------------------------------------------------------------------------------
	def __init__( self, myTopWindowReference= None ):

		super( MyCentralWidget, self ).__init__( None );

		self.myTopWindowReference = myTopWindowReference;

		

		## OTHER WIDGETS
		# ------------------------------------------------------------
		self.phaseShiftSlider = QtGui.QSlider(QtCore.Qt.Horizontal);
		self.phaseShiftSlider.setRange(0,90);
		self.phaseShiftSlider.setValue(0);
		
		
		self.ourPathPlotInstance = MyPlotWidget( myTopWindowReference= self.myTopWindowReference );
		self.phaseShiftSlider.valueChanged.connect( self.ourPathPlotInstance.updatePlot );
		# ------------------------------------------------------------------------------------------
		## BUTTONS
		# ------------------------------------------------------------------------------------------
		self.buttClear = QtGui.QPushButton( "Clear Plot" );
		self.buttClear.pressed.connect( self.ourPathPlotInstance.clearPlot );

		self.buttPlot = QtGui.QPushButton( "Plot Sinusoid" );
		self.buttPlot.pressed.connect( self.ourPathPlotInstance.updatePlot );
		

		self.buttClose = QtGui.QPushButton( "Close" );
		self.buttClose.pressed.connect( myTopWindowReference.close );
		# ------------------------------------------------------------------------------------------


		## LAYOUTS
		# ------------------------------------------------------------------------------------------
		mainLayout = QtGui.QVBoxLayout( );
		
		####
		#### CODE GOES HERE
		####
		

		## BUTTON LAYOUT GROUP
		buttLayout = QtGui.QHBoxLayout();
		buttLayout.addWidget( self.buttClear );
		buttLayout.addWidget( self.buttPlot );
		buttLayout.addWidget( self.buttClose );




		# SET THE FINAL WINDOW LAYOUT
		mainLayout.addWidget( self.ourPathPlotInstance );
		####
		mainLayout.addWidget( self.phaseShiftSlider )
		####
		mainLayout.addLayout( buttLayout );
		
		self.setLayout( mainLayout );
		# ------------------------------------------------------------------------------------------

		
		return None
	#fed -------------------------------------------------------------------------------------------

#ssalc ---------------------------------------------------------------------------------------------




## MAIN WINDOW OF APPLICATION
# --------------------------------------------------------------------------------------------------
class MyApplicationWindow( QtGui.QMainWindow ): # QMainWindow is a class from QtGui. It is inherited
	
	## PERFORMED AT INSTANTIATION
	# ----------------------------------------------------------------------------------------------
	def __init__( self, myTopWindowReference= None ):
		
		super( MyApplicationWindow, self ).__init__( None ); # initialize everything that is already created

		self.defaultStatusMessage = "Let's plot some curves...";

		self.centralWidget = MyCentralWidget( myTopWindowReference= self );

		self.setCentralWidget( self.centralWidget );

		self.statusBar().showMessage( self.defaultStatusMessage );

		return None;
	#fed -------------------------------------------------------------------------------------------


#ssalc ---------------------------------------------------------------------------------------------





## MAIN
# --------------------------------------------------------------------------------------------------
MyApplication = QtGui.QApplication( sys.argv );

myWindowInstance = MyApplicationWindow();

myWindowInstance.show();
myWindowInstance.raise_();	    

sys.exit( MyApplication.exec_() );
# --------------------------------------------------------------------------------------------------
