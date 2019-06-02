from keras.models import load_model
from sklearn import metrics
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
# local code:
from model_training import get_validation_data


def roc_plot(fpr, tpr, path_to_file):
    """
    :param fpr: array of false positive rates (an output from metrics.roc_curve())
    :param tpr: array of true positive rates (an output from metrics.roc_curve())
    :param path_to_file: where you wish to save the .png file
    """
    fig, ax = plt.subplots(figsize=(10, 10))

    plt.grid(True)
    plt.xlabel("False positive rate")
    plt.ylabel("True positive rate")
    plt.title("ROC curve")
    plt.ylim([0, 1])

    ax.get_xaxis().set_minor_locator(matplotlib.ticker.AutoMinorLocator())
    ax.get_yaxis().set_minor_locator(matplotlib.ticker.AutoMinorLocator())
    ax.grid(b=True, which='major', color='w', linewidth=1.0)
    ax.grid(b=True, which='minor', color='w', linewidth=0.5)

    plt.semilogx(fpr, tpr, 'b-', label="Test set")
    plt.savefig(path_to_file)
    fig.clear()
    plt.close(fig)


if __name__ == '__main__':
    # first, load up the trained model
    model = load_model('my_model.h5')  # from keras.models.load_model

    # grab the validation data:
    validation_data = get_validation_data(n_validation_files=1000,
                                          features_length=1024)
    # next, split it up into validation labels (0, 1) and flattened predictions:
    validation_labels = validation_data[1]
    validation_scores = [el[0] for el in model.predict(validation_data[0])]

    fpr, tpr, thres = metrics.roc_curve(y_true=validation_labels,
                                        y_score=validation_scores)
    auc = metrics.auc(fpr, tpr)
    print('Validation AUC = {}'.format(auc))

    # now let's plot the ROC curve
    roc_plot(fpr=fpr, tpr=tpr, path_to_file='roc_curve.png')
