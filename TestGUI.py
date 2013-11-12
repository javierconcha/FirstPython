## IMPORTS

# -----------------------------------------------------------
import sys;

from PySide import QtCore, QtGui
# -----------------------------------------------------------


# -----------------------------------------------------------

class MyCentralWidget( QtGui.QDialog ):


	def __init__(self, myWindowReference= None, parent= None):

		super( MyCentralWidget, self ).__init__(parent);

		mainLayout = QtGui.QVBoxLayout();

		self.buttClose = QtGui.QPushButton( "Close");
		# self.buttClose.pressed.connect( QtCore.QCoreApplication.instance().quit );
		self.buttClose.pressed.connect( myWindowReference.close );

		# self.buttName = QtGui.QPushButton("Javier")

		self.mySlider = QtGui.QSlider(QtCore.Qt.Horizontal);

		mainLayout.addWidget( self.mySlider );
		mainLayout.addWidget( self.buttClose )

		self.setLayout( mainLayout );
	#fed
#ssalc


## MAINWINDOW
# -----------------------------------------------------------
class MyMainWindow( QtGui.QMainWindow ):
	'''

	'''
	# windName = "My Window";

	def __init__( self, myWindowReference= None, parent= None ):

		super( MyMainWindow, self ).__init__( parent );
	

		self.centralWidget = MyCentralWidget( myWindowReference= self );

		self.setCentralWidget( self.centralWidget );

		self.statusBar().showMessage( 'Application Ready...');

		return None;

		# self.myVerticalSlider = QtGui.QSlider()
	#fed
#ssalc	


## MAIN
# -----------------------------------------------------------
MyQtApp = QtGui.QApplication(sys.argv );

myWindowPane = MyMainWindow( );

myWindowPane.show();
myWindowPane.raise_();


sys.exit( MyQtApp.exec_() );
# -----------------------------------------------------------