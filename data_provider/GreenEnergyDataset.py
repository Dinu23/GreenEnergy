import os
import numpy as np
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import StandardScaler
from utils.timefeatures import time_features
import pandas as pd

from utils.weights import compute_weights, load_weights


class GreenEnergyDataSet(Dataset):
    def __init__(self, root_path, flag='train', size=None,
                data_path='green.csv',external_path='weather.csv',
                scale=True, external_var = [], freq='h',use_weights=True, load_weights = True, weights_path=""):
        # size [seq_len, label_len, pred_len]
        # info
        print(size)
        if size == None:
            self.seq_len = 24 * 4 * 4
            self.label_len = 24 * 4
            self.pred_len = 24 * 4
        else:
            self.seq_len = size[0]
            self.label_len = size[1]
            self.pred_len = size[2]
        
        # init
        assert flag in ['train', 'test', 'val']
        type_map = {'train': 0, 'val': 1, 'test': 2}
        self.set_type = type_map[flag]

        self.scale = scale
        # self.timeenc = timeenc
        self.freq = freq

        self.root_path = root_path
        self.data_path = data_path
        self.external_path = external_path
        self.external_var = external_var
        if("time" not in external_var ):
            self.external_var.append("time")
        self.use_weights= use_weights
        self.load_weights = load_weights
        self.weights_path = weights_path
        self.__read_data__()

    def __read_data__(self):
        self.scaler = StandardScaler()
        df_green_raw = pd.read_csv(os.path.join(self.root_path,
                                          self.data_path))
        df_weather_raw = pd.read_csv(os.path.join(self.root_path,
                                          self.external_path))
        
        df_weather_raw = df_weather_raw[self.external_var]

        df_raw = df_green_raw.merge(df_weather_raw, on="time")
        size = df_raw.shape[0]
        print(size)
        border1s = [0, size//2 - self.seq_len, 3*size//4 - self.seq_len]
        border2s = [size//2, 3*size//4, size]
        border1 = border1s[self.set_type]
        border2 = border2s[self.set_type]
     
        cols_data = df_raw.columns[1:]
        df_data = df_raw[cols_data]
        
        if self.scale:
            train_data = df_data[border1s[0]:border2s[0]]
            self.scaler.fit(train_data.values)
            data = self.scaler.transform(df_data.values)
        else:
            data = df_data.values
        
        df_stamp = df_raw[['time']][border1:border2]
        df_stamp['time'] = pd.to_datetime(df_stamp.time)
        data_stamp = time_features(pd.to_datetime(df_stamp['time'].values), freq=self.freq)
        data_stamp = data_stamp.transpose(1, 0)
        self.data_x = data[border1:border2]
        if(len(self.external_var)-1 >0):
            self.data_y = self.data_x[:,:-(len(self.external_var)-1)]
        else:
             self.data_y = data[border1:border2]
        self.data_stamp = data_stamp
        if(self.set_type == 0 and self.use_weights):
            if(self.load_weights):
                self.weights = 100*load_weights(self.weights_path)
            else:
                self.weights = 100*compute_weights(self.data_y,self.seq_len,self.pred_len)
            
        print(self.data_x.shape)
        print(self.data_y.shape)

    def __getitem__(self, index):
        s_begin = index
        s_end = s_begin + self.seq_len
        r_begin = s_end - self.label_len
        r_end = r_begin + self.label_len + self.pred_len

        seq_x = self.data_x[s_begin:s_end]
        seq_y = self.data_y[r_begin:r_end]
        seq_x_mark = self.data_stamp[s_begin:s_end]
        seq_y_mark = self.data_stamp[r_begin:r_end]
        if(self.set_type == 0 and self.use_weights):
            return seq_x, seq_y, seq_x_mark, seq_y_mark, self.weights[index]
        else:
            return seq_x, seq_y, seq_x_mark, seq_y_mark, np.ones_like(seq_x[0])

    def __len__(self):
        return len(self.data_x) - self.seq_len - self.pred_len + 1

    def inverse_transform(self, data):
        return self.scaler.inverse_transform(data)