## Flower detection using yolov5 
This is purely a passion project I decided to make by training yolov5 on a custom dataset that I labeled. The trained model can detect 5 flowers: rose, dandelion, daisy, tulip and sunflower.

## Get Started
1. Clone this repository
2. Run ` pip install -r requirements.txt `
3. Run ` python app.py `
Open the local server in your browser and have fun :)

## Dataset
I used the Roboflow annotation tool to label the images and export them using code. Check out the notebook in the repo to see how to import the custom dataset and train it.
I've also written the code for testing it on a single inference and also to permanently save the trained weights to google drive.

Ultralytics docs - [Train on custom data](https://docs.ultralytics.com/yolov5/tutorials/train_custom_data/#faq)

Dataset link - [Flowers_Classification](<a href="https://universe.roboflow.com/myworkspace-r3ka3/flowers_detection-fh5pt">
    <img src="https://app.roboflow.com/images/download-dataset-badge.svg"></img>)
</a>)

## Demo 
![Screenshot (393)](https://github.com/user-attachments/assets/7df57ec9-ad6f-45fb-beea-b1d46281e12a)
![Screenshot (394)](https://github.com/user-attachments/assets/e4163681-5273-422c-a5e6-37125db1443a)
![Screenshot (395)](https://github.com/user-attachments/assets/2157cedf-d32b-4664-8dcc-ec512d605517)
![Screenshot (396)](https://github.com/user-attachments/assets/145e588d-b25c-4acd-b090-7e2e597cce78)

## Bonus
This is incredibly funny but, while annotating, I decided to skip this image below, since it doesn't contain any real flowers. And the model still detected the roses in it. plus a lil tulip :))

![download (4)](https://github.com/user-attachments/assets/05760776-d089-4358-8434-46d05c2162ae)


