import pandas
from matplotlib import pyplot

malware = pandas.read_csv("malware_data.csv")
pyplot.plot(malware['size'], malware['positives'],
            'bo', alpha=0.01)
pyplot.xscale("log")
pyplot.ylim([0, 57])
pyplot.xlabel("File size in bytes (log base-10)")
pyplot.ylabel("Number of detections")
pyplot.title("Number of anti-virus detections versus file size")
pyplot.show()
