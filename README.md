# Identifying and tracking Parking Lot Status using Computer Vision.

1. Parking Slot Segmentation.
   - Use manual Segmentation to mark Regions of Intrest.(Parking slots)
     -A parking Slot is defined as a single point(x,y) plus the width and height of a lot.
2. Car Detection.

   - MASK RCNN did not work as expected. Given that the program is supposed to work on low cost hardware, image processing was preffered.
   - Humans and cars must be distingiushable.
   - Non-Zero pixels are counted after the image/feed has gone through multiple iterations of processing.
     - Feed was converted to Grayscale.
       ![Grayscale Image](/images/grayscale.png?raw=true "Feed Converted to Grayscale")
     - A Gaussian Blur was then applied to remove noise.
       ![After Blur](/images/gaussianblur.png?raw=true "Blur Applied to reduce visual noise")
     - Feed was converted to a Binary Image Map using an Adaptive Threshold.
       ![Binary Mapped Image](/images/binarymap.png?raw=true "Converted Image")
     - The image still has a lot of noise(The small dotted lines and spots that can be seen in the picture above) and Median blur was then used on to further remove these spots.
       ![Binary Mapped Image](/images/medianblur.png?raw=true "Converted Image")
     - One pass of dilation was then applied to the feed. (This basically causes the brighter spots in an image increase in size. See [OpenCv: Eroding and Dilating](https://docs.opencv.org/3.4/db/df6/tutorial_erosion_dilatation.html))
       ![Image after Dilation](/images/dilation.png?raw=true "Dilated Image")
     - Given that the image was converted to a binary map, the non-zero pixels will be the white ones. We can then count how many of these pixels exist in a bounding box(parking lot). This will be used to determine the status of a lot.

3. Slot Occupancy Tracking.

   - Slot position,status and distance from a common origin(gate) is stored in a Nested Dictionary to allow for fast lookup times. The dictionary is then pickled to allow for data persistance.
   - Parking lot status(Current Car count vs Total available slots) is tracked throughout.
   - Directions to available the nearest available space is shown in refrence to the gate.

4. Graphical User Interfaces

- Implement a means through which the drivers can view the number of slots available and be informed of the nearest available slot.
  - This is to be done using the Eel Library.
    -Multithreaded to allow the Image Processing and the GUI to be viewed concurrently.
    -Implement a means for the lot manager to view current occupied slots.

## Manual Segmentation

- The Width and Length of parking lots are calculated manually.
- Slots.py is used to manually select parking slots in a video feed.

## AI Segmentation

- Low accuracy, work in progress.
