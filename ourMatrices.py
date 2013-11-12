
class ourMatrix():

	def __init__(self, listOfElements, listOfSizes=None ):

		self.matrixData = listOfElements;

		if (listOfSizes is None):

			self.matrixSize = listOfSizes;

		#fi

		return None;

	#fed

	def matrixAdd( self, secondMatrix ):

		if ((secondMatrix.matrixSize != self.matrixSize) or (len( secondMatrix.matrixData) != len(self.matrixData) )):

			raise NameError ( "Matrices are nothe same size" )


		dataLength = len( self.matrixData);

		addedMatrices = [];

		for i in range (0, dataLength,1):
			addedMatrices.append(self.matrixData[i] + secondMatrix.matrixData[i]);

		return addedMatrices;

	#fed