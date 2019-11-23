_init_command = [0xAE, 0x20, 0x10, 0xB0,
                 0xC8, 0x00, 0x10, 0x40,
                 0x81, 0xFF, 0xA1, 0xA6,
                 0xA8, 0x3F, 0xA4, 0xD3,
                 0x00, 0xD5, 0xF0, 0xD9,
                 0x22, 0xDA, 0x12, 0xDB,
                 0x20, 0x8D, 0x14, 0xAF]

_on_command = [0x8D, 0x14, 0xAF]

_off_command = [0x8D, 0x10, 0xAE]

Font6x8 = [[0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
           [0x00, 0x00, 0x00, 0x2f, 0x00, 0x00],
           [0x00, 0x00, 0x07, 0x00, 0x07, 0x00],
           [0x00, 0x14, 0x7f, 0x14, 0x7f, 0x14],
           [0x00, 0x24, 0x2a, 0x7f, 0x2a, 0x12],
           [0x00, 0x62, 0x64, 0x08, 0x13, 0x23],
           [0x00, 0x36, 0x49, 0x55, 0x22, 0x50],
           [0x00, 0x00, 0x05, 0x03, 0x00, 0x00],
           [0x00, 0x00, 0x1c, 0x22, 0x41, 0x00],
           [0x00, 0x00, 0x41, 0x22, 0x1c, 0x00],
           [0x00, 0x14, 0x08, 0x3E, 0x08, 0x14],
           [0x00, 0x08, 0x08, 0x3E, 0x08, 0x08],
           [0x00, 0x00, 0x00, 0xA0, 0x60, 0x00],
           [0x00, 0x08, 0x08, 0x08, 0x08, 0x08],
           [0x00, 0x00, 0x60, 0x60, 0x00, 0x00],
           [0x00, 0x20, 0x10, 0x08, 0x04, 0x02],
           [0x00, 0x3E, 0x51, 0x49, 0x45, 0x3E],
           [0x00, 0x00, 0x42, 0x7F, 0x40, 0x00],
           [0x00, 0x42, 0x61, 0x51, 0x49, 0x46],
           [0x00, 0x21, 0x41, 0x45, 0x4B, 0x31],
           [0x00, 0x18, 0x14, 0x12, 0x7F, 0x10],
           [0x00, 0x27, 0x45, 0x45, 0x45, 0x39],
           [0x00, 0x3C, 0x4A, 0x49, 0x49, 0x30],
           [0x00, 0x01, 0x71, 0x09, 0x05, 0x03],
           [0x00, 0x36, 0x49, 0x49, 0x49, 0x36],
           [0x00, 0x06, 0x49, 0x49, 0x29, 0x1E],
           [0x00, 0x00, 0x36, 0x36, 0x00, 0x00],
           [0x00, 0x00, 0x56, 0x36, 0x00, 0x00],
           [0x00, 0x08, 0x14, 0x22, 0x41, 0x00],
           [0x00, 0x14, 0x14, 0x14, 0x14, 0x14],
           [0x00, 0x00, 0x41, 0x22, 0x14, 0x08],
           [0x00, 0x02, 0x01, 0x51, 0x09, 0x06],
           [0x00, 0x32, 0x49, 0x59, 0x51, 0x3E],
           [0x00, 0x7C, 0x12, 0x11, 0x12, 0x7C],
           [0x00, 0x7F, 0x49, 0x49, 0x49, 0x36],
           [0x00, 0x3E, 0x41, 0x41, 0x41, 0x22],
           [0x00, 0x7F, 0x41, 0x41, 0x22, 0x1C],
           [0x00, 0x7F, 0x49, 0x49, 0x49, 0x41],
           [0x00, 0x7F, 0x09, 0x09, 0x09, 0x01],
           [0x00, 0x3E, 0x41, 0x49, 0x49, 0x7A],
           [0x00, 0x7F, 0x08, 0x08, 0x08, 0x7F],
           [0x00, 0x00, 0x41, 0x7F, 0x41, 0x00],
           [0x00, 0x20, 0x40, 0x41, 0x3F, 0x01],
           [0x00, 0x7F, 0x08, 0x14, 0x22, 0x41],
           [0x00, 0x7F, 0x40, 0x40, 0x40, 0x40],
           [0x00, 0x7F, 0x02, 0x0C, 0x02, 0x7F],
           [0x00, 0x7F, 0x04, 0x08, 0x10, 0x7F],
           [0x00, 0x3E, 0x41, 0x41, 0x41, 0x3E],
           [0x00, 0x7F, 0x09, 0x09, 0x09, 0x06],
           [0x00, 0x3E, 0x41, 0x51, 0x21, 0x5E],
           [0x00, 0x7F, 0x09, 0x19, 0x29, 0x46],
           [0x00, 0x46, 0x49, 0x49, 0x49, 0x31],
           [0x00, 0x01, 0x01, 0x7F, 0x01, 0x01],
           [0x00, 0x3F, 0x40, 0x40, 0x40, 0x3F],
           [0x00, 0x1F, 0x20, 0x40, 0x20, 0x1F],
           [0x00, 0x3F, 0x40, 0x38, 0x40, 0x3F],
           [0x00, 0x63, 0x14, 0x08, 0x14, 0x63],
           [0x00, 0x07, 0x08, 0x70, 0x08, 0x07],
           [0x00, 0x61, 0x51, 0x49, 0x45, 0x43],
           [0x00, 0x00, 0x7F, 0x41, 0x41, 0x00],
           [0x00, 0x55, 0x2A, 0x55, 0x2A, 0x55],
           [0x00, 0x00, 0x41, 0x41, 0x7F, 0x00],
           [0x00, 0x04, 0x02, 0x01, 0x02, 0x04],
           [0x00, 0x40, 0x40, 0x40, 0x40, 0x40],
           [0x00, 0x00, 0x01, 0x02, 0x04, 0x00],
           [0x00, 0x20, 0x54, 0x54, 0x54, 0x78],
           [0x00, 0x7F, 0x48, 0x44, 0x44, 0x38],
           [0x00, 0x38, 0x44, 0x44, 0x44, 0x20],
           [0x00, 0x38, 0x44, 0x44, 0x48, 0x7F],
           [0x00, 0x38, 0x54, 0x54, 0x54, 0x18],
           [0x00, 0x08, 0x7E, 0x09, 0x01, 0x02],
           [0x00, 0x18, 0xA4, 0xA4, 0xA4, 0x7C],
           [0x00, 0x7F, 0x08, 0x04, 0x04, 0x78],
           [0x00, 0x00, 0x44, 0x7D, 0x40, 0x00],
           [0x00, 0x40, 0x80, 0x84, 0x7D, 0x00],
           [0x00, 0x7F, 0x10, 0x28, 0x44, 0x00],
           [0x00, 0x00, 0x41, 0x7F, 0x40, 0x00],
           [0x00, 0x7C, 0x04, 0x18, 0x04, 0x78],
           [0x00, 0x7C, 0x08, 0x04, 0x04, 0x78],
           [0x00, 0x38, 0x44, 0x44, 0x44, 0x38],
           [0x00, 0xFC, 0x24, 0x24, 0x24, 0x18],
           [0x00, 0x18, 0x24, 0x24, 0x18, 0xFC],
           [0x00, 0x7C, 0x08, 0x04, 0x04, 0x08],
           [0x00, 0x48, 0x54, 0x54, 0x54, 0x20],
           [0x00, 0x04, 0x3F, 0x44, 0x40, 0x20],
           [0x00, 0x3C, 0x40, 0x40, 0x20, 0x7C],
           [0x00, 0x1C, 0x20, 0x40, 0x20, 0x1C],
           [0x00, 0x3C, 0x40, 0x30, 0x40, 0x3C],
           [0x00, 0x44, 0x28, 0x10, 0x28, 0x44],
           [0x00, 0x1C, 0xA0, 0xA0, 0xA0, 0x7C],
           [0x00, 0x44, 0x64, 0x54, 0x4C, 0x44],
           [0x00, 0x00, 0x10, 0xFE, 0x82, 0x00],
           [0x00, 0x00, 0x00, 0xFF, 0x00, 0x00],
           [0x00, 0x82, 0xFE, 0x10, 0x00, 0x00],
           [0x02, 0x01, 0x01, 0x02, 0x02, 0x01]]


class Display:
    def __init__(self, i2c, ADDRESS = 0x78):
        self.i2c = i2c
        self.ADDR = ADDRESS
        
    def _set_pos(self, x, y):
        if x<128 and y<8:
            self.i2c.writeto_mem(self.ADDR, 0x00, 0xb0+y, mem_size = 8)
            self.i2c.writeto_mem(self.ADDR, 0x00, ((x&0xf0)>>4)|0x10, mem_size = 8)
            self.i2c.writeto_mem(self.ADDR, 0x00, x&0x0f, mem_size = 8)

    def Init(self):
            for i in _init_command:
                self.i2c.writeto_mem(self.ADDR, 0x00, i, mem_size = 8)

    def On(self):
        for i in _on_command:
            self.i2c.writeto_mem(self.ADDR, 0x00, i, mem_size = 8)

    def Off(self):
        for i in _off_command:
            self.i2c.writeto_mem(self.ADDR, 0x00, i, mem_size = 8)

    def Fill(self, data):
        for i in range(0,8):
            self.i2c.writeto_mem(self.ADDR, 0x00, 0xb0+i, mem_size = 8)
            self.i2c.writeto_mem(self.ADDR, 0x00, 0x10, mem_size = 8)
            self.i2c.writeto_mem(self.ADDR, 0x00, 0x01, mem_size = 8)
            for j in range(0,128):
                self.i2c.writeto_mem(self.ADDR, 0x40, data, mem_size = 8)
    def Text (self, x, y, STR):
        for i in range(len(STR)):
            Num = ord(STR[i])
            self._set_pos(x, y)
            for j in range(6):
                self.i2c.writeto_mem(self.ADDR, 0x40, Font6x8[c][j], mem_size = 8)
