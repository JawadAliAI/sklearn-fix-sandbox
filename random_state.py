def check_random_state(seed):
    if isinstance(seed, np.random.Generator):
        return seed
    elif isinstance(seed, int) or seed is None:
        return np.random.RandomState(seed)
    else:
        raise ValueError('Invalid seed type: {}'.format(type(seed)))
