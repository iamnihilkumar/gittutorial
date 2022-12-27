class Volume:
    def get(self):
        self.r=float(input('Enter radius='))
        self.h=float(input('Enter height='))
class cone(Volume):
    def Volume(self):
        Volume.get(self)
        self.vc=0.3*3.14*(self.r**2)*self.h
class sphere(Volume):
    def volsph(self):
        Volume.get(self)
        self.vs=1.33*3.14*(self.r**3)
class Large(cone,sphere):
    def display(self):
        cone.Volume(self):
        sphere.volsphere