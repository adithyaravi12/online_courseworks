
# Color picker using OpenCV

While learning OpenCV, I was able to program a color picker from the base up, that displays three individual windows; where one is the original image, second is the window toolbar where you get to choose the color you want to pick and the third window is the actual image with the desired color picked.

## Procedure

    1. Import necessary dependencies
    2. Defined an empty function and a stack function that is used to stack the different windows into a single window by passing it as a parameter
    3. Create a trackbar window with the desired dimensions and label and set them to their default values.
    4. Read an image and covert it to cv2.COLOR_BGR2HSV ie. Hue, Saturation and value
    5. Mask the image with the corresponding values from the trackbar window
    6. Display output



## Run Locally

Clone the project

```bash
  git clone https://github.com/adithyaravi12/online_courseworks/tree/main/opencv%20%40%20youtube/color-picker
```

Go to the project directory

```bash
  cd color-picker
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```


## Screenshots

![App Screenshot](https://github.com/adithyaravi12/online_courseworks/blob/main/opencv%20%40%20youtube/color-picker/output.png)
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://adithyaravi12.github.io/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adithya-ravi-707443126/)
