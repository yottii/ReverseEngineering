import pandas
import seaborn
from matplotlib import pyplot

malware = pandas.read_csv("malware_data.csv")
axis = seaborn.violinplot(x=malware['type'], y=malware['size'])
axis.set(xlabel="Malware type", ylabel="File size in bytes (log base-10)",
         title="File sizes by malware type", yscale="log")
pyplot.show()
