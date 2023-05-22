import sys
import numpy as np
import pandas as pd
from pathlib import Path

def add_context(df, cpc_codes):
    df = pd.merge(df, cpc_codes[["context","title"]], on ="context", how = "left")
    df.drop('context', axis=1, inplace=True)
    df.rename(columns={"title": "context"}, inplace=True)
    return df


def train_val_split(df, val_prop=0.25):
    anchors = df.anchor.unique()
    np.random.shuffle(anchors)
    val_sz = int(len(anchors)*val_prop)
    val_anchors = anchors[:val_sz]

    is_val = np.isin(df.anchor, val_anchors)
    idxs = np.arange(len(df))
    val_idxs = idxs[ is_val]
    trn_idxs = idxs[~is_val]
    train_df, val_df = df.iloc[trn_idxs], df.iloc[val_idxs]
    return train_df, val_df


def split_data(input_path):
    path = input_path.parent()
    train_path = path/'train_df.csv'
    valid_path = path/'valid_df.csv'
    
    df = pd.read_csv(input_path)
    df.drop('id', axis=1, inplace=True)
    
    cpc_codes = pd.read_csv(path/"titles.csv")
    cpc_codes = cpc_codes.rename(columns = {"code" : "context"})
    df = add_context(df, cpc_codes)
    
    train_df, val_df = train_val_split(df)
    train_df.to_csv(path/'train_df.csv', index=False)
    val_df.to_csv(path/'val_df.csv', index=False)
    print(f"Train shape : {train_df.shape}, Valid shape : {val_df.shape}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the input file path as an argument.")
        sys.exit(1)
        
    input_path = Path(sys.argv[1])
    split_data(input_path)