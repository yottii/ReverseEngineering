import pandas
from matplotlib import pyplot
pyplot.rcParams["figure.figsize"] = (10,6)


malware = pandas.read_csv("malware_data.csv")
pyplot.plot(malware['size'], malware['positives'],
            'bo', alpha=0.01)
pyplot.xscale("log")
pyplot.ylim([0, 57])
pyplot.xlabel("File size in bytes (log base-10)")
pyplot.ylabel("Number of detections")
pyplot.title("Number of anti-virus detections versus file size")
# pyplot.show()
pyplot.savefig("Figure_9-3.png")