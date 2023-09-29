from direct.showbase.ShowBase import ShowBase
from direct.showbase.Loader import Loader

class HelloWorld(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.scene = self.loader.loadModel("models/environment")
        self.scene.reparentTo(self.render)
        self.scene.setScale(1, 1, 1)
        self.scene.setPos(0, 0, 0)

app = HelloWorld()
app.run()