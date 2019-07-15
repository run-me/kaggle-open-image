This directory holds different detection frameworks being experimented with.

## Currently the repo holds
1. mmdetection<br>

#### Inference Instructions
1. Download mmdetection framework from github and put it inside this directory 
2. Follow the installation instructions for the mmdetection framework
3. install pycocotools in the venv using the command 
`pip3 install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI` 
4. Ensure path for cuda and nvidia library framework if there is path error
5. Run any python script associated with any model in inference_scripts directory 
to verify installation when you see output

#### Training Instructions
- [ ] Data pre-processing script
- [ ] Custom dataset entry