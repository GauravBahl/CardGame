class SetCard:

    def __init__(self, color=None, shape=None, shade=None, num_shape=None):
        self.color = color
        self.shape = shape
        self.shade = shade
        self.num_shape = num_shape
        self.available = True
    
    def show(self):
        print('Card of {} , {} , {} , {}, {}'.format(self.color, 
            self.shape, self.shade, self.num_shape, self.available))

    def isAvailable(self):
        return self.available

    def markAvailable(self):
        self.available = True
    
    def markUnAvailable(self):
        self.available = False
