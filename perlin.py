from PIL import Image
import math
import random

class point:
    x = y = float ()
    def createPoint (x, y):
        p = point ()
        p.x = x
        p.y = y
        return p
    def createVector (x1, y1, x2, y2):
        p = point ()
        p.x = x2 - x1
        p.y = y2 - y1
        return p
    def dotProduct (a, b):
        return (a.x * b.x) + (a.y * b.y)

    def normalized (p):
        t = math.sqrt (p.x * p.x + p.y * p.y)
        p.x /= t
        p.y /= t
        return p

class Perlin:
    def fade (self, t):
        return ((3 * t * t) - (2 * t * t * t))
    def lerp (self, a, b, x):
        return a + x * (b - a);

    V = []
    P = []
    def __init__ (self):
        for i in range (256):
            self.P.append (i)
            self.V.append (point.createPoint (float (random.randrange (-100, 100)), float(random.randrange (-100, 100))))
            self.V[i] = point.normalized (self.V [i])
        for i in range (256):
            t = random.randrange (0, 256)
            temp = self.P [i]
            self.P [i] = self.P [t]
            self.P [t] = temp
        for i in range (256):
            self.P.append (0)
    # end __init__

    def getValue (self, x, y):
        x0 = int (x)
        y0 = int (y)
        x1 = x0 + 1
        y1 = y0 + 1

        rx0 = x - x0
        rx1 = rx0 - 1
        ry0 = y - y0
        ry1 = ry0 - 1

        v = self.fade (x - x0)
        u = self.fade (y - y0)

        i = x0
        j = x1

        A00 = self.P[i + self.P [y0]]
        A10 = self.P[j + self.P [y0]]
        A01 = self.P[i + self.P [y1]]
        A11 = self.P[j + self.P [y1]]

        q1 = point.dotProduct (point.createPoint (rx0, ry0), self.V [A00])
        q2 = point.dotProduct (point.createPoint (rx1, ry0), self.V [A10])
        w = self.lerp (q1, q2, v)
        q3 = point.dotProduct (point.createPoint (rx0, ry1), self.V [A01])
        q4 = point.dotProduct (point.createPoint (rx1, ry1), self.V [A11])
        e = self.lerp (q3, q4, v)
        value = self.lerp (w, e, u)
        return (value + 1) / 2
    #end getValue
#end Perlin Class
