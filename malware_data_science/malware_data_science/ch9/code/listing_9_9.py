import dateutil
import pandas
from matplotlib import pyplot
pyplot.rcParams["figure.figsize"] = (10,4)

malware = pandas.read_csv("malware_data.csv")
malware['fs_date'] = [dateutil.parser.parse(d) for d in malware['fs_bucket']]
ransomware = malware[malware['type'] == 'ransomware']
pyplot.plot(ransomware['fs_date'], ransomware['positives'], 'ro', alpha=0.05)
pyplot.title("Ransomware detections over time")
pyplot.xlabel("Date")
pyplot.ylabel("Number of anti-virus engine detections")
# pyplot.show()
pyplot.savefig("Figure_9-4.png")
