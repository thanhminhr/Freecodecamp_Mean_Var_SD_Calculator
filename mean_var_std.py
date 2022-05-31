import numpy as np

def calculate(input):
  if (len(input)!=9):
    raise ValueError('List must contain nine numbers.')
  matrix0= [[input[0],input[1],input[2]],
            [input[3],input[4],input[5]],
            [input[6],input[7],input[8]]]
  matrix=np.array(matrix0)
  mean_res=[np.mean(matrix,axis=0).tolist(),np.mean(matrix,axis=1).tolist(),np.mean(matrix).tolist()]
  var_res=[np.var(matrix,axis=0).tolist(),np.var(matrix,axis=1).tolist(),np.var(matrix)]
  std_res=[np.std(matrix,axis=0).tolist(),np.std(matrix,axis=1).tolist(),np.std(matrix)]
  max_res=[np.max(matrix,axis=0).tolist(),np.max(matrix,axis=1).tolist(),np.max(matrix)]
  min_res=[np.min(matrix,axis=0).tolist(),np.min(matrix,axis=1).tolist(),np.min(matrix)]
  sum_res=[np.sum(matrix,axis=0).tolist(),np.sum(matrix,axis=1).tolist(),np.sum(matrix)]
  result={'mean':mean_res,
       'variance':var_res,
       'standard deviation':std_res,
       'max':max_res,
       'min':min_res,
       'sum':sum_res}
  return result 