import numpy as np
import cv2

class PintoCompiler:
    def __init__(self):
        self.binary_path = "arborium.pinto"

    def Compile(self):        
        media_meta, media_binary = self.CompileMedia()
        source_meta, source_binary = self.CompileSource()
        meta_meta, meta_binary = self.CompileMeta(media_meta, source_meta)
        
        binary_data = np.concat((meta_binary, media_binary, source_binary))
        
        binary_data.tofile(self.binary_path)
        
        print("Compiling complete!")
        print("   meta_size:", meta_meta["size"])
        print("   media_size:", media_meta["size"])
        print("   total_size:", binary_data.shape[0])
            
    def CompileMeta(self, media_meta, source_meta):
        meta_data = {}
        
        media_start_address = 3
        instruction_start_address = media_start_address + media_meta["size"]
        
        binary_data = np.array([5, media_start_address, instruction_start_address], dtype = np.uint32)
        binary_data = np.zeros(1024, dtype = np.int32)
        binary_data[0] = 10424079
        binary_data[1] = media_start_address
        binary_data[2] = instruction_start_address
        binary_data.dtype = np.int32
        
        meta_data["size"] = binary_data.shape[0]
        
        return meta_data, binary_data
        
    def CompileMedia(self):
        img_paths = [ "media/framebuffer0.png", "media/framebuffer1.png" ]
        meta_data = {}
        binary_data = []
        
        total_size = 0
        for i in range(len(img_paths)):
            path = img_paths[i]
            img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
            img = img[:, :, [2, 1, 0, 3]]
            
            img = img.reshape(-1)
            img.dtype = np.int32
            
            binary_data.append(img)
            total_size += img.shape[0]
             
        binary_data.append(np.zeros(2, dtype = np.int32))
        binary_data = np.concatenate(binary_data)
        
        meta_data["size"] = total_size
        
        return meta_data, binary_data
            
    def CompileSource(self):
        src_path = "src.py"
        meta_data = {}
        binary_data = []
        
        with open(src_path) as f:
            src = f.read()
            #print(src)
            
            binary_data.append(np.zeros(8, dtype = np.int32))
            
        binary_data.append(np.zeros(2, dtype = np.int32))
        binary_data = np.concatenate(binary_data)
        
        return {}, binary_data

application = PintoCompiler()
application.Compile()
