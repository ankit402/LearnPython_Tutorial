class chip:
    def __init__(self,provider):
        self._provider = provider

    def supportedpadding(self):
        print("by Default it is not padding")

    def supporttedDrivekey(self):
        print("by Default it is none drive case")

class DriveAuth:
    def __init__(self,chipname):
        self.chipname = chipname

class Gemalto(chip,DriveAuth):
    def __init__(self,provider, chipname):
        chip.__init__(self,provider)
        DriveAuth.__init__(self, chipname)

    def supportedPadding(self):
        print("Supported Padding: FFFFFF")

    def supporttedDrivekey(self):
        print("Supported drive key auth")

c1 = Gemalto("Thales", "R12")

# Call methods
c1.supportedPadding()
c1.supporttedDrivekey()