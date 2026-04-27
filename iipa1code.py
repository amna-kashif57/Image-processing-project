import numpy as np
import matplotlib.pyplot as plt
from skimage import io as skio

def negative_image(img):
    return 255 - img

def threshold_image(img, threshold_value, direction):
    if direction == "up":
        return np.where(img > threshold_value, 255, 0)
    elif direction == "down":
        return np.where(img < threshold_value, 255, 0)
    else:
        raise ValueError("Invalid direction. Choose 'up' or 'down'.")

def scaled_image(img, scale_factor):
    result = img * scale_factor
    return np.clip(result, 0, 255).astype(np.uint8)

def log_image(img, log_base):
    img_norm = img / 255.0
    result = (np.log(1 + img_norm) / np.log(log_base)) * 255
    return np.clip(result, 0, 255).astype(np.uint8)

def power_law_image(img, gamma):
    img_norm = img / 255.0
    result = np.power(img_norm, gamma) * 255
    return np.clip(result, 0, 255).astype(np.uint8)

def main():
    image_path = r"C:\Users\Amna kashif\Downloads\iip1.jpg"  # Your image path

    img = skio.imread(image_path, as_gray=True)
    img = (img * 255).astype(np.uint8) if img.max() <= 1 else img.astype(np.uint8)

    print("\nChoose Transformation:")
    print("1. Negative Image")
    print("2. Threshold Image")
    print("3. Scaled Image")
    print("4. Logarithm Image")
    print("5. Power Law Image")
    choice = int(input("Enter choice (1-5): "))

    params = {}
    if choice == 1:
        pass
    elif choice == 2:
        params['threshold_value'] = int(input("Enter threshold value (0-255): "))
        params['direction'] = input("Direction (up/down): ").lower()
    elif choice == 3:
        params['scale_factor'] = float(input("Enter scaling factor: "))
    elif choice == 4:
        params['log_base'] = float(input("Enter log base (e.g., 2): "))
    elif choice == 5:
        params['gamma'] = float(input("Enter gamma/power value: "))
    else:
        print("Invalid choice!")
        return

    if choice == 1:
        result = negative_image(img)
        func_name = "Negative Image"
    elif choice == 2:
        result = threshold_image(img, **params)
        func_name = "Threshold Image"
    elif choice == 3:
        result = scaled_image(img, **params)
        func_name = "Scaled Image"
    elif choice == 4:
        result = log_image(img, **params)
        func_name = "Logarithm Image"
    elif choice == 5:
        result = power_law_image(img, **params)
        func_name = "Power Law Image"

    # Plot before and after
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(result, cmap='gray')
    plt.title(f"{func_name} - Amna Kashif - L1F23BSCS0959")
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()

