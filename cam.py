import cv2

# Create a window to display the edges video
cv2.namedWindow('Edges')

# Define a callback function for the trackbars
def update(val):
    # Get the current trackbar positions
    threshold1 = cv2.getTrackbarPos('Threshold1', 'Edges')
    threshold2 = cv2.getTrackbarPos('Threshold2', 'Edges')

    # Read the next frame from the webcam
    ret, frame = cap.read()
    print(frame.shape)

    new_width = 500
    new_height = 400
    # Resize the image
    resized_img = cv2.resize(frame, (new_width, new_height))

    if ret:
        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to the frame
        blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        # Apply Canny edge detection to the blurred frame
        edges = cv2.Canny(blurred_frame, threshold1, threshold2)

        # Display the edges video
        cv2.imshow('Edges', edges)
        cv2.imshow('Normal',resized_img)

# Open the webcam for reading
cap = cv2.VideoCapture(0)

# Create two trackbars to control the threshold1 and threshold2 values
cv2.createTrackbar('Threshold1', 'Edges', 100, 255, update)
cv2.createTrackbar('Threshold2', 'Edges', 200, 255, update)

# Call the update function to initialize the edges video
update(0)

# Process each frame of the video
while True:
    # Wait for a key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Call the update function to process the next frame
    update(0)

# Release the webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()