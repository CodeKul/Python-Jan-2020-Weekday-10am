class Car:
    # color = ""
    # model = ""
    # make = ""
    def __init__(self, color, model, make):
        super().__init__()
        self.color = color
        self.model = model
        self.make = make
    
    def start(self):
        print("{} - {} is starting...".format(self.make, self.model))

    def stop(self):
        print("{} - {} is stopping...".format(self.make, self.model))

    def info(self):
        print("Model: ",self.model)
        print("Make: ",self.make)
        print("Color: ",self.color)

nano1 = Car("Red", "LXI", "Tata")
nano1.start()
nano1.stop()
nano1.info()
nano1.color = "Blue"
nano1.info()

nana2 = Car("Green", "VX", "Tata")
nano2.start()
nano2.stop()
nano2.info()
nano2.color = "Blue"
nano2.info()
