from channels.routing import route


channel_routing = [
    route("http.request", "processes.consumers.http_consumer"),
]
