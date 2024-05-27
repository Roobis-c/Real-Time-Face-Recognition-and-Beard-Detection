import cv2
import os

# Set up directories for saving the dataset
dataset_path = 'dataset'
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

# Function to capture images from webcam and save them with a label
def capture_images(label, num_images=100):
    # Create a directory for the label if it doesn't exist
    label_path = os.path.join(dataset_path, label)
    if not os.path.exists(label_path):
        os.makedirs(label_path)
    
    # Capture images from the webcam
    cap = cv2.VideoCapture(0)
    print(f'Capturing {num_images} images for label: {label}')
    
    count = 0
    while count < num_images:
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2.imshow('Capture Images', frame)
        
        # Save the captured image
        img_path = os.path.join(label_path, f'{label}_{count}.jpg')
        cv2.imwrite(img_path, frame)
        
        count += 1
        
        # Display the frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print(f'Finished capturing {num_images} images for label: {label}')

# Example usage:
# Call capture_images with the person's name and the number of images to capture
y = int(input("No of People: "))
for i in range(y):
    person_name = input(f'Name of {i+1} Person: ')  # Change this to the name of the person
    capture_images(person_name, num_images=100)  # Capture 100 images for this person
