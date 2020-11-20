import unittest

import Gaffer
import GafferTest
import GafferScene

from DemoGafferExtension import TaskAlgo


class TaskAlgoTest( GafferTest.TestCase ) :

	def testGetTaskFileNames( self ) :

		# check if the function gracefully returns empty list
		self.assertEqual( TaskAlgo.getTaskFileNames( None ), [] )

		scriptNode = Gaffer.ScriptNode()
		scriptNode["reader"] = GafferScene.SceneReader()
		scriptNode["reader"]["fileName"].setValue( "/some/scene/path" )
		scriptNode["camera"] = GafferScene.Camera()
		scriptNode["group"] = GafferScene.Group()
		scriptNode["group"]["in"][-1].setInput( scriptNode["reader"]["out"] )
		scriptNode["group"]["in"][-1].setInput( scriptNode["camera"]["out"] )
		scriptNode["render"] = GafferScene.OpenGLRender()
		scriptNode["render"]["fileName"].setValue( "/some/output/path" )
		scriptNode["render"]["in"].setInput( scriptNode["group"]["out"] )

		self.assertEqual(
			TaskAlgo.getTaskFileNames( scriptNode["render"]["task"] ),
			['/some/scene/path', '/some/output/path']
		)


if __name__ == "__main__":
	unittest.main()
