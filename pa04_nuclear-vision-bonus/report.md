For this assignment I tested out traditional feature extraction methods and a basic U net model.

Since the traditional feature extraction methods didn't have a very high score, I decided to switch to a NN model since it would probably have a higher score

Using the U net tutorial model that the kaggle competition provided
https://github.com/kamalkraj/DATA-SCIENCE-BOWL-2018/blob/master/Data_Science_Bowl_2018.ipynb

I decided to adapt this notebook for my own uses. One significant hurdle I faced was that the stage2 data, not the stage 1 data was the data needed to submit to the assignment, so I was really confused when the submission I used for stage 1 was invalid.

Another issue was the dataset for stage2 which was the one I needed to submit had an image in it that was invalid, which broke my neural net pipeline program in the ipynb. After unsuccessfully attempting to find a remedy to the problem through using pathlib and seperating out reading the image and getting a segment of an image, I just used a basic try except block to replace a failed image read with a placeholder dark image. I also had to modify the entire codebase to accomodate running both stage1 and stage2 testing, since I didn't know at the time that only stage2 was needed.

A third problem I faced was that colab would delete all my files every time I refreshed, so I had to pack up everything and switch to the mill, which, despite being on the gpu node didn't let my model use the gpu for some reason.

Since the NN took so long to train (about 78 minutes) and the whole process was in general very time consuming just to test things out, it took multiple days before I was able to test things out enough to come up with a good solution. Doing this competition was exhausting, and I don't want to spend another second on it.