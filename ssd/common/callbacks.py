import tensorflow as tf


class CallbackBuilder:
    def __init__(self, name, config):
        self._name = name
        self._model_dir = config['model_dir']
        self._early_stopping_patience = config['patience']

    def get_callbacks(self):
        callbacks_list = [
            tf.keras.callbacks.TensorBoard(log_dir=self._model_dir + 'tensorboard'),
            tf.keras.callbacks.ModelCheckpoint(
                filepath=self._model_dir +
                'checkpoints/ssd_weights_{}'.format(self._name),
                monitor='val_loss',
                save_best_only=True,
                save_weights_only=True,
                verbose=1),
            tf.keras.callbacks.EarlyStopping(
                monitor='val_loss',
                min_delta=0,
                patience=self._early_stopping_patience,
                verbose=1)]
        return callbacks_list
