BOARD_IDENTIFIER = "ESP32_S3_SPIRAM_OCT"

BOOT_PIN = const(0)

LED_PIN = 48


def lowpower():
    """Enter low power mode."""
    pass


def led_set(state):
    """Set the state of the LED"""
    import neopixel, machine
    if state:
        np = neopixel.NeoPixel(machine.Pin(LED_PIN), 1)
        np[0] = (255, 0, 0)
        np.write()
    else:
        np = neopixel.NeoPixel(machine.Pin(LED_PIN), 1)
        np[0] = (0, 0, 0)
        np.write()


def toggle_led():
    """Toggle the LED"""
    import neopixel, machine
    np = neopixel.NeoPixel(machine.Pin(LED_PIN), 1)
    if np[0] == (255, 0, 0):
        np[0] = (0, 0, 0)
    else:
        np[0] = (255, 0, 0)
    np.write()


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
