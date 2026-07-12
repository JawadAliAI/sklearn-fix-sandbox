# This file is adapted from scikit-learn (https://github.com/scikit-learn/scikit-learn)
# Original code: sklearn/utils/validation.py, check_random_state()
# Copyright (c) 2007-2024 The scikit-learn developers.
# License: BSD-3-Clause
#
# Included here as a small, realistic, self-contained snippet for testing
# an AI coding agent against real-world code (not a full sklearn install).

import numbers

import numpy as np


def check_random_state(seed):
    """Turn seed into a np.random.RandomState instance.

    Parameters
    ----------
    seed : None, int or instance of RandomState
        If seed is None, return the RandomState singleton used by np.random.
        If seed is an int, return a new RandomState instance seeded with seed.
        If seed is already a RandomState instance, return it.
        Otherwise raise ValueError.

    Returns
    -------
    :class:`numpy:numpy.random.RandomState`
        The random state object based on `seed` parameter.
    """
    if seed is None or seed is np.random:
        return np.random.mtrand._rand
    if isinstance(seed, numbers.Integral):
        return np.random.RandomState(seed)
    if isinstance(seed, np.random.RandomState):
        return seed
    raise ValueError(
        f"{seed!r} cannot be used to seed a numpy.random.RandomState instance"
    )
