# Instructions

To use this lab in the colab environment, make sure you upload the utils.py along with the raw data to the virtual machine's main directory.
You can also pull data from your own google drive using the following code block: 

~~~
from google.colab import drive
drive.mount('/content/drive')
~~~

(This will ask you to log in each time. You can also mount your google drive using this part. 
After you set it up once it will automatically connect every time you open this notebook.)

<img src="https://github.com/volgasezen/di504/assets/127928023/d257b486-b593-46df-b43a-7ea4493f2318" alt="gdrive instructions" width="500"/>

You can also just use the preprocessed data. To pull it use the following in colab: (Or download it from [here](https://drive.google.com/file/d/1rd62dw3yV2j05qOxHdKgLI-0y_BNPPcR/view?usp=sharing).)

~~~
!wget https://drive.google.com/u/0/uc?id=1rd62dw3yV2j05qOxHdKgLI-0y_BNPPcR&export=download&confirm=t&uuid=c84387e4-c22f-4794-8c2a-e496341b5423&at=AB6BwCCK_s-ycLdW_LLgam3ZTXp3:1700138438465
~~~
