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

To download the raw data into the colab environment directly, you can use the following command:

~~~
!gdown --id 14JMMOvhOlCotz5ZPbrq_WF9xLsjQ3kUq
~~~

And finally the preprocessed version of the dataset can be downloaded with this command to save time:

~~~
!gdown --id 1rd62dw3yV2j05qOxHdKgLI-0y_BNPPcR
~~~