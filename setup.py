from distutils.core import setup

setup(
    name="COVID19",
    py_modules=["COVID19"],
    entry_points={"console_scripts": ["COVID19=COVID:main"]},
    version="0.2.0",
    description="stressful DOS tool for websites.",
    author="Alwaleed Alabri",
    author_email="asa10.asa10.asa69@gmail.com",
    url="https://github.com/asa-asa/COVID19",
    keywords=["dos", "ddos", "http", "covid19"],
)
