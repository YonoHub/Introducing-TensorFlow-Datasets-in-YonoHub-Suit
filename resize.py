import cv2

from yonoarc_utils.image import to_ndarray, from_ndarray


class resize:
    
    def on_new_messages(self,messages):
        
        width=self.get_property("width")
        height=self.get_property("height")
        
        dim=(width,height)
        
        resized_image=cv2.resize(to_ndarray(messages["image"]),dim,interpolation=cv2.INTER_AREA)
        
        self.publish("resized_image",from_ndarray(resized_image,messages["image"].header))