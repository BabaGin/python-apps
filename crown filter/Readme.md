# Python Face Filter with Crown Overlay

This Python application demonstrates real-time face detection and recognition using OpenCV. It allows users to apply a virtual crown overlay on their detected faces through a webcam feed.

## Features:
- **Real-time Face Detection:** Utilizes OpenCV's pre-trained Haar cascade classifier to detect faces in a live webcam feed.
- **Crown Overlay:** Upon detecting a face, the application overlays a virtual crown on top of the detected face.
- **Dynamic Crown Scaling:** The size of the crown overlay dynamically adjusts based on the size of the detected face, ensuring proper alignment and sizing.

## Requirements:
- Python 3.x
- Pip

## Dependencies:
- OpenCV
- NumPy

## Usage:
1. Clone the repository to your local machine.
2. Use virtual environment is preferably 
3. Install the required dependencies (`pip install opencv-contrib-python`, `pip install numpy`).
4. Enjoy real-time face detection and recognition with the virtual crown overlay!

---
## Virtual Environment
In case you wanna create virtual environment to your device,
here are the steps to create a virtual environment in Python:

1. **Install Virtualenv (if not already installed):**
   
   If you haven't installed `virtualenv` yet, you can do so using pip:
   ```
   pip install virtualenv
   ```

2. **Create a New Virtual Environment:**

   Navigate to your project directory in the terminal and run the following command to create a new virtual environment named `venv`:
   ```
   virtualenv venv
   ```

   This will create a new directory named `venv` in your project folder, containing a self-contained Python environment.

3. **Activate the Virtual Environment:**

   Before you can use the virtual environment, you need to activate it. Run the appropriate command based on your operating system:

   - On Windows:
     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

   You should see `(venv)` in your terminal prompt, indicating that the virtual environment is active.

4. **Install Dependencies:**

   While the virtual environment is active, you can install packages using pip. For example:
   ```
   pip install numpy opencv-contrib-python
   ```

   This will install NumPy and OpenCV packages into your virtual environment.

5. **Deactivate the Virtual Environment:**

   To exit the virtual environment, simply run the following command:
   ```
   deactivate
   ```

   Your terminal prompt should return to normal, indicating that the virtual environment is no longer active.

That's it! You now have a virtual environment set up for your Python project. You can activate it whenever you want to work on your project and deactivate it when you're done. This helps keep your project dependencies isolated and prevents conflicts with other Python projects.

---

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
