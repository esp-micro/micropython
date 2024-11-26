import firebeetlec6

BOARD_IDENTIFIER = "FIREBEETLE_C6"  # FireBeetle C6

BOOT_PIN = const(9)


def lowpower():
    """Enter low power mode."""
    firebeetlec6.lowpower()


def led_set(state):
    """Set the state of the LED on IO15"""
    firebeetlec6.led_set(state)


def toggle_led():
    """Toggle the LED on IO15"""
    firebeetlec6.toggle_led()


def get_bat_voltage():
    """Read and return the battery voltage from the fuel gauge."""
    return firebeetlec6.get_bat_voltage()


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
