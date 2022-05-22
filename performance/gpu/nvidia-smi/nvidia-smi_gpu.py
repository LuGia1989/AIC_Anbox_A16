import sys
import pandas as pd


f=sys.argv[1]


def gpu0_utilization(f):
    something = []
    mylines = []
    utils_all = []
    utils = []
    tempC = []
    gpuMemoryUtils = []
    powerConsumption = []
    with open(f, 'r+') as myfile:
        for line in myfile:
            mylines.append(line.rstrip('\n'))
    for idx, word in enumerate(mylines):
        index = word.find('0  NVIDIA A16')
        if index != -1:
            something.append(mylines[idx + 1])
    for i in something:
        utils_all.append(i.rstrip().split())
    for i in range(59):
        gpuMemoryUtils.append((int(utils_all[i][8].rstrip('MiB'))/15867)*100)


    #df_utils = pd.DataFrame(utils).astype('int')
    #ave_utils = float(df_utils.mean())
    #min_utils = float(df_utils.min())
    #max_utils = float(df_utils.max())
    #std_utils = float(df_utils.std())

    #df_tempC  = pd.DataFrame(tempC).astype('int')
    #ave_tempC = float(df_tempC.mean())
    #min_tempC = float(df_tempC.min())
    #max_tempC = float(df_tempC.max())
    #std_tempC = float(df_tempC.std())

    df_gpuMemoryUtils  = pd.DataFrame(gpuMemoryUtils).astype('float')
    ave_gpuMemoryUtils = float(df_gpuMemoryUtils.mean())
    min_gpuMemoryUtils = float(df_gpuMemoryUtils.min())
    max_gpuMemoryUtils = float(df_gpuMemoryUtils.max())
    std_gpuMemoryUtils = float(df_gpuMemoryUtils.std())


    #df_powerConsumption  = pd.DataFrame(powerConsumption).astype('int')
    #ave_powerConsumption = float(df_powerConsumption.mean())
    #min_powerConsumption = float(df_powerConsumption.min())
    #max_powerConsumption = float(df_powerConsumption.max())
    #std_powerConsumption = float(df_powerConsumption.std())

        
    return min_gpuMemoryUtils, ave_gpuMemoryUtils, max_gpuMemoryUtils, std_gpuMemoryUtils

def gpu1_utilization(f):
    something = []
    mylines = []
    utils_all = []
    utils = []
    tempC = []
    gpuMemoryUtils = []
    powerConsumption = []
    with open(f, 'r+') as myfile:
        for line in myfile:
            mylines.append(line.rstrip('\n'))
    for idx, word in enumerate(mylines):
        index = word.find('1  NVIDIA A16')
        if index != -1:
            something.append(mylines[idx + 1])
    for i in something:
        utils_all.append(i.rstrip().split())
    for i in range(59):
        #utils.append(utils_all[i][12].rstrip('%'))
        #tempC.append(utils_all[i][2].rstrip('C'))
        gpuMemoryUtils.append((int(utils_all[i][8].rstrip('MiB'))/15867)*100)
        #powerConsumption.append(utils_all[i][4].rstrip('W'))


    #df_utils = pd.DataFrame(utils).astype('int')
    #ave_utils = float(df_utils.mean())
    #min_utils = float(df_utils.min())
    #max_utils = float(df_utils.max())
    #std_utils = float(df_utils.std())

    #df_tempC  = pd.DataFrame(tempC).astype('int')
    #ave_tempC = float(df_tempC.mean())
    #min_tempC = float(df_tempC.min())
    #max_tempC = float(df_tempC.max())
    #std_tempC = float(df_tempC.std())

    df_gpuMemoryUtils  = pd.DataFrame(gpuMemoryUtils).astype('float')
    ave_gpuMemoryUtils = float(df_gpuMemoryUtils.mean())
    min_gpuMemoryUtils = float(df_gpuMemoryUtils.min())
    max_gpuMemoryUtils = float(df_gpuMemoryUtils.max())
    std_gpuMemoryUtils = float(df_gpuMemoryUtils.std())


    #df_powerConsumption  = pd.DataFrame(powerConsumption).astype('int')
    #ave_powerConsumption = float(df_powerConsumption.mean())
    #min_powerConsumption = float(df_powerConsumption.min())
    #max_powerConsumption = float(df_powerConsumption.max())
    #std_powerConsumption = float(df_powerConsumption.std())

        
    return min_gpuMemoryUtils, ave_gpuMemoryUtils, max_gpuMemoryUtils, std_gpuMemoryUtils 


def gpu2_utilization(f):
    something = []
    mylines = []
    utils_all = []
    utils = []
    tempC = []
    gpuMemoryUtils = []
    powerConsumption = []
    with open(f, 'r+') as myfile:
        for line in myfile:
            mylines.append(line.rstrip('\n'))
    for idx, word in enumerate(mylines):
        index = word.find('2  NVIDIA A16')
        if index != -1:
            something.append(mylines[idx + 1])
    for i in something:
        utils_all.append(i.rstrip().split())
    for i in range(59):
        #utils.append(utils_all[i][12].rstrip('%'))
        #tempC.append(utils_all[i][2].rstrip('C'))
        gpuMemoryUtils.append((int(utils_all[i][8].rstrip('MiB'))/15867)*100)
        #powerConsumption.append(utils_all[i][4].rstrip('W'))

    df_gpuMemoryUtils  = pd.DataFrame(gpuMemoryUtils).astype('float')
    ave_gpuMemoryUtils = float(df_gpuMemoryUtils.mean())
    min_gpuMemoryUtils = float(df_gpuMemoryUtils.min())
    max_gpuMemoryUtils = float(df_gpuMemoryUtils.max())
    std_gpuMemoryUtils = float(df_gpuMemoryUtils.std())

   
    return min_gpuMemoryUtils, ave_gpuMemoryUtils, max_gpuMemoryUtils, std_gpuMemoryUtils



def gpu3_utilization(f):
    something = []
    mylines = []
    utils_all = []
    utils = []
    tempC = []
    gpuMemoryUtils = []
    powerConsumption = []
    with open(f, 'r+') as myfile:
        for line in myfile:
            mylines.append(line.rstrip('\n'))
    for idx, word in enumerate(mylines):
        index = word.find('3  NVIDIA A16')
        if index != -1:
            something.append(mylines[idx + 1])
    for i in something:
        utils_all.append(i.rstrip().split())
    for i in range(59):
        #utils.append(utils_all[i][12].rstrip('%'))
        #tempC.append(utils_all[i][2].rstrip('C'))
        gpuMemoryUtils.append((int(utils_all[i][8].rstrip('MiB'))/15867)*100)
        #powerConsumption.append(utils_all[i][4].rstrip('W'))

    df_gpuMemoryUtils  = pd.DataFrame(gpuMemoryUtils).astype('float')
    ave_gpuMemoryUtils = float(df_gpuMemoryUtils.mean())
    min_gpuMemoryUtils = float(df_gpuMemoryUtils.min())
    max_gpuMemoryUtils = float(df_gpuMemoryUtils.max())
    std_gpuMemoryUtils = float(df_gpuMemoryUtils.std())

   
    return min_gpuMemoryUtils, ave_gpuMemoryUtils, max_gpuMemoryUtils, std_gpuMemoryUtils


def main():
    min_gpuMemoryUtils0, ave_gpuMemoryUtils0, max_gpuMemoryUtils0, std_gpuMemoryUtils0 = gpu0_utilization(f)
    min_gpuMemoryUtils1, ave_gpuMemoryUtils1, max_gpuMemoryUtils1, std_gpuMemoryUtils1 = gpu1_utilization(f)
    min_gpuMemoryUtils2, ave_gpuMemoryUtils2, max_gpuMemoryUtils2, std_gpuMemoryUtils2 = gpu2_utilization(f)
    min_gpuMemoryUtils3, ave_gpuMemoryUtils3, max_gpuMemoryUtils3, std_gpuMemoryUtils3 = gpu3_utilization(f)


    print('#################################################')
    print('GPU0 MEMORY UTILIZATION')
    print('Min gpu memory utilization     = ' + '{:.1f}'.format(min_gpuMemoryUtils0) + '%')
    print('Average gpu memory utilization = ' + '{:.1f}'.format(ave_gpuMemoryUtils0) + '%')
    print('Max gpu memory utilization     = ' + '{:.1f}'.format(max_gpuMemoryUtils0) + '%')
    print('Std gpu memory utilization     = ' + '{:.1f}'.format(std_gpuMemoryUtils0) + '%')
    print('\n')

    print('GPU1 MEMORY UTILIZATION')
    print('Min gpu memory utilization     = ' + '{:.1f}'.format(min_gpuMemoryUtils1) + '%')
    print('Average gpu memory utilization = ' + '{:.1f}'.format(ave_gpuMemoryUtils1) + '%')
    print('Max gpu memory utilization     = ' + '{:.1f}'.format(max_gpuMemoryUtils1) + '%')
    print('Std gpu memory utilization     = ' + '{:.1f}'.format(std_gpuMemoryUtils1) + '%')
    print('\n')
  
    print('GPU2 MEMORY UTILIZATION')
    print('Min gpu memory utilization     = ' + '{:.1f}'.format(min_gpuMemoryUtils2) + '%')
    print('Average gpu memory utilization = ' + '{:.1f}'.format(ave_gpuMemoryUtils2) + '%')
    print('Max gpu memory utilization     = ' + '{:.1f}'.format(max_gpuMemoryUtils2) + '%')
    print('Std gpu memory utilization     = ' + '{:.1f}'.format(std_gpuMemoryUtils2) + '%')
    print('\n')

    print('GPU3 MEMORY UTILIZATION')
    print('Min gpu memory utilization     = ' + '{:.1f}'.format(min_gpuMemoryUtils3) + '%')
    print('Average gpu memory utilization = ' + '{:.1f}'.format(ave_gpuMemoryUtils3) + '%')
    print('Max gpu memory utilization     = ' + '{:.1f}'.format(max_gpuMemoryUtils3) + '%')
    print('Std gpu memory utilization     = ' + '{:.1f}'.format(std_gpuMemoryUtils3) + '%')
    print('#################################################')
    print('Average GPU memory utilization = ' + '{:.1f}'.format((float(ave_gpuMemoryUtils0) + float(ave_gpuMemoryUtils1) + \
                                                                 float(ave_gpuMemoryUtils2) + float(ave_gpuMemoryUtils3))/4) + '%')
    print('Std GPU memory utilization = ' + '{:.1f}'.format((float(std_gpuMemoryUtils0) + float(std_gpuMemoryUtils1) + \
                                                                             float(std_gpuMemoryUtils2) + float(std_gpuMemoryUtils3))/4) + '%')


if __name__ == '__main__':
    main()
