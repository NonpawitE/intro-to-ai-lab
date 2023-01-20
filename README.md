# Introduction to AI | Lab Session

## Table of Content
- [Anaconda Setup](#anaconda-setup)
- [Visual Studio Code Setup](#visual-studio-code-setup)
- [Grading Criteria](#grading-criteria)
- [Export Model from Teachable Machines](#export-model-from-teachable-machines)


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
* Spyder
```
conda install spyder
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
<img width="499" alt="Screenshot 2023-01-18 at 15 06 06" src="https://user-images.githubusercontent.com/95632474/213116876-0172ab07-9791-49de-957d-69d99bc596f1.png">

* Select virtual environment that we created
<img width="599" alt="Screenshot 2023-01-18 at 15 08 08" src="https://user-images.githubusercontent.com/95632474/213117247-73e4fe3c-92e9-4604-937c-a78238c0be7a.png">

* Activate virtual environment
```
intro_ai\Scripts\activate
```
* If there's problem about `ExecutionPoliicy` type this in Terminal, then repeat the step before
```
Set-ExecutionPolicy Unrestricted -Scope CurrentUser
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


## Export Model from Teachable Machines

* First, train your model in [Teachable Machine](https://teachablemachine.withgoogle.com/train)
* Press export your model
<img width="425" alt="export" src="https://user-images.githubusercontent.com/95632474/213115634-83100231-1425-4db1-b119-efae344ef5af.png">

* Then, click export as Tensor-flow
* Download model as Keras
* Also, you can copy the Open CV code from the bottom section
<img width="808" alt="Screenshot 2023-01-18 at 14 52 50" src="https://user-images.githubusercontent.com/95632474/213116291-5f2f8aa1-633f-4f28-b629-ac4bea821d08.png">

