import usb.core
import usb.util
import sys
import label



# In Linux, you must:
#
# 1) Add your user to the Linux group "lp" (line printer), otherwise you will
#    get a user permissions error when trying to print.
#
# 2) Add a udev rule to allow all users to use this USB device, otherwise you
#    will get a permissions error also. Example:
#
#    In /etc/udev/rules.d create a file ending in .rules, such as
#    33-receipt-printer.rules with the contents:
#
#   # Set permissions to let anyone use the thermal receipt printer
#   SUBSYSTEM=="usb", ATTR{idVendor}=="0416", ATTR{idProduct}=="5011", MODE="666"
#
# Find our device  command usb-devices 
# 0416:5011 is POS58 USB thermal receipt printer
dev = usb.core.find(idVendor=0x0416, idProduct=0x5011)

# Was it found?
if dev is None:
    raise ValueError('Impressora não localizada')

# Disconnect it from kernel
needs_reattach = False
if dev.is_kernel_driver_active(0):
    needs_reattach = True
    dev.detach_kernel_driver(0)

# Set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None

etiq = label.label()
ep.write(etiq)

# Reattach if it was attached originally
dev.reset()
if needs_reattach:
    dev.attach_kernel_driver(0)
    print("Dispositivo USB reconectado ao driver do kernel")