# Identifying and tracking Parking Lot Status using Computer Vision.

1. Parking Slot Identification.
   - Use manual Segmentation to mark Regions of Intrest.(Parking slots)
   - Upgrade to Image based Segmentation using Active Contours
   - Canny edge detection was used to detect the straight lines in parking lots.
2. Car Detection.
   - Define a vehicle using 4 bounds.-[MASK RCNN]
   - Object Classification. (Cars must be distinguishable from other objects)
3. Slot Occupancy Tracking.
   - A slot's status is updated in memory.
   - Parking lot status(Current Car count vs Total available slots)
   - Directions to available space as a feature.

## Manual Segmentation

- Segmentor.py is used to manually select parking slots in a video feed.
- The cars will then be identified using Mask-RCNN.
- The Area of Overlap between the cars bounding points and the previously identified ROI(parking slots) will then be calculated and used to determine the ocupancy of said lot.
- The cars mask can be used to make this more accurate instead of the cars bbounding box.

## AI Segmentation

- Low accuracy, work in progress.
