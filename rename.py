# -*- coding=utf-8 -*-
import logging
import os
import re

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    for filename in os.listdir("."):
        if not os.path.isfile(filename):
            continue

        if not (m := re.match(r"(.+\.firmware)\.bin$", filename)):
            continue

        name = m.group(1)

        with open(filename, "rb") as f:
            blob = f.read()

        version = None
        if m := re.search(rb"@\(#\)MPTFW-([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)-", blob):
            version = m.group(1).decode()

        if version is not None:
            name = f"{name}.{version}.bin"
            logger.info("Renaming %s to %s", filename, name)
            os.rename(filename, name)

