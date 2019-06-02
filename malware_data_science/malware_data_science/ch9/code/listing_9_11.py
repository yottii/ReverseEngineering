import pandas
from matplotlib import pyplot
import seaborn
pyplot.rcParams["figure.figsize"] = (10,8)

malware = pandas.read_csv("malware_data.csv")
seaborn.countplot(x='type', data=malware)
# pyplot.show()
pyplot.savefig("Figure_9-6.png")