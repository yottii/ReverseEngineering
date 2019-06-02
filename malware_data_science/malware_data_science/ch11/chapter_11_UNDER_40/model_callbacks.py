import numpy as np
from keras import callbacks
from sklearn import metrics
# local code:
from model_training import get_validation_data, make_training_data_generator
from model_architecture import my_model


class MyCallback(callbacks.Callback):
    """
    Custom Keras callback to print validation AUC metric during training.
    Allowable over-writable methods:
    on_epoch_begin, on_epoch_end, on_batch_begin, on_batch_end,
    on_train_begin, on_train_end
    """

    def on_epoch_end(self, epoch, logs={}):
        validation_labels = self.validation_data[1]
        validation_scores = self.model.predict(self.validation_data[0])
        # flatten the scores:
        validation_scores = [el[0] for el in validation_scores]
        fpr, tpr, thres = metrics.roc_curve(y_true=validation_labels,
                                            y_score=validation_scores)
        auc = metrics.auc(fpr, tpr)
        print('\n\tEpoch {}, Validation AUC = {}'.format(epoch,
                                                         np.round(auc, 6)))


if __name__ == '__main__':
    # first, let's use some code from previous sections to get our model
    # and data up and running:
    features_length = 1024
    num_obs_per_epoch = 5000
    batch_size = 128

    # create the model using the function from the model architecture section:
    model = my_model(input_length=features_length)

    # make the training data generator:
    training_generator = make_training_data_generator(
        batch_size=batch_size,
        features_length=features_length
    )
    # and the validation data:
    validation_data = get_validation_data(features_length=features_length,
                                          n_validation_files=1000)

    ##########################################################################
    # now for some new code:
    # first, use a built-in callback to save the best model over training:
    model.fit_generator(
        generator=training_generator,
        steps_per_epoch=num_obs_per_epoch / batch_size,
        epochs=5,
        validation_data=validation_data,
        callbacks=[
            callbacks.ModelCheckpoint('best_model.h5',
                                      monitor='val_loss',
                                      save_best_only=True)
        ],
    )

    # next, use the built-in callback to record the model after every epoch.
    model.fit_generator(
        generator=training_generator,
        steps_per_epoch=num_obs_per_epoch / batch_size,
        epochs=5,
        validation_data=validation_data,
        callbacks=[
            callbacks.ModelCheckpoint('model_epoch_{epoch}.h5',
                                      monitor='val_loss',
                                      save_best_only=False)
        ],
    )

    # now try using our custom callback with AUC logging!
    model.fit_generator(
        generator=training_generator,
        steps_per_epoch=num_obs_per_epoch / batch_size,
        # making the training artificially fast to showcase the validation logs!
        epochs=5,
        validation_data=validation_data,
        callbacks=[
            MyCallback()
        ],
    )