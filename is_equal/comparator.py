# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Gallery.
#
# storm-gallery is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from .hasher import hash_dir


def is_equal(directory_one: str, directory_two: str, algorithm: str = "md5", **kwargs):
    """Function to check if two directories has the same content (based on bytes).

    To compare both directories this function uses hash functions. So, in this
    comparison, only the content bytes is used as basis. The structure and
    files names is not used.
    """
    directory_one_hash = hash_dir(directory_one, algorithm, **kwargs)
    directory_two_hash = hash_dir(directory_two, algorithm, **kwargs)

    return (
        directory_one_hash.checksum == directory_two,
        directory_one_hash,
        directory_two_hash,
    )
