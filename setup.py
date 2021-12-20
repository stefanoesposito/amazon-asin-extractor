from setuptools import setup

APP=['asin_extractor.py']
OPTIONS = {
    'argv_emulation': True,
    # 'packages': ['certifi',]
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)