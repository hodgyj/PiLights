import board
import adafruit_ws2801

class WS2801:
    def __init__(self, numleds, brightness, odata=board.MOSI, oclock=board.SCLK):
        self.leds = adafruit_ws2801.WS2801(oclock, odata, numleds, brightness=brightness, auto_write=False)
        self.values = []
        self.brightness = brightness
        self.numleds = numleds
    
    def set_leds(self, vals):
        if len(vals) == 1:
            val = vals[0]
            vals = []
            for i in range(0, self.numleds):
                vals.append(val)

        if len(vals) == self.numleds:
            for i in range(self.numleds):
                self.leds[i] = (
                    int(vals[i][0] * self.brightness),
                    int(vals[i][1] * self.brightness),
                    int(vals[i][2] * self.brightness)
                )
            self.values = vals
        else:
            print("Incorrect vals length")
            return
        self.leds.show()

    def set_brightness(self, brightness):
        if brightness > 1.0:
            brightness = 1.0
        elif brightness < 0.0:
            brightness = 0.0

        self.brightness = brightness

        self.set_leds(self.values)



