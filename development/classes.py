class Mario :

    _lives = 3
    _speed = 30.0

    def Test(self):
        print("Hallo")
        print("Speed is: ", self._speed)



instanceMario = Mario()
nogEenMario = Mario()

print( instanceMario._lives )
instanceMario.Test()
instanceMario._speed = 50.5

print("instanceMario snelheid:", instanceMario._speed)
print("nogEenMario snelheid:", nogEenMario._speed)
