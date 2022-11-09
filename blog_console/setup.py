from setuptools import setup, find_packages

setup(
    name="greet",
    version="1.0.0",
    description="Greet in the console",
    packages=["greet"],
    entry_points={
        "console_scripts": [
            "SayHi=greet.my_app:my_func",
            "SayHello=greet.my_app:my_func_with_args",
        ],
    },
)
