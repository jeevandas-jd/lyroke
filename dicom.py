import pydicom
import matplotlib.pyplot as plt
file=pydicom.dcmread('demo.dcm')

print(file.PatientName)

plt.imshow(file.pixel_array,cmap=plt.cm.gray)

plt.show()
