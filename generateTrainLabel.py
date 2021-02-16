import os
import pickle
import numpy as np

# 将similar_pics 转换成pkl标签文档，供ImageRetrieval训练数据
if __name__ == '__main__':
    cids = []
    clusters = []
    qidxs = []
    pidxs = []
    class_num = 0
    dirs = 'data/train'
    for dir in os.listdir(dirs):
        # test1 = os.listdir(dirs)
        # print(dir)
        # test = os.listdir('/'.join([dirs,dir]))
        one_dir = '/'.join([dirs,dir])
        if os.path.isdir(one_dir):
            for qpimg in os.listdir(one_dir):
                # qpdir = '/'.join([one_dir,path])
                save_cid_path = '/'.join([dir,qpimg])
                cids.append(save_cid_path)
                clusters.append(class_num)
            class_num += 1

    print(cids)
    print(len(cids))

    print(clusters)
    print(len(clusters))

    for i in range(len(clusters)-1):
        if clusters[i]==clusters[i+1]:
            qidxs.append(i)
            pidxs.append(i+1)
    qidxs = np.array(qidxs,'uint16')
    pidxs = np.array(pidxs, 'uint16')
    print({'qidxs':qidxs})
    print({'pidxs':pidxs})

    data = {'train':{'cids':cids,'cluster':clusters,'qidxs':qidxs,'pidxs':pidxs}}
    print(data)
    with open("data/train/train.pkl", "wb") as f:
        pickle.dump(data, f)
