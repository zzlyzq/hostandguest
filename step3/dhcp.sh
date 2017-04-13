#!/bin/sh
echo '' > /tmp/dhcp.txt
vim-cmd vmsvc/getallvms | grep vmx > /tmp/vmx.txt
cat /tmp/vmx.txt | while read line
do
  vmid=`echo $line | awk '{print $1}'`
  vmname=`echo $line | awk '{print $2}'`
  vmip=`echo $vmname | awk -F\- '{print $NF}'`
  vmip=`echo $vmip | awk -FP '{print "192.168.0."$NF}'`
  vmmac=`vim-cmd vmsvc/device.getdevices $vmid | grep macAddress | awk -F\" '{print $2}'`
  echo "$vmid $vmname $vmip $vmmac"
  echo "dhcp-host=$vmmac,$vmip" >> /tmp/dhcp.txt
done
                  
cat /tmp/dhcp.txt

