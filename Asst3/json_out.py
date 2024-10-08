import subprocess
import json
import time
import os

ROUND=2
time_s=3
txqlen=[50,100,200,400,800,1000,1500,2000,2500,3000,3500,4000]
#txqlen=[1,5,10,20,30,40,50,100,200,300,400,600,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
expo=f"test_{time_s}"
sleeptime=1
proto="tcp"
_out=f"{expo}_{proto}"
# 定义iperf3命令
for txql in txqlen:
    
    #set the quenelen
    try:
            #set qlen
            cmd_qlen=f"ethtool -G ens33 tx {txql} "
            cmd_qlen_result = subprocess.run(cmd_qlen, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if cmd_qlen_result:
                pass
            else:
                print(cmd_qlen_result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing iperf3: {e}")
        print(e.stderr)
        exit(1)

    time.sleep(sleeptime)
    print(f"After setting : ||  {cmd_qlen}  ||, we slept for 5 seconds...")

    for r in range(ROUND):

        try:
            #restart the network service
            cmd_restart_net="/etc/init.d/networking restart"
            restart_result = subprocess.run(cmd_restart_net,  shell=True,check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if restart_result:
                pass
            else:
                print(restart_result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error executing iperf3: {e}")
            print(e.stderr)
            exit(1)

        time.sleep(sleeptime)
        print(f"After Restarting : ||  {cmd_restart_net}  ||, we slept for 5 seconds...")

        #get the througput and time json
        try:
            command = ["iperf3", "-c", "10.68.75.53", "-t", str(time_s), "-J", "-i", "0.1"]
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output = result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error executing iperf3: {e}")
            print(e.stderr)
            exit(1)

        #save the data
        try:
            data = json.loads(output)
        except json.JSONDecodeError:
            print("Failed to decode the output as JSON.")
            exit(1)

        # 保存输出到JSON文件
        if not os.path.exists(_out):
            # 路径不存在，创建文件夹
            os.makedirs(_out)
        test_out=f"{_out}/output_txql_{txql}_r_{r}.json"
        with open(test_out, "w") as file:
            json.dump(data, file, indent=4)

        print(f"The output has been saved to {test_out}.")
    
