## Guideline

The image alignment problem has been placed under dir alignment/ and text classification has been placed under text_classification/ . You can find the notebook and output for each problem and the dir itself.

To install dependencies : `pip install -r requirements.txt`


## Comparision of Model Architecture

| S.N  | Model Architecture                                       | Avg Train Score | Avg Val Score | EPOCHS |
| ---- | -------------------------------------------------------- | --------------- | ------------- | ------ |
| 1    | 1 LSTM 64 cells, d =0.5 ,optimizer = RMSProp             | 86.0            | 88.9          | 25     |
| 2    | 1 Bidirectional LSTM 64 cells, d=0.5,optimizer = RMSProp | 86.0            | 88.4          | 25     |
| 3    | 1 LSTM 128 cells, d= 0.5,optimizer = RMSProp             | 86.0            | 88.7          | 25     |
| 4    | 1 LSTM 64 cells, d =0.3 ,optimizer = RMSProp             | 86.0            | 88.48         | 25     |
| 5    | 1 LSTM 64 cells, d =0.5,optimizer = Adam                 | 87.66           | 89.19         | 25     |
| 6    | 1 LSTM 64 cells, d =0.3,optimizer = Adam                 | 87.38           | 88.57         | 25     |
| 7    | 1 LSTM 64 cells, d =0.3,optimizer = Adam                 | 87.23           | 88.96         | 50     |
| 8    | 1 Bidirectional LSTM 64 cells, d=0.3,optimizer = Adam    | 89.81           | 89.47         | 50     |
| 9    | 1 Bidirectional LSTM 128 cells,Conv1D,Pooling            | 89.40           | 90.29         | 50     |



