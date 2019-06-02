import pandas
import seaborn
from matplotlib import pyplot

malware = pandas.read_csv("malware_data.csv")
axis = seaborn.violinplot(x=malware['type'], y=malware['positives'])
axis.set(xlabel="Malware type", ylabel="Number of vendor detections",
         title="Number of detections by malware type")
pyplot.show()
