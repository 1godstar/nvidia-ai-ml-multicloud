import numpy as np

def preprocess_input(data):
    """Simple preprocessing: ensure input is numpy array with right shape"""
    if isinstance(data, list):
        data = np.array(data)
    if len(data.shape) == 1:
        data = np.expand_dims(data, 0)
    return data.astype('float32')
