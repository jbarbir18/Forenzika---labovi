import re
import datetime

log_path='setupapi.dev2.log'
usb_devices={
    'device_vendor_id':[],
    'device_product_id':[],
    'device_instance_id':[],
    'event_time':[]
}
usb_regex=r'^>>>  \[Device Install.*#(Disk&Ven_[A-Za-z0-9]+)&(Prod_([\w\s\S]+?))&(Rev_([\w\s\S]+?))#([\w\s\S]+?)#.*\]'
# Read the contents of the setupapi.dev.log file
with open(log_path, "r") as log_file:
     # Store information about each USB device in a dictionary
     for line in log_file:
        # Find all USB device installation events and extract information about each device
        line_text=next(log_file)
        matched_object=re.search(usb_regex,line)
        if(matched_object!=None):
            event_time=line_text.split("start ")[1].strip()
            usb_devices["device_vendor_id"].append(matched_object.groups()[0])
            usb_devices["device_product_id"].append(matched_object.groups()[1])
            usb_devices["device_instance_id"].append(matched_object.groups()[2])
            usb_devices["event_time"].append(event_time)

print(f"Printing \n {usb_devices['device_vendor_id']} \n {usb_devices['device_product_id']} \n {usb_devices['device_instance_id']} \n {usb_devices['event_time']}")