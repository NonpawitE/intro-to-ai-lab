# Introduction to AI | Lab Session

## Table of Content
- [Anaconda Setup](#anaconda-setup)
- [Visual Studio Code Setup](#visual-studio-code-setup)
- [Grading Criteria](#grading-criteria)


## Anaconda Setup

* Download Anaconda from [here](https://www.anaconda.com/products/distribution)
* Open `Anaconda Prompt`
* Then we setup new environment for our class
```
conda create --name intro_ai python=3.9
```
* If `Proceed ([y]/n)?` shows up, type `y` then press enter
* To activate the environment we created
```
conda activate intro_ai
```
* After that, we will install Open CV
```
conda install opencv
```
* Tensor-flow
```
conda install tensorflow
```
* Keras
```
conda install keras
```
* Pillow
```
conda install pillow
```


## Visual Studio Code Setup

* Download the latest Python 3.9 [here](https://www.python.org/downloads/release/python-3913)
* Download Visual Studio Code from [here](https://code.visualstudio.com/download)
* Open Visual Studio Code
* Download Python extension [here](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* Press `Ctrl + J` to open Terminal
* Create virtual environment
```
python -m venv intro_ai 
```
* Then look on the bottom right and look for `Interpreter`
* Select virtual environment that we created
* Activate virtual environment
```
intro_ai\Scripts\activate
```
* After that, we install Open CV
```
pip install opencv-python
```
* Tensor-flow
```
pip install tensorflow
```
* Keras
```
pip install keras
```
* Pillow
```
pip install pillow
```


## Grading Criteria

| Topic         | Percentage   |
| ------------- |:------------:|
| Mini-project  | 40%          |
| Assignments   | 30%          |
| Mid-term      | 20%          |
| Attendance    | 10%          |
