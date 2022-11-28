#!/usr/bin/env python3
import os
import sys

from metadata import METADATA_MAPPING, load_metadata

platform = sys.platform
distributions = sys.argv[1:]
if not distributions:
    distributions = os.listdir("stubs")

if platform in METADATA_MAPPING:
    for distribution in distributions:
        for package in load_metadata(distribution)["tool"]["stubtest"][METADATA_MAPPING[platform]]:
            print(package)
