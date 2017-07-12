# find this part in torrc file in etc
# and commentout ControlPort so that stem can use it. for controlling tor
## The port on which Tor will listen for local connections from Tor
## controller applications, as documented in control-spec.txt.
#ControlPort 9051


from stem import Signal
from stem.control import Controller

def switchIP():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
