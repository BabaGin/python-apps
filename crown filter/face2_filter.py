import cv2

# Load pre-trained face detection cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the crown image
crown_img = cv2.imread('crown.png', cv2.IMREAD_UNCHANGED)

# Function to overlay transparent image on the background
def overlay_transparent(background, overlay, x, y):
    # Separate the overlay image into color channels and alpha channel
    overlay_rgb = overlay[..., :3]
    alpha = overlay[..., 3] / 255.0

    # Calculate coordinates for overlay placement
    y1, y2 = y, y + overlay.shape[0]
    x1, x2 = x, x + overlay.shape[1]

    # Blend the images using alpha blending
    for c in range(3):
        background[y1:y2, x1:x2, c] = (1.0 - alpha) * background[y1:y2, x1:x2, c] + alpha * overlay_rgb[:, :, c]

    return background

# Modify the recognize_faces function to use RGBA crown image
def recognize_faces(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Recognize faces and overlay crown
    for (x, y, w, h) in faces:
        # Calculate position to place the crown on top of the head
        crown_width = int(w * 1)  # Adjust crown width based on face width
        crown_height = int(crown_width * crown_img.shape[0] / crown_img.shape[1])
        crown_x = x - int((crown_width - w) / 2)  # Center crown horizontally on the face
        crown_y = y - int(crown_height / 2)

        # Ensure crown image is within the bounds of the image
        crown_x = max(crown_x, 0)
        crown_y = max(crown_y, 0)
        crown_x_end = min(crown_x + crown_width, image.shape[1])
        crown_y_end = min(crown_y + crown_height, image.shape[0])

        # Resize the crown image to fit the width of the face
        resized_crown = cv2.resize(crown_img, (crown_x_end - crown_x, crown_y_end - crown_y))

        # Overlay the crown image onto the original frame
        image = overlay_transparent(image, resized_crown, crown_x, crown_y)

    return image

# Main function
def main():
    # Open video capture
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        if ret:
            # Perform face recognition on the frame
            frame = recognize_faces(frame)

            # Display the frame
            cv2.imshow('Crown Filter', frame)

            # Break the loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release the video capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
