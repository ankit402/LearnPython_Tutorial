#real-world use cases of NumPy broadcasting — where it saves time, memory, and code.

#✅ 1. Image Processing: Subtracting the Mean Color

from PIL import Image
import numpy as np

import numpy as np
import matplotlib.pyplot as plt

# Create a random RGB image (values 0–255)
image = np.random.randint(0, 256, size=(256, 256, 3), dtype=np.uint8)

# Compute mean color
mean_color = np.mean(image, axis=(0, 1))

# Normalize image by subtracting mean color (broadcasting)
normalized = image.astype(np.float32) - mean_color

# Rescale normalized image back to 0–255 for display
normalized_rescaled = np.clip(normalized + 127, 0, 255).astype(np.uint8)

# Plot before and after
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Normalized (mean-subtracted)")
plt.imshow(normalized_rescaled)
plt.axis('off')

plt.tight_layout()
plt.show()
