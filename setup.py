from setuptools import setup

setup(
    name="speedtest-prometheus",
    version="0.0.1",
    packages=[""],
    url="https://github.com/wengole/speedtest-prometheus",
    license="",
    author="Ben Cole",
    author_email="",
    description="Prometheus exporter wrapping new Ookla speedtest CLI",
    install_requires=["prometheus_client",],
)
