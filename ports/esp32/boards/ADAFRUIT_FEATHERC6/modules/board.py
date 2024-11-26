import featherc6

BOARD_IDENTIFIER = "ADA_FEATHER_C6" # Adafruit Feather C6

I2C_SCL = featherc6.I2C_SCL
I2C_SDA = featherc6.I2C_SDA
I2C_PWR = featherc6.I2C_PWR

RGB_DATA = featherc6.RGB_DATA
RGB_PWR = featherc6.RGB_PWR

LED = featherc6.LED

def get_bat_voltage():
    """Read and return the battery voltage from the fuel gauge."""
    return featherc6.get_bat_voltage()


def get_state_of_charge():
    """Read and return the state of charge from the fuel gauge."""
    return featherc6.get_state_of_charge()


def reset_battery_monitor():
    """Reset the battery monitor to default values."""
    featherc6.reset_battery_monitor()


def quick_start_battery_monitor():
    """Perform a quick start to reset the SOC calculation in the chip."""
    featherc6.quick_start_battery_monitor()


def set_pixel_power(state):
    """Enable or Disable power to the onboard NeoPixel to either show colour, or to reduce power for deep sleep."""
    featherc6.set_pixel_power(state)


def rgb_color_wheel(wheel_pos):
    """Color wheel to allow for cycling through the rainbow of RGB colors."""
    return featherc6.rgb_color_wheel(wheel_pos)


def led_set(state):
    """Set the state of the LED on IO15"""
    featherc6.led_set(state)


def toggle_led():
    """Toggle the LED on IO15"""
    featherc6.toggle_led()


def lowpower():
    """Enter low power mode."""
    featherc6.lowpower()
