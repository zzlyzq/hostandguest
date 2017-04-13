#!/bin/sh

cat create.txt | while read line
do
	   echo $line
	      vmname=`echo $line | awk -F, '{print $1}'`
	         vmsize=`echo $line | awk -F, '{print $2}'`
		    /vmfs/volumes/datastore1/vmware-ovftool/ovftool -dm=thin -ds=datastore1 '--net:bridged=VM Network' "--name=$vmname" http://192.168.0.88:1280/ovf/${vmsize}.ovf 'vi://root:fOgLnr1D@192.168.0.216'
	    done
