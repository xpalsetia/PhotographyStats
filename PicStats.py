import piexif
import os
from fractions import Fraction
import array
import collections



folder_path = "/enter/folder/path/here"
exposure_count = []
focal_count = []

# loop through all files in the folder
for filename in os.listdir(folder_path):
    # check that the file is a file (not a directory)
    if os.path.isfile(os.path.join(folder_path, filename)):
        filename = folder_path + "/" + filename

        # read the EXIF data from a JPEG image
        exif_data = piexif.load(filename)

        # extract the relevant metadata values
        focal_length = exif_data["Exif"][piexif.ExifIFD.FocalLength][0] / exif_data["Exif"][piexif.ExifIFD.FocalLength][1]
        exposure_time_1 = exif_data["Exif"][piexif.ExifIFD.ExposureTime][0]
        exposure_time_2 = exif_data["Exif"][piexif.ExifIFD.ExposureTime][1]
        fraction = Fraction(exposure_time_1,exposure_time_2)

        # add metadata values to arrays
        focal_count.append(str(focal_length))
        exposure_count.append(str(fraction))


# extract most common metadata values from list
counter = collections.Counter(focal_count)
most_common_focal = counter.most_common(1)[0][0]
counter = collections.Counter(exposure_count)
most_common_exp = counter.most_common(1)[0][0]

# print the results values
print(f"Most common focal length: {most_common_focal}mm")
print(f"Most common exposure time: {most_common_exp}")
