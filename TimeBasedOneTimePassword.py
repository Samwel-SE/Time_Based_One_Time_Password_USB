from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_RGB565


# uses the utotp code copied from: https://github.com/i-infra/utotp/blob/main/utotp.py
import utotp
import time

# Your Base32-encoded secret (e.g. from an authenticator app or QR code)
ExampleSecret = 'JBSWY3DPEHPK3PXP'
secret = ' ' # Put your real secret here.

# Generate the current 6-digit TOTP
code = utotp.totp(secret)


# Initialize display with the correct driver and pen type
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_RGB565)

# Get bounds (width, height)
width, height = display.get_bounds()

# Set a color and clear the screen
display.set_pen(0)  # Black
display.clear()

asciiDwightSchrute = "\n:)"

# Draw text
display.set_pen(255)  # White
display.text(code, 10, 10, 200, 4)
display.text(asciiDwightSchrute, 10, 10, 200, 4)

# Update the screen
display.update()   