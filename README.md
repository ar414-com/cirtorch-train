# Cirtorch Train

> from [filipradenovic/cnnimageretrieval-pytorch](https://github.com/filipradenovic/cnnimageretrieval-pytorch)




## Usage
### Init project
```bash
$ git clone https://github.com/ar414-com/cirtorch-train
```

### Prepare training data
```
project  
│
└───data
│   │
│   └───train
│       │   qp_0
│       │   │   q0.png
│       │   │   ...
│       │   qp_1
│       │   │   q0.png
│       │   │   ...
│       │   ...
│   
```

### Generate train label
> export path: data/train/train.pkl
```bash
$ python -m generateTrainLabel
```

### Run train
> export path: networks/

**Note**: Just download `imagenet-caffe-resnet101-features-10a101d.pth`, Removed the test process, please ignore the operation to show that downloading test data failed
```bash
$ python -m cirtorch.examples.train --no-val ./networks 
```
