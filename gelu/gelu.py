import math
import numpy as np

# x là tham số đầu vào kiểu list
# kết quả trả ra là np.ndarray
def gelu(x: list) -> np.ndarray:
    x = np.asarray(x, dtype = float) # chuyển kiểu list về kiểu mảng vì kiểu list không được hỗ trợ kiểu tính toán
    erf = np.vectorize(math.erf) # vecto hóa thay vì viết vòng lặp thủ công cho math.erf
    return x/2*(1+erf(x/np.sqrt(2)))
    
    