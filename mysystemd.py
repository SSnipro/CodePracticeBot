#!/usr/bin/env python3

try:
    import systemd.daemon
    from systemd import journal
    systemd_enable=True
except ImportError:
    systemd_enable=False

def ready():
    if systemd_enable:
        systemd.daemon.notify('READY=1')