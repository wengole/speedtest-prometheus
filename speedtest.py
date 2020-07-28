import json
from subprocess import run

from aiohttp import web
from aiohttp_wsgi import WSGIHandler
from prometheus_client import start_http_server, REGISTRY, make_wsgi_app
from prometheus_client.metrics_core import GaugeMetricFamily


class SpeedtestCollector:
    def describe(self):
        yield GaugeMetricFamily("speedtest_ping_jitter", "Ping jitter ms")
        yield GaugeMetricFamily("speedtest_ping_latency", "Ping latency ms")
        yield GaugeMetricFamily(
            "speedtest_download_bandwidth", "Download bandwidth (Mibps)"
        )
        yield GaugeMetricFamily(
            "speedtest_upload_bandwidth", "Upload bandwidth (Mibps)"
        )
        yield GaugeMetricFamily("speedtest_packetloss", "Packet Loss (%)")

    def collect(self):
        _output = run(["speedtest", "-b", "-f", "json"], capture_output=True)
        results = json.loads(_output.stdout)
        yield GaugeMetricFamily(
            "speedtest_ping_jitter", "Ping jitter (ms)", value=results["ping"]["jitter"]
        )
        yield GaugeMetricFamily(
            "speedtest_ping_latency",
            "Ping latency ms",
            value=results["ping"]["latency"],
        )
        yield GaugeMetricFamily(
            "speedtest_download_bandwidth",
            "Download bandwidth (Mibps)",
            value=results["download"]["bandwidth"],
        )
        yield GaugeMetricFamily(
            "speedtest_upload_bandwidth",
            "Upload bandwidth (Mibps)",
            value=results["upload"]["bandwidth"],
        )
        yield GaugeMetricFamily(
            "speedtest_packetloss", "Packet Loss (%)", value=results["packetLoss"]
        )


if __name__ == "__main__":
    REGISTRY.register(SpeedtestCollector())
    wsgi_app = make_wsgi_app()
    wsgi_handler = WSGIHandler(wsgi_app)
    app = web.Application()
    app.router.add_route("*", "/{path_info:.*}", wsgi_handler)
    web.run_app(app, port=9516)
