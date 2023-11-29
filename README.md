# RGB Footprint Extractor

Welcome to the RGB Footprint Extractor repository! This tool is designed to extract building footprints from RGB satellite imagery using pre-trained deep learning models. Below, you'll find instructions on how to set up and use the tool.


Our team CSV provides you with 3 pre-trained models to use. Let's go!
## Setup

Clone the repository:

```bash
git clone 

```

## Navigate to the project directory:

```bash
cd rgb-footprint-extract

```

## Install the required dependencies:

```bash
pip install -r requirements.txt

```
## Datasets

#### Downloading the Datasets
1. To download the AICrowd dataset, please go [here](https://www.aicrowd.com/challenges/mapping-challenge-old). You will have to either create an account or sign in to access the training and validation set. Please store the training/validation set inside `<root>/AICrowd/<train | val>` for ease of conversion.
2. To download the Urban3D dataset, please run:
```setup
aws s3 cp --recursive s3://spacenet-dataset/Hosted-Datasets/Urban_3D_Challenge/01-Provisional_Train/ <root>/Urban3D/train
aws s3 cp --recursive s3://spacenet-dataset/Hosted-Datasets/Urban_3D_Challenge/02-Provisional_Test/ <root>/Urban3D/test
``` 
3. To download the SpaceNet Vegas dataset, please run:
```setup
aws s3 cp s3://spacenet-dataset/spacenet/SN2_buildings/tarballs/SN2_buildings_train_AOI_2_Vegas.tar.gz <root>/SpaceNet/Vegas/
aws s3 cp s3://spacenet-dataset/spacenet/SN2_buildings/tarballs/AOI_2_Vegas_Test_public.tar.gz <root>/SpaceNet/Vegas/

tar xvf <root>/SpaceNet/Vegas/SN2_buildings_train_AOI_2_Vegas.tar.gz
tar xvf <root>/SpaceNet/Vegas/AOI_2_Vegas_Test_public.tar.gz
```


## Images

If you want to use a directory of images, convert them to the .npy format using the script images_dir.py. Specify the path to the image directory in the script.


```bash
  python images_dir.py
```

If you prefer using a single image, specify the image path in the images.py script and run it:

```bash
  python images.py
```
## Training and Evaluation
To train / evaluate the DeepLabV3+ models described in the paper, please use `train_deeplab.sh` or `test_deeplab.sh` for your convenience. We employ the following primary command-line arguments:

| Parameter                 | Default       | Description (final argument)  |	
| :------------------------ |:-------------:| :-------------|
| --backbone 	    |	`resnet`         | The DeeplabV3+ backbone **(final method used `drn_c42`)**
| --out-stride | 16 | The backbone compression facter **(8)**
| --dataset | `urban3d` | The dataset to train / evaluate on (other choices: `spaceNet`, `crowdAI`, `combined`)
| --data-root | `/data/` | **Please replace this with the root folder of the dataset samples**
| --workers | 2 | Number of workers for dataset retrieval
| --loss-type | `ce_dice` | Type of objective function. Use `wce_dice` for exponentially weighted boundary loss
| --fbeta | 1 | The beta value to use with the F-Beta Measure  **(0.5)**
| --dropout | `0.1 0.5` | Dropout values to use in the DeepLabV3+ **(0.3 0.5)**
|--epochs | None | Number of epochs to train **(60 for train, 1 for test)**
| --batch-size| None | Batch size **(3/4)**
| --test-batch-size| None | Testing Batch Size **(1/4)**
| --lr | `1e-4` | Learning Rate **(`1e-3`)**
| --weight-decay | `5e-4` | L2 Regularization Constant **(`1e-4`)**
| --gpu-ids | `0` | GPU Ids (Use `--no-cuda` for only CPU)
| --checkname | None | Experiment name
| --use-wandb | False | Track experiment using WandB
| --resume | None | Experiment name to load weights from (i.e. `urban` for `weights/urban/checkpoint.pth.tar`)
| --evalulate | False | **Enable this flag for testing**
| --best-miou | False | **Enable this flag to get best results when testing**
| --incl-bounds | False | **Enable this flag when training with `wce_dice` as a loss**

To train with the cross-task training strategy, you need to:
1. Train a model using `--dataset=combined` until the best loss has been achieved
2. Train a model using `--resume=<checkname>` on one of the three primary datasets until the best mIoU is achieved


## Models run

If you have converted the images and are ready to run the model, then you need to select the model and then run the commented script in the console (we recommend spaceNet)


```bash
  python spaceNet run.py
```

```bash
  python crowdAI run.py
```

```bash
  python urban3d run.py
```
## Screenshots

This is what you should get❤️

![model visualization](Buildings_segmentation/rgb-footprint-extract/ready images/output1.png)

## Metrics

Explore and customize the evaluation metrics in the following files:

### F1 Score Metric:
```bash
  python metric_f1.py
```
### Pixel Accuracy Metric:
```bash
  python metric_pixel_accuracy.py
```
## Python Version

This project is developed using Python 3.10.13.

Feel free to explore, modify, and contribute to the repository.

Happy coding!
## Authors

- Ivan Karpov
- Irina Minkina
- Semyon Pleskunin
- Diana Bagotskaya
- Pavel Degtyarev