
# Color picker using OpenCV

While learning OpenCV, I was able to program a shape detector from the base up, that displays a stacked window with images at different stages of the project, and the output obtained is a rectangle that maps around the shape, and display the name of the shape on top of it
##  Procedure

    1. Read input image
    2. Convert it to greyscale
    3. Add gaussian blur
    4. Add canny to find the edges 
    5. From the edges obtained, find the contours 
	    a. Cv2.RETR_EXTERNAL(source, retrieval method, approximation method) 
		    i. Retrieval method - to retrieve the outer most contours of the edges obtained
		    ii. approximation method - to return all of the information or compressed values ie reduce the points 
    6. Detect minimum threshold so it doesnt detect any noise 
    7. Create a for loop to loop through the contour variable
	    a. Find the area - cv2. contourArea(cnt)
	    b. Draw the shape using cv2.drawContours(source, contour, contour index, color, thickness
    8. Calculate the curve length
    9. Approximate the number of corner points
    10. Create object corner variable based on the length of the corner points
    11. Draw a bounding box for the shapes to find the total width and height of objects - cv2.boundingRect(approx)
    12. Categorize objects 
## Run Locally

Clone the project

```bash
  git clone https://github.com/adithyaravi12/online_courseworks/tree/main/opencv%20%40%20youtube/shape-detection
```

Go to the project directory

```bash
  cd shape-detection
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

![App Screenshot](https://github.com/adithyaravi12/online_courseworks/blob/main/opencv%20%40%20youtube/shape-detection/output.png)
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://adithyaravi12.github.io/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adithya-ravi-707443126/)
