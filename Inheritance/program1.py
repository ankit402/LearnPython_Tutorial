

class car:
    def __init__(self, windows, doors, enginetype):
            self._window = windows
            self._doors = doors
            self._enginetype = enginetype

    def drive(self):
        print(f'the person will drive the {self._enginetype}')


class Tesla(car):
    def __init__(self, windows, doors, enginetype, isdriving):
        super().__init__(windows,doors,enginetype)
        self._isdriving = isdriving

    def selfdriving(self):
        if self._isdriving:
            print(f"tesla supports automatic driving")
        else:
            print(f"tesla does not support automatic driving")


t1=Tesla(4,5 ,"Petrol", True)
t1.drive()
t1.selfdriving()







