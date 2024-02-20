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

- This is the git repo for CMPE 257 Machine Learning Course.

### Resources
---
- [Project Proposal Doc](https://docs.google.com/document/d/1g0QzqaCswfreFEjupCt6V5stKHfmYMRoKg1mxsk5PwQ)
- Dataset [U.S. Patent Phrase to Phrase Matching](https://www.kaggle.com/competitions/us-patent-phrase-to-phrase-matching)
- https://www.kaggle.com/code/jhoward/getting-started-with-nlp-for-absolute-beginners
- https://www.kaggle.com/code/jhoward/iterate-like-a-grandmaster
- https://github.com/shahrukhx01/siamese-nn-semantic-text-similarity
- Cross Attention[Paper](https://arxiv.org/pdf/1603.07810.pdf) and [Code](https://github.com/andreasveit/conditional-similarity-networks)
