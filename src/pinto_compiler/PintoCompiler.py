import numpy as np
import cv2

class PintoCompiler:
    def __init__(self):
        self.binary_path = "arborium.pinto"

    def Compile(self):        
        media_binary = self.CompileMedia()
        source_binary = self.CompileSource()
        
        binary_data = np.concat((media_binary, source_binary))
        
        binary_data.tofile(self.binary_path)
            
    def CompileMedia(self):
        img_paths = [ "media/env.png" ]
        
        binary_data = []
        for i in range(len(img_paths)):
            path = img_paths[i]
            img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
            img = img[:, :, [2, 1, 0, 3]]
            
            img = img.reshape(-1)
            img.dtype = np.int32
            
            binary_data.append(img)
             
        binary_data.append(np.zeros(2, dtype = np.int32))
        binary_data = np.concatenate(binary_data)
        
        return binary_data
            
    def CompileSource(self):
        src_path = "src.py"
        
        binary_data = []
        with open(src_path) as f:
            src = f.read()
            #print(src)
            
            binary_data.append(np.zeros(8, dtype = np.int32))
            
        binary_data.append(np.zeros(2, dtype = np.int32))
        binary_data = np.concatenate(binary_data)
        
        return binary_data

application = PintoCompiler()
application.Compile()
