from micropython import const
from machine import Pin, SoftI2C
from max17048 import MAX17048

DEBUG = True  # Set to False to disable logging

def log(message):
    """Logs a message if debugging is enabled."""
    if DEBUG:
        print(message)

# I2C
I2C_SCL = const(4)
I2C_SDA = const(3)
I2C_PWR = const(7)

# NeoPixel
RGB_DATA = const(33)
RGB_PWR = const(21)

# LED
LED = const(13)

# Initialize I2C bus
i2c = SoftI2C(scl=I2C_SCL, sda=I2C_SDA)

# Create an instance of the MAX17048 class
max17048 = MAX17048(i2c)


def set_i2c_power(state):
    """Enable or Disable power to the onboard MAX17048 fuel gauge."""
    log(f" :: setting i2c power to {'ON' if state else 'OFF'}")
    Pin(I2C_PWR, Pin.OUT).value(state)
    log(f" :: i2c power state is now {'ON' if get_i2c_power() else 'OFF'}")


def get_i2c_power():
    """Get the current state of the i2c power pin."""
    return Pin(I2C_PWR, Pin.OUT).value()


def get_bat_voltage():
    """Read and return the battery voltage from the fuel gauge."""
    log(" :: reading battery voltage")
    current_i2c_power = get_i2c_power()

    if not current_i2c_power:
        set_i2c_power(True)

    try:
        voltage = max17048.cell_voltage
        log(f" :: battery voltage read: {voltage} V")
        return voltage
    except:
        log(f"Error reading battery voltage: {e}")
        return None
    finally:
        if not current_i2c_power:
            set_i2c_power(False)


def get_state_of_charge():
    """Read and return the state of charge from the fuel gauge."""
    log(" :: reading state of charge")
    current_i2c_power = get_i2c_power()

    if not current_i2c_power:
        set_i2c_power(True)

    try:
        soc = max17048.state_of_charge
        log(f" :: state of charge read: {soc} %")
        return soc
    except Exception as e:
        log(f"Error reading state of charge: {e}")
        return None
    finally:
        if not current_i2c_power:
            set_i2c_power(False)


def reset_battery_monitor():
    """Reset the battery monitor to default values."""
    log(" :: resetting battery monitor")
    current_i2c_power = get_i2c_power()

    if not current_i2c_power:
        set_i2c_power(True)

    try:
        max17048.reset()
        log(" :: battery monitor reset")
    except Exception as e:
        log(f"Error resetting battery monitor: {e}")
    finally:
        if not current_i2c_power:
            set_i2c_power(False)


def quick_start_battery_monitor():
    """Perform a quick start to reset the SOC calculation in the chip."""
    log(" :: performing quick start on battery monitor")
    try:
        max17048.quick_start()
        log(" :: quick start successful")
    except Exception as e:
        log(f"Error performing quick start: {e}")


def set_pixel_power(state):
    """Enable or Disable power to the onboard NeoPixel to either show colour, or to reduce power for deep sleep."""
    log(f" :: setting pixel power to {'ON' if state else 'OFF'}")
    Pin(RGB_PWR, Pin.OUT).value(state)
    log(f" :: pixel power state is now {'ON' if get_pixel_power() else 'OFF'}")


def get_pixel_power():
    """Get the current state of the pixel power pin."""
    return Pin(RGB_PWR, Pin.OUT).value()


# NeoPixel rainbow colour wheel
def rgb_color_wheel(wheel_pos):
    """Color wheel to allow for cycling through the rainbow of RGB colors."""
    wheel_pos = wheel_pos % 255

    if wheel_pos < 85:
        return 255 - wheel_pos * 3, 0, wheel_pos * 3
    elif wheel_pos < 170:
        wheel_pos -= 85
        return 0, wheel_pos * 3, 255 - wheel_pos * 3
    else:
        wheel_pos -= 170
        return wheel_pos * 3, 255 - wheel_pos * 3, 0


# LED control
def led_set(state):
    """Set the state of the BLUE LED on IO13"""
    l = Pin(LED, Pin.OUT)
    l.value(state)


def toggle_led(state):
    """Toggle the BLUE LED on IO13"""
    l = Pin(LED, Pin.OUT)
    l.value(not l.value())


def lowpower():
    log(" :: entering low power mode")
    set_i2c_power(0)
    set_pixel_power(0)
    led_set(0)
    # Additional actions to reduce power consumption
    log(" :: low power mode set")
