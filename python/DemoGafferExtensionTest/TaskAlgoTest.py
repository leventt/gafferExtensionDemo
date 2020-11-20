import unittest

import GafferTest

from DemoGafferExtension import TaskAlgo


class TaskAlgoTest( GafferTest.TestCase ) :

	def testGetTaskFileNames( self ) :

		# check if the function gracefully returns empty list
		self.assertEqual( TaskAlgo.getTaskFileNames( None ), [] )


if __name__ == "__main__":
	unittest.main()
