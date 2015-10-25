"""Setup for client_side_authoring XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='client_side_authoring-xblock',
    version='0.1',
    description='client_side_authoring XBlock',   # TODO: write a better description.
    packages=[
        'client_side_authoring',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'client_side_authoring = client_side_authoring:ClientSideAuthoringXBlock',
        ]
    },
    package_data=package_data("client_side_authoring", ["static", "public"]),
)
