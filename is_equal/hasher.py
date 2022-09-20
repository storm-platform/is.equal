# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Gallery.
#
# storm-gallery is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

import os

import pandas as pd

from checksumdir import dirhash
from storm_hasher import StormHasher


class DirectoryHash:
    """A hashed directory."""

    def __init__(self, name, checksum, files):
        """Initializer."""
        self.name = name
        self.files = files
        self.checksum = checksum


def hash_dir(directory_path: str, algorithm: str, followlinks=False) -> DirectoryHash:
    """Hash (in multiple ways) a directory and its files (Based on content)."""
    if not os.path.isdir(directory_path) or not os.path.exists(directory_path):
        raise NotADirectoryError("`hash_dir` only works on directories")

    # 1. Generating a checksum to the entire directory
    fulldir_hash = dirhash(directory_path, hashfunc=algorithm, followlinks=followlinks)

    # 2. Generating a checksum to the individual files
    hashes = []
    hasher = StormHasher(algorithm)

    for root, dirs, files in os.walk(
        directory_path, topdown=True, followlinks=followlinks
    ):

        dirs.sort()
        files.sort()

        for fname in files:
            filepath = os.path.join(root, fname)
            filehash = hasher.hash_file(filepath)

            hashes.append(dict(fname=filehash))

    return DirectoryHash(
        name=os.path.basename(directory_path),
        checksum=fulldir_hash,
        files=pd.DataFrame(hashes),
    )
