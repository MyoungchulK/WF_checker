import numpy as np
import re

def data_info_reader(d_path_str):

    # it must be start with /data/exp/ARA/.....
    # these informations might can salvage from root file itself in future...

    # salvage just number
    d_path = re.sub("\D", "", d_path_str) 

    # year
    yr = int(d_path[:4])
    if yr == 2013:

        # station 
        st = int(d_path[7:9])

        # run 
        run = int(re.sub("\D", "", d_path_str[-11:]))

        # config
        config = config_checker(st, run)

        # month and data
        md = 'Unknown'

        print(f'data info. 1)station:{st} 2)year:{yr} 3)mm/dd:{md} 4)run:{run} 5)config:{config}')

    else:

        # station
        st = int(d_path[5:7])

        # run
        run = int(d_path[-6:])

        # config
        config = config_checker(st, run)

        # month and data
        md = str(d_path[7:11])

        print(f'data info. 1)station:{st} 2)year:{yr} 3)mm/dd:{md} 4)run:{run} 5)config:{config}')

    return st, run, config, yr, md

def config_checker(st, runNum):

    # from Brian: https://github.com/clark2668/a23_analysis_tools/blob/master/tools_Cuts.h

    # default. unknown
    config=0

    # by statation
    if st == 2:
        if runNum>=0 and runNum<=4:
            config=1
        elif runNum>=11 and runNum<=60:
            config=4
        elif runNum>=120 and runNum<=2274:
            config=2
        elif runNum>=2275 and runNum<=3463:
            config=1
        elif runNum>=3465 and runNum<=4027:
            config=3
        elif runNum>=4029 and runNum<=6481:
            config=4
        elif runNum>=6500 and runNum<=8097:
            config=5
        elif runNum>=8100 and runNum<=8246:
            config=4
        else:
            pass

    elif st == 3:
        if runNum>=0 and runNum<=4:
            config=1
        elif runNum>=470 and runNum<=1448:
            config=2
        elif runNum>=1449 and runNum<=1901:
            config=1
        elif runNum>=1902 and runNum<=3103:
            config=5
        elif runNum>=3104 and runNum<=6004:
            config=3
        elif runNum>=6005 and runNum<=7653:
            config=4
        elif runNum>=7658 and runNum<=7808:
            config=3
        else:
            pass

    elif st == 5:
        pass

    return config

