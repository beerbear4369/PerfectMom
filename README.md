# PerfectMom
The raw text dialog data was not include due to sensitive personal info. Only encoded data are upload here

# Text preprocessing
1. Connect iphone to PC, use the wxbackup_2.0_win to extract wechat history into text file
2. Run the preprocessing scripty to process the dialog data to desired conversation pairs

```
python txtpreprocessing.py
```
# Sentiment analysis
1. Make sure the preprocessed text in data folder
2. Run  snownlp_sentimentanalysis to generate positive dialog subfile
```
python snownlp_sentimentanalysis.py
```
3. Run  text analysis.ipynb to generate wordfeature and sentiment histogram

# Text-Generation

## 1. LSTM2LSTM Model
Run the LSTM2LSTM.ipynb to train a model from scratch, make sure mount the google drive correctly.

## 2. Bert2Bert Model
Run the BERT2BERT.ipynb to train a model with hugging face's transformers library.
Bert-base-chinese base 12 is used here.

## 3. GPT2-Chinese Model

1. Preprocessing the data to GPT2-Chinese acceptable format
```
import pandas as pd
import numpy
# Load the dataset into a pandas dataframe.
df_mom = pd.read_csv("/content/drive/MyDrive/iss/NLP/perfectmom/data/dialog_mom", header=0, names=['index','mom_sentence','sentiment','sentiment_score'])
df_son = pd.read_csv("/content/drive/MyDrive/iss/NLP/perfectmom/data/dialog_son", header=0, names=['index','son_sentence','sentiment','sentiment_score'])

# Display the first 10 rows from the data.

son =df_son["son_sentence"]
mom  = df_mom["mom_sentence"]
df_son["son_sentence"][0]

# open('/data/gpt2data.txt','create',encoding='utf-8')

for ind in son.index:
  print(ind)
  with open('/content/drive/MyDrive/iss/NLP/perfectmom/data/gpt2data.txt','a',encoding='utf-8') as f:
      f.write(df_son["son_sentence"][ind])
      f.write(df_mom["mom_sentence"][ind])
      f.write('\n')
```
2. save as train.txt and save under 'GPT2-chitchat\data' directory
3. pre process the data into pickle
```
python preprocess.py --train_path data/train.txt --save_path data/train.pkl
```
4. use pretrained model to interference the talk dialog
```
python interact.py --no_cuda --model_path model/epoch40
```
5. finetuning pretrained model with your data
```
python train.py --epochs 40 --batch_size 8 --device 0,1 --train_path data/train.pkl
```

# Reference
- [Unilmchatchitrobot](https://github.com/liucongg/UnilmChatchitRobot)
- [GPT2-Chinese](https://github.com/Morizeyao/GPT2-Chinese)
- [transformers](https://github.com/huggingface/transformers)
- [GPT2-chitchat](https://github.com/yangjianxin1/GPT2-chitchat)
- https://towardsdatascience.com/intuitive-understanding-and-step-by-step-implementation-of-sequence-to-sequence-model-with-86be00ebe0fd
