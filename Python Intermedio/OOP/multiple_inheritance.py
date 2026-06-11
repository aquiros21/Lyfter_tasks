class Phone:
    def make_call(self):
        print("I can make phone calls")


class Camera:
    def take_picture(self):
        print("I can take pictures")


class Smartphone(Phone,Camera):
    pass


iphone = Smartphone()
iphone.make_call()
iphone.take_picture()

