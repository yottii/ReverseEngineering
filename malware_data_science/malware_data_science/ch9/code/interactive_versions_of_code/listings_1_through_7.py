"""
This code is meant to be run line by line in an interactive python console, so that that output is automatically
printed to the screen.
"""
import pandas

example_data = [{'column1': 1, 'column2': 2},
                {'column1': 10, 'column2': 32},
                {'column1': 3, 'column2': 58}]

pandas.DataFrame(example_data)

malware = pandas.read_csv("malware_data.csv")

malware.describe()

malware['positives']

malware['positives'].mean()
malware['positives'].max()
malware['positives'].min()
malware['positives'].std()

malware[malware['type'] == 'trojan']['positives'].mean()
malware[malware['type'] == 'bitcoin']['positives'].mean()
malware[malware['type'] == 'worm']['positives'].mean()


malware[malware['size'] > 1000000]['positives'].mean()
malware[malware['size'] > 2000000]['positives'].mean()
malware[malware['size'] > 3000000]['positives'].mean()
malware[malware['size'] > 4000000]['positives'].mean()
malware[malware['size'] > 5000000]['positives'].mean()
