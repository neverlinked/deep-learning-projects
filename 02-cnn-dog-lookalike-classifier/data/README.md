# Data

## Source

The Stanford Dogs Dataset.

* Main page: http://vision.stanford.edu/aditya86/ImageNetDogs/
* Paper: Khosla, Jayadevaprakash, Yao and Fei-Fei, *Novel Dataset for Fine-Grained Image
  Categorization*, First Workshop on Fine-Grained Visual Categorization, CVPR 2011.

20,580 photos of 120 dog breeds, with a bounding box around the dog in every photo. The photos
were taken from ImageNet. That matters for this project, because the pretrained networks I use
were also trained on ImageNet (see the limitations in the notebook).

## Download date

The date the files were downloaded is saved in `DOWNLOAD_DATE.txt`. To get the data again, run:

```bash
python scripts/download_stanford_dogs.py
```

The script downloads `images.tar` (about 750 MB) and `annotation.tar` (about 21 MB), extracts
them into this folder and deletes the tar files again. The photos themselves are not committed
to git.

## Folder layout after the download

| Path | What it is |
| --- | --- |
| `Images/n02085620-Chihuahua/*.jpg` | photos, one folder per breed |
| `Annotation/n02085620-Chihuahua/<photo id>` | XML file per photo with image size and bounding box(es) |
| `cache/` | files the notebook makes itself (embeddings, the 224 x 224 images of my 12 breeds). Safe to delete, the notebook rebuilds them. |
| `DOWNLOAD_DATE.txt` | when the download was made |

## Licence and terms

The dataset is meant for research and education. The photos belong to their original owners
(via ImageNet). See the dataset page above.
