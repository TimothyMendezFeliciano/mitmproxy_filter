import asyncio
from mitmproxy import http, options
from mitmproxy.tools.dump import DumpMaster

# import logging

# Configure logging
# logging.basicConfig(filename="blocked_requests.log", level=logging.INFO, format="%(asctime)s - %(message)s")


# List of adult domains to block
BLOCKED_DOMAINS = [
    "pornhub.com", "xvideos.com", "redtube.com", "xnxx.com", "xxx.com",
    "sex.com", "adultfriendfinder.com", "hentaikey.com", "brazzers.com", "onlyfans.com",
    "youporn.com", "porn.com", "fuq.com", "porn300.com", "xhamster", "fanfix.com", "superporn.com",
    "serviporno.com", "xvideos2.com", "bellesa.co", "xxxi.porn"
]

# List of WhatsApp domains to allow
WHITELISTED_DOMAINS = [
    "mmg.whatsapp.net",
    "media.whatsapp.net",
    "static.whatsapp.net",
    "web.whatsapp.com",
    "www.google.com",
    "ssl.gstatic.com",
    "beacons.gcp.gvt2.com",
    "mtalk.google.com",
    "clientservices.googleapis.com",
]


class BlockAdultSites:
    def request(self, flow: http.HTTPFlow) -> None:
        # Intercept requests and block adult sites

        for allowed_domain in WHITELISTED_DOMAINS:
            if allowed_domain in flow.request.pretty_url:
                return

        for domain in BLOCKED_DOMAINS:
            if domain in flow.request.pretty_url:
                # logging.info(f"Blocked: {flow.request.pretty_url}")
                flow.response = http.Response.make(
                    403,  # Http Status Code - Forbidden
                    b"Blocked by mitmproxy",
                    {"Content-Type": "text/plain"}
                )


class MitmProxyRunner:
    def __init__(self):
        self.options = options.Options(
            listen_host="127.0.0.1",
            listen_port=9090,
            mode=["regular"]
        )

        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        self.master = DumpMaster(self.options, loop=self.loop)
        # self.master.addons.add(core.Core())
        self.master.addons.add(BlockAdultSites())

    def run(self):
        print("Starting mitmproxy in transparent mode...")
        try:
            self.loop.run_until_complete(self.master.run())
        except KeyboardInterrupt:
            print("Shutting down mitmproxy...")
            self.loop.run_until_complete(self.master.shutdown())
        finally:
            self.loop.close()


if __name__ == "__main__":
    proxy = MitmProxyRunner()
    proxy.run()
