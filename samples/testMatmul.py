import tensorflow as tf
from tensorflow import Session, device, constant, matmul

with Session() as session:
    with device('/cpu:0'): # 計算デバイスを指定する
        mat1 = constant([[3,3]])
        mat2 = constant([[2],[2]])
        product = matmul(mat1,mat2)
        result = session.run(product)
        print(result)