import cv2
import numpy as np

def apply_effect(frame, effect_name):
    """
    Apply the specified effect to the input frame
    """
    if effect_name == 'grayscale':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    elif effect_name == 'blur':
        return cv2.GaussianBlur(frame, (15, 15), 0)
    
    elif effect_name == 'edge_detection':
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray, 100, 200)
    
    elif effect_name == 'sepia':
        kernel = np.array([[0.272, 0.534, 0.131],
                          [0.349, 0.686, 0.168],
                          [0.393, 0.769, 0.189]])
        return cv2.transform(frame, kernel)
    
    elif effect_name == 'invert':
        return cv2.bitwise_not(frame)
    
    elif effect_name == 'emboss':
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kernel = np.array([[-2, -1, 0],
                          [-1, 1, 1],
                          [0, 1, 2]])
        return cv2.filter2D(gray, -1, kernel)
    
    elif effect_name == 'sharpen':
        kernel = np.array([[-1, -1, -1],
                          [-1, 9, -1],
                          [-1, -1, -1]])
        return cv2.filter2D(frame, -1, kernel)
    
    elif effect_name == 'cartoon':
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Apply median blur
        gray = cv2.medianBlur(gray, 5)
        # Detect edges
        edges = cv2.adaptiveThreshold(gray, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 9, 9)
        # Apply bilateral filter
        color = cv2.bilateralFilter(frame, 9, 300, 300)
        # Combine color image with edges
        return cv2.bitwise_and(color, color, mask=edges)
    
    elif effect_name == 'noise_reduction':
        return cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21)
    
    elif effect_name == 'rotate_90':
        return cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    
    elif effect_name == 'flip_horizontal':
        return cv2.flip(frame, 1)
    
    elif effect_name == 'flip_vertical':
        return cv2.flip(frame, 0)
    
    else:
        return frame  # Return original frame if effect not found 