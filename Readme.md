# Contenxt Aware Semantic Similarity

This GitHub repo is part of 257 final project. It has all the code implementation and other helper scripts.

## Preparing Data
We used the [US patent phrase to phrase matching]( https://www.kaggle.com/competitions/us-patent-phrase-to-phrase-matching) dataset from Kaggle, also download the [titles file](https://www.kaggle.com/datasets/xhlulu/cpc-codes) which contain the title text for each section. Run the following script to prepare the train and validation set.

```python
python prepare_data.py data/train.csv
```

## Implementation

- [Cross Encoder](./cross_encoder_HF.ipynb)
- [Bi Encoder](./bi_encoder_ST.ipynb)