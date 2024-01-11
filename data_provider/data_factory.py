import os
from data_provider.GreenEnergyDataset import GreenEnergyDataSet
from torch.utils.data import DataLoader

def data_provider(args, flag):
    if flag == 'test':
        shuffle_flag = False
        drop_last = False
        batch_size = args.batch_size
        freq = args.freq
    else:
        shuffle_flag = True
        drop_last = True
        batch_size = args.batch_size
        freq = args.freq

    data_set = GreenEnergyDataSet(
        root_path=args.root_path,
        flag=flag,
        size=[args.seq_len, args.label_len, args.pred_len],
        freq=freq,
        external_var = args.external_var,
        use_weights=args.use_weights,
        weights_path=os.path.join(args.root_path,f"weights/weights_{args.seq_len}_{args.label_len}_{args.pred_len}.npy"),
        load_weights=args.load_weights,
        future = args.future
    )
    print(flag, len(data_set))
    data_loader = DataLoader(
        data_set,
        batch_size=batch_size,
        shuffle=shuffle_flag,
        num_workers=args.num_workers,
        drop_last=drop_last)

    return data_set, data_loader
