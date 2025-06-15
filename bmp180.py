import smbus
import time
import math

BMP180_ADDR = 0x77
bus = smbus.SMBus(1)

def read_word(addr):
    msb = bus.read_byte_data(BMP180_ADDR, addr)
    lsb = bus.read_byte_data(BMP180_ADDR, addr + 1)
    return (msb << 8) + lsb

def read_signed_word(addr):
    val = read_word(addr)
    if val > 32767:
        val -= 65536
    return val

# Calibration coefficients
AC1 = read_signed_word(0xAA)
AC2 = read_signed_word(0xAC)
AC3 = read_signed_word(0xAE)
AC4 = read_word(0xB0)
AC5 = read_word(0xB2)
AC6 = read_word(0xB4)
B1  = read_signed_word(0xB6)
B2  = read_signed_word(0xB8)
MB  = read_signed_word(0xBA)
MC  = read_signed_word(0xBC)
MD  = read_signed_word(0xBE)

def read_temperature():
    bus.write_byte_data(BMP180_ADDR, 0xF4, 0x2E)
    time.sleep(0.005)
    UT = read_word(0xF6)

    X1 = ((UT - AC6) * AC5) >> 15
    X2 = (MC << 11) // (X1 + MD)
    B5 = X1 + X2
    temp = ((B5 + 8) >> 4) / 10.0
    return temp, B5

def read_pressure(B5):
    oss = 0
    bus.write_byte_data(BMP180_ADDR, 0xF4, 0x34 + (oss << 6))
    time.sleep(0.005)

    msb = bus.read_byte_data(BMP180_ADDR, 0xF6)
    lsb = bus.read_byte_data(BMP180_ADDR, 0xF7)
    xlsb = bus.read_byte_data(BMP180_ADDR, 0xF8)
    UP = ((msb << 16) + (lsb << 8) + xlsb) >> (8 - oss)

    B6 = B5 - 4000
    X1 = (B2 * ((B6 * B6) >> 12)) >> 11
    X2 = (AC2 * B6) >> 11
    X3 = X1 + X2
    B3 = (((AC1 * 4 + X3) << oss) + 2) >> 2

    X1 = (AC3 * B6) >> 13
    X2 = (B1 * ((B6 * B6) >> 12)) >> 16
    X3 = ((X1 + X2) + 2) >> 2
    B4 = (AC4 * (X3 + 32768)) >> 15
    B7 = (UP - B3) * (50000 >> oss)

    if B7 < 0x80000000:
        p = (B7 * 2) // B4
    else:
        p = (B7 // B4) * 2

    X1 = (p >> 8) * (p >> 8)
    X1 = (X1 * 3038) >> 16
    X2 = (-7357 * p) >> 16
    p = p + ((X1 + X2 + 3791) >> 4)

    return p

def calculate_altitude(pressure_hpa, sea_level_pressure=1013.25):
    return 44330.0 * (1.0 - pow(pressure_hpa / sea_level_pressure, 1 / 5.255))

def get_readings():
    temperature, B5 = read_temperature()
    pressure_pa = read_pressure(B5)
    pressure_hpa = pressure_pa / 100.0
    altitude = calculate_altitude(pressure_hpa)

    return {
        "temperature": round(temperature, 2),
        "pressure": round(pressure_hpa, 2),
        "altitude": round(altitude, 2)
    }

# Optional: run standalone
if __name__ == "__main__":
    readings = get_readings()
    print("Temperature:", readings["temperature"], "°C")
    print("Pressure:", readings["pressure"], "hPa")
    print("Altitude:", readings["altitude"], "m")
