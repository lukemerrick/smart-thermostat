import network

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

ap_if.active(False)
sta_if.active(True)
sta_if.connect("<ssid>", "<psk>")
