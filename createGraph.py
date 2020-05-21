import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def createGraph(label, data, graph_filename):
    # plotting and saving figure
    sns.set()
    fig = plt.figure(figsize=(15, 7))
    fig = sns.barplot(label, data)
    plt.ylabel("Probability", labelpad=20, fontsize=15)
    plt.xlabel("Object", labelpad=20, fontsize=15)
    plt.savefig("static/image/" + graph_filename)
    return True