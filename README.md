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

* Changes are made in mesh folder ( respectively in the files: distmesh.py,shape.py and wrapper.py ) and in the image reconstruction algorithms ( in examples folder ) to be adapted to the update in the library . 

* Don't hesitate to create an issue if you have any question/problem .

NB : "#....#" in code means that : in that place there are line(s) of codes in the original pyEIT source code. 
