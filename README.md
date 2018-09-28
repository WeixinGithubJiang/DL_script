# DL_script
DL script for keras and pytorch

For a deep learning script, usually we need to write a class, including data loading, network building, network running and model saving/loading.

data loading: it should be flexible with the input data type/file type/file path, while it should have a standard output format. Mostly two types, one for classification task, the other is for regression task. For a more advanced version, data augument should be included.

network building: the 1st version should including some typical network model, like Alex Net, VGG Net, Res Net, advanced version should include customized network architecture.

network running: training and testing, including input parameters for batch size, optimizer, criterion, max epoches.

model saving/loading.