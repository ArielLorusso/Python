
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Define constants
width = 960
height = 960
MAX_ITERS = 100
min_x = -2.0
max_x = 0.6
min_y = -1.5
max_y = 1.5

# Compute the Mandelbrot fractal
def mandelbrot_kernel(c):       # SINGLE PIXEL
    z = c
    for i in range(MAX_ITERS):
        z = z * z + c
        if abs(z) > 2:
            return i
    return MAX_ITERS            # how manty steps

def compute_mandelbrot():           # WHILE IMAGE
    mandelbrot = np.zeros((height, width), dtype=np.float64)

    dx = (max_x - min_x) / width
    dy = (max_y - min_y) / height

    for row in range(height):       
        for col in range(width):
            x = min_x + col * dx    # x = real
            y = min_y + row * dy    # y = imag
            c = complex(x, y)       
            mandelbrot[row, col] = mandelbrot_kernel(c)

    return mandelbrot

# Display the Mandelbrot fractal
def show_plot(tensor):
    scale = 10
    dpi = 64

    light = colors.LightSource(315, 10, 0, 1, 1, 0)
    image = light.shade(tensor, plt.cm.hot, colors.PowerNorm(0.3), "hsv", 0, 0, 1.5)

    plt.figure(1, figsize=(scale, scale * height // width), dpi=dpi)
    plt.imshow(image)
    plt.axis("off")
    plt.show()

# Compute and display the Mandelbrot fractal
mandelbrot_image = compute_mandelbrot()
show_plot(mandelbrot_image)
