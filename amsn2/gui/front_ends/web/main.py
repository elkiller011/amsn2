
from amsn2.gui import base
from bend import Backend
import os

class aMSNMainWindow(base.aMSNMainWindow,Backend):
    def __init__(self, amsn_core):
        try:
            os.remove("/tmp/test.in")
        except:
            pass
        try:
            os.remove("/tmp/test.out")
        except:
            pass
        open("/tmp/test.in","w").close()
        open("/tmp/test.out","w").close()
        os.chmod("/tmp/test.in",0666)
        os.chmod("/tmp/test.out",0666)
        Backend.__init__(self,"/tmp/test.in","/tmp/test.out")
        self._amsn_core = amsn_core
        self._amsn_core.timerAdd(1,self.checkEvent)
 
    def show(self):
        self.send("showMainWindow",[])
        self._amsn_core.idlerAdd(self.__on_show)

    def hide(self):
        self.send("hideMainWindow",[])
        pass
    
    def setTitle(self,title):
        self.send("setMainWindowTitle",[title])
        pass

    def setMenu(self,menu):
        print "aMSNMainWindow.setMenu"
        pass

    def __on_show(self):
        self._amsn_core.mainWindowShown()
