import multiprocessing

bind = "127.0.0.1:8002"
workers = multiprocessing.cpu_count() * 1
pidfile = "/var/tmp/goout.pid"
