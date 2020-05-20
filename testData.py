import seaborn as sns
import matplotlib.pyplot as plt

def run_analyze(output_filename):
    # opening the data and separate into data + label list
    org = open("TestData/data.in", "r")
    org = org.read()
    org = org.split('\n')
    data = [float(i) for i in org[0].split()]
    label = org[1].split()

    # plotting and saving figure
    sns.set()
    fig = plt.figure(figsize=(15, 7))
    fig = sns.barplot(label, data)
    plt.ylabel("Probability", labelpad=20, fontsize=15)
    plt.xlabel("Object", labelpad=20, fontsize=15)
    plt.savefig("static/image/" + output_filename)
    return True