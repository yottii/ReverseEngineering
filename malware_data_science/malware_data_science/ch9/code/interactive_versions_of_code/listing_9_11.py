import pandas
from matplotlib import pyplot
import seaborn

malware = pandas.read_csv("malware_data.csv")
seaborn.countplot(x='type', data=malware)
pyplot.show()
