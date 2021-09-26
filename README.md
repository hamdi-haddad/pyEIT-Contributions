# pyEIT-contributions
This project presents my contributions to pyEIT library (it includes changed and added code and files only)
pyEIT source code : https://github.com/liubenyuan/pyEIT

* To run the project with this update :
  - Install the source code 
  - Add modified/added lines of codes and files in this repository. 
  - Run the following commands to compile the update :
  $python setup.py build
  $python setup.py install
  - Run any example of EIT image reconstruction algorithms using the command :
  $python "file_path" 


* Every added/modified line or file is commented to know where to include the change .  

* Modified/added code: 
- In the mesh folder ( respectively in the files: distmesh.py,shape.py and wrapper.py ), in fem.py and in the image reconstruction algorithms ( in examples folder ) to be adapted to the update in the library . 

* Added modules (Real simulations folder): 

- Image reconstruction algorithms based on real thorax voltages from lungData.py (the voltages are taken from EIDORS library documentation page and they are measured based on 16 electrodes with an image frequency of 7 frames/s)
- UNET_Segmentor includes a Deep Learning trained model (V8.hdf5 file) (U-NET multi-class image segmentation) that segments the thorax image to better visualize thorax regions. Training Data-Set includes EIT thorax reconstructed images and manually labeled thorax images (masks) based on a real CT thorax image using APEER microscopy software. Data augmentation was also performed on the available Data-Set. The model is trained on 1035 thorax images in Colab Pro platform.
NB: You can build and apply your own deep learning model. To do so, you can check my notebook on Google Colab (that i used to build this model) that includes details about the Data-Set upload, Data augmentation, Model training and evaluation.  
Link to my Google Colab notebook : https://colab.research.google.com/drive/1BVtGQvwxikfXjR9H5jqypf3tB0xlazs-?usp=sharing#scrollTo=p1ae943ld6L0


* Don't hesitate to create an issue if you have any question/problem .

NB : "#....#" in code means that : in that place there are line(s) of codes in the original pyEIT source code. 
