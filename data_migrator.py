#!/usr/bin/env python

import os
import shutil

# dir_path = '/Users/hesam/AFRICA'
# bigList = os.listdir(dir_path)
# source = "/Users/hesam/AFRICA/{netwrok_name}/{file_name}"
# destin = "/Users/hesam/test/db_test/NETWORKS/{dest_dir}/{netwrok_name}_{file_name}"
#
# for net in bigList:
#     if net != "SCRIPTS" and net != ".DS_Store":
#         shutil.copy(
#             source.format(netwrok_name = net, file_name = "sta_evt_predTT.out")
#             ,
#             destin.format(dest_dir='STATIONS',netwrok_name = net, file_name = "sta_evt_predTT.out")
#         )
#         shutil.copy(
#             source.format(netwrok_name = net, file_name = "events.txt")
#             ,
#             destin.format(dest_dir='EVENTS',netwrok_name = net, file_name = "events.txt")
#         )


dir_path = '/Users/hesam/test/db_test/NETWORKS/EVT_WNUM/'
bigList = os.listdir(dir_path)
destin = "/Users/hesam/AFRICA/{netwrok_name}/events_wNums.txt"

for f in bigList:
    network_code = f.split('_')[0]
    shutil.copy(dir_path+f, destin.format(netwrok_name=network_code))

    # print(dir_path+f)
