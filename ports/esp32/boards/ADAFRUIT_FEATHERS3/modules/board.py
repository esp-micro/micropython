import feathers3

BOARD_IDENTIFIER = "ADA_FEATHER_S3" # Adafruit Feather S3

I2C_SCL = feathers3.I2C_SCL
I2C_SDA = feathers3.I2C_SDA
I2C_PWR = feathers3.I2C_PWR

RGB_DATA = feathers3.RGB_DATA
RGB_PWR = feathers3.RGB_PWR

LED = feathers3.LED

def get_bat_voltage():
    """Read and return the battery voltage from the fuel gauge."""
    return feathers3.get_bat_voltage()


def get_state_of_charge():
    """Read and return the state of charge from the fuel gauge."""
    return feathers3.get_state_of_charge()


def reset_battery_monitor():
    """Reset the battery monitor to default values."""
    feathers3.reset_battery_monitor()


def quick_start_battery_monitor():
    """Perform a quick start to reset the SOC calculation in the chip."""
    feathers3.quick_start_battery_monitor()


def set_pixel_power(state):
    """Enable or Disable power to the onboard NeoPixel to either show colour, or to reduce power for deep sleep."""
    feathers3.set_pixel_power(state)


def rgb_color_wheel(wheel_pos):
    """Color wheel to allow for cycling through the rainbow of RGB colors."""
    return feathers3.rgb_color_wheel(wheel_pos)


def led_set(state):
    """Set the state of the LED on IO13"""
    feathers3.led_set(state)


def toggle_led():
    """Toggle the LED on IO13"""
    feathers3.toggle_led()


def lowpower():
    """Enter low power mode."""
    feathers3.lowpower()
