from PIL import Image
import mss



output_filename = 'Desktop\screenshot.png'

with mss.mss() as mss_instance:
    monitor_2 = mss_instance.monitors[2]
    screenshot = mss_instance.grab(monitor_2)

    img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
    img.save(output_filename, "PNG")
