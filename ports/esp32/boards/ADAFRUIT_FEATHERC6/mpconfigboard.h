#define MICROPY_HW_BOARD_NAME               "Adafruit Feather ESP32-C6 4MB Flash No PSRAM"
#define MICROPY_HW_MCU_NAME                 "ESP32C6"
#define MICROPY_PY_NETWORK_HOSTNAME_DEFAULT "ESP32C6"

#define MICROPY_HW_ENABLE_SDCARD            (0)
#define MICROPY_PY_MACHINE_I2S              (0)

// Enable UART REPL for modules that have an external USB-UART and don't use native USB.
#define MICROPY_HW_ENABLE_UART_REPL         (1)

#define MICROPY_HW_I2C0_SCL                 (18)
#define MICROPY_HW_I2C0_SDA                 (19)

#define MICROPY_HW_SPI1_MOSI                (22)
#define MICROPY_HW_SPI1_SCK                 (21)
#define MICROPY_HW_SPI1_MISO                (23)
