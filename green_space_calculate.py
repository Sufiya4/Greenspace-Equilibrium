# green_space_calculator.py
import cv2
import numpy as np

def calculate_green_space_ratio(area_name):
    # Mapping of area names to image paths
    area_image_paths = {
        'kumaraswamy_layout': '/workspaces/137993833/Final/images/xx.jpg',
        'banashankari':'/workspaces/137993833/Final/images/banashankri.jpg',
        'jp_nagar':'/workspaces/137993833/Final/images/jp_nagar.jpg',
        'jayanagar': '/workspaces/137993833/Final/images/jayanagar.jpg',
        'rr_nagar': '/workspaces/137993833/Final/images/rr_nagar.jpg',
        'mg_road': '/workspaces/137993833/Final/images/mg_road.jpg',
        'banaswadi': '/workspaces/137993833/Final/images/banaswadi.jpg',
        'kormangala':'/workspaces/137993833/Final/images/kormangala.jpg',
        'indranagar':'/workspaces/137993833/Final/images/indranagar.jpg',
        'chickpete':'/workspaces/137993833/Final/images/chickpete.jpg'
        # Add more area names and corresponding image paths as needed
    }

    # Check if the area_name exists in the dictionary
    if area_name not in area_image_paths:
        raise ValueError(f"Error: Unknown area name '{area_name}'.")

    # Load the satellite image
    image = cv2.imread(area_image_paths[area_name])

    if image is None:
        raise ValueError(f"Error: Unable to read the image for area '{area_name}'.")

    # Convert the image to the HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define a green color range in HSV
    lower_green = np.array([30, 40, 40])
    upper_green = np.array([90, 255, 255])

    # Create a mask to extract green areas
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Apply the mask to the original image
    green_areas = cv2.bitwise_and(image, image, mask=mask)

    # Calculate the green space ratio
    total_pixels = np.prod(image.shape[:2])
    green_pixels = np.count_nonzero(mask)
    green_space_ratio = green_pixels / total_pixels

    return green_space_ratio
