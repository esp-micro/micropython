BOARD_IDENTIFIER = "ESP32_S3_SPIRAM_OCT"

BOOT_PIN = const(0)


def lowpower():
    """Enter low power mode."""
    pass


def led_set(state):
    """Set the state of the LED on IO15"""
    pass


def toggle_led():
    """Toggle the LED on IO15"""
    pass


def get_bat_voltage():
    """Read and return the battery voltage from the fuel gauge."""
    pass


def get_state_of_charge():
    """Read and return the state of charge from the fuel gauge."""
    pass


def reset_battery_monitor():
    """Reset the battery monitor to default values."""
    pass


def quick_start_battery_monitor():
    """Perform a quick start to reset the SOC calculation in the chip."""
    pass


def set_pixel_power(state):
    """Enable or Disable power to the onboard NeoPixel to either show colour, or to reduce power for deep sleep."""
    pass


def rgb_color_wheel(wheel_pos):
    """Color wheel to allow for cycling through the rainbow of RGB colors."""
    pass
