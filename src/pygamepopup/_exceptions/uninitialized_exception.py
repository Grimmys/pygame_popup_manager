class UnintializedException(Exception):
    def __init__(self):
        self.message = "pygamepopup.init() has to be called before any other interaction with pygamepopup"
        super().__init__(self.message)
