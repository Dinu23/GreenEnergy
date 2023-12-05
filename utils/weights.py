import numpy as np
from scipy.integrate import quad

def gaussian_kernel(v, v_0, sigma):
    return np.exp(-(v - v_0)**2 / (2 * sigma**2)) / (np.sqrt(2 * np.pi) * sigma)

def load_weights(path):
    all_weigths = np.load(path)
    return all_weigths


def compute_weights(data,seq_len, pred_len, eps = 1e-3, n_bins = 200, bandwidth = 2, sigma =5):
    LDs = []
    size = len(data)
    print(size)
    for i in range(size - seq_len - pred_len):
        input = data[i:(i+seq_len)]
        mean_input = np.mean(input, axis=0)
        std_input = np.std(input, axis=0)

        output = data[(i+seq_len): (i+seq_len+ pred_len)]
        mean_output = np.mean(output, axis=0)
        std_output = np.std(output, axis=0) 

        LD = (mean_input - mean_output)/np.sqrt(((std_input**2)/seq_len) + ((std_output)/pred_len)  + eps)
        LDs.append(LD)
    
    LDs = np.array(LDs)
    emperical_densities = []
    bins = []
    for i in range(data.shape[1]):
        hist, b = np.histogram(LDs[:,i], bins=n_bins)
        empirical_density = hist / len(data)
        emperical_densities.append(empirical_density)
        bins.append(b)

    weights = []
    for i in range(size- seq_len - pred_len):
        w = []
        for j in range(data.shape[1]):
            
            x_0 = LDs[i][j]
            mini = np.min(LDs[:,j])
            maxi = np.max(LDs[:,j])
            value,_ = quad(lambda x: gaussian_kernel(x,x_0,sigma) *np.interp(x, bins[j][:-1], emperical_densities[j]),a=mini,b=maxi)
            w.append(value)

        w = np.array(w)
        weights.append(w)
        
    weights = np.array(weights)
    return weights

