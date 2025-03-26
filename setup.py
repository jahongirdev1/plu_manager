from setuptools import setup, find_packages

setup(
    name="plu_manager",
    version="1.0.0",
    description="Universal PLU file generator and uploader for PLU Manager software",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pyautogui",
        "keyboard"
    ],
    entry_points={
        'console_scripts': [
            'plu-manager=plu_manager.main:run'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    python_requires='>=3.7',
)
