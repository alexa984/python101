class Subject(object):
    def __init__(self):
        self._observers = [] #contains references to all theobservers

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer: #not notify the observer, who is updating
                observer.update_viewer(self)

class Sensor(Subject):

    def __init__(self, name = ''):
        Subject.__init__(self)
        self._name = name
        self._temp = 0

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, temp):
        self._temp = temp
        # self.notify(self)


class TempViewer:
    def update_viewer(self, subject):
        print("Temperature Viewer: {} has Temperature {}".format(subject._name, subject._temp))

if __name__=='__main__':

    sensor1 = Sensor("Temp Sensor 1")
    v1 = TempViewer() #observer1
    v2 = TempViewer() #observer2    

    sensor1.attach(v1)
    sensor1.attach(v2)  

    sensor1.temp = 80
    sensor1.temp = 90
