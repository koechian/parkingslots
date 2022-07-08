#Identifying and tracking Parking Lot Status using Computer Vision.

1. Parking Slot Identification.
   -> Use manual Segmentation to mark Regions of Intrest.(Parking slots)
   -> Upgrade to Image based Segmentation using Active Contours
2. Car Detection.
   -> Define a vehicle using 4 bounds.-[MASK RCNN]
   -> Object Classification. (Cars must be distinguishable from other objects)
3. Slot Occupancy Tracking.
   -> A slot's status is updated in memory.
   -> Parking lot status(Current Car count vs Total available slots)
   -> Directions to available space as a feature.
