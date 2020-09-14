#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

author: whiteP

modified time: 2020/9/6 18:57

"""

"""Send a reply from the proxy without sending any data to the remote server."""
from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if "json" in flow.request.pretty_url:
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            b"Hello World",  # (optional) content
            {"Content-Type": "application/json"}  # (optional) headers
        )
