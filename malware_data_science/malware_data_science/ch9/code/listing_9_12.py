import pandas
import seaborn
from matplotlib import pyplot
pyplot.rcParams["figure.figsize"] = (10,8)

malware = pandas.read_csv("malware_data.csv")
axis = seaborn.distplot(malware['positives'])
axis.set(xlabel="Number of engines detecting each sample (out of 57)",
         ylabel="Amount of samples in the dataset",
         title="Commercial anti-virus detections for malware")
# pyplot.show()
pyplot.savefig("Figure_9-7.png")