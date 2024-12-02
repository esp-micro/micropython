from machine import ADC, Pin

DEBUG = True  # Set to False to disable logging


def log(message):
    """Logs a message if debugging is enabled."""
    if DEBUG:
        print(message)


# LED
LED = const(15)

VBAT_SENSE = const(0)


def get_bat_voltage():
    """
    Returns the current battery voltage. If no battery is connected, returns 4.2V which is the charge voltage
    This is an approximation only, but useful to detect if the charge state of the battery is getting low.
    """
    log(" :: reading battery voltage")
    adc = ADC(Pin(VBAT_SENSE))  # Assign the ADC pin to read
    # Max voltage on ADC input will be 4.2V divided by R15 (1000K) & R16 (1000K), 4.2 / (1000 + 1000) * 1000 = 2.1V
    adc.atten(ADC.ATTN_11DB)  # 11dB attenuation (150mV - 2450mV) for a max of 2.1V
    # Use read_uv() to get ADC reading as this will use the on-chip calibration data
    measuredvbat = adc.read_uv() / 1000  # Read micovolts and convert to millivolts
    measuredvbat *= 2  # Multiply by ratio of battery voltage to ADC pin voltage: 4.2 / 2.1 = 2
    measuredvbat = int(round(measuredvbat, 0))  # Round to nearest integer
    log(f" :: battery voltage: {measuredvbat} mV")
    return measuredvbat


def led_set(state):
    """Set the state of the LED on IO15"""
    l = Pin(LED, Pin.OUT)
    l.value(state)


def toggle_led():
    """Toggle the LED on IO15"""
    l = Pin(LED, Pin.OUT)
    l.value(not l.value())


def lowpower():
    """Enter low power mode."""
    led_set(0)
    pass
