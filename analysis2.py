#!/usr/bin/env python
#coding:utf-8

import json



mental_server_type = {
    'cpu': 42,
    'mem': 200
}

# target，初始化一百台服务器
machines = []
for i in range(50):
    a = {}
    a['cpuused'] = 0
    a['memused'] = 0
    a['yw'] = []
    a['yw2'] = []
    machines.append(a)

# IP地址编号


def main():
    with open("./info2.txt") as f:
        ip_bianhao = 10
        for line in f:
            #print line
            info = line.replace("\r", "").replace("\n", "").split(",")
            yw_name = info[0]
            yw_instance_type = info[2]
            yw_instance_count = int(info[1])
            instance_used_cpu = int(yw_instance_type.split(".")[0])
            instance_used_mem = int(yw_instance_type.split(".")[1])
            instance_used_disk = int(yw_instance_type.split(".")[2])
            for number in range(0,yw_instance_count):
                guest_name = yw_name + "+" + str(instance_used_cpu) +"." + str(instance_used_mem)+"."+ str(instance_used_disk)
                for machine in machines:
                    if machine['cpuused'] + instance_used_cpu < mental_server_type['cpu'] and machine['memused'] + instance_used_mem < mental_server_type['mem'] and guest_name not in machine['yw']:
                        machine['yw'].append(guest_name )
                        machine['yw2'].append(guest_name + "+" +str(ip_bianhao) )
                        ip_bianhao = ip_bianhao + 1
                        machine['cpuused'] += instance_used_cpu
                        machine['memused'] += instance_used_mem
                        break


main()

# 直接打印
print "*"*60
for machine in machines:
    if machine['memused'] !=0:
        print machine

# 详细打印
print "*"*60
cpu_used_total = 0
mem_used_total = 0
instance_total = 0
for machine in machines:
    if machine['memused'] !=0:
        cpu_used_total += machine['cpuused']
        mem_used_total += machine['memused']
        instance_total += 1
print """一共消耗cpu: %s， mem: %s， instnaces: %s"""%(cpu_used_total,mem_used_total,instance_total)

# 直接打印
print "*"*60
i = 1
for machine in machines:
    if machine['memused'] !=0:
        print "-"*30 + "打印第%s服务器的虚拟机列表"%i + "-"*30
        for item in machine['yw2']:
            #print item
            item2 = item.split("+")
            result = "%s-IP%s,%s"%(item2[0],item2[2],item2[1])
            print result
        i += 1
