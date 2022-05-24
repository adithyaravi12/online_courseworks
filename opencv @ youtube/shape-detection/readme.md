##Procedure:

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
	
			
