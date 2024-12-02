import asyncio
import network
import sys
import machine
from board import led_set  # type: ignore


def get_unique_id() -> str:
    wlan = network.WLAN(network.STA_IF)
    return wlan.config("mac").hex()


RESET_CAUSE_MAP = {
    machine.HARD_RESET: "HARD_RESET",
    machine.SOFT_RESET: "SOFT_RESET",
    machine.PWRON_RESET: "PWRON_RESET",
    machine.WDT_RESET: "WDT_RESET",
    machine.DEEPSLEEP_RESET: "DEEPSLEEP_RESET",
}

if sys.platform == "esp32":
    from machine import reset_cause, wake_reason
    WAKE_REASON_MAP = {
        # ESP32
        0: "RESET",
        machine.ULP_WAKE: "ULP_WAKE",
        machine.PIN_WAKE: "PIN_WAKE",
        machine.TOUCHPAD_WAKE: "TOUCHPAD_WAKE",
        machine.TIMER_WAKE: "TIMER_WAKE",
        machine.EXT0_WAKE: "EXT0_WAKE",
        machine.EXT1_WAKE: "EXT1_WAKE",
    }
elif sys.platform == "esp8266":
    from machine import reset_cause
    WAKE_REASON_MAP = {}

    def wake_reason():
        return "DEEPSLEEP_WAKE"
else:  # vscode stubs
    from _typeshed import Incomplete
    def reset_cause() -> Incomplete: ...
    def wake_reason() -> Incomplete: ...
    WAKE_REASON_MAP = {}


def get_reset_cause():
    return RESET_CAUSE_MAP.get(reset_cause(), "UNKNOWN")


def get_wake_reason():
    reason = wake_reason()
    if reason == 0:
        return get_reset_cause()
    else:
        return WAKE_REASON_MAP.get(reason, "UNKNOWN")


async def _pulse_led(interval):
    s = True
    while True:
        await asyncio.sleep_ms(interval)
        led_set(s)
        s = not s


async def pulse_led_task(interval):
    task = asyncio.create_task(_pulse_led(interval))
    return task


def led_on():
    led_set(True)


def led_off():
    led_set(False)
