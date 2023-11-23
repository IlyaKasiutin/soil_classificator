# Soil classification model
CNN model based on MobileNetV3: https://arxiv.org/abs/1905.02244
Current approximate accuracy: 80%

Model was trained on https://www.kaggle.com/datasets/jayaprakashpondy/soil-image-dataset

This dataset contains 4 soil types:
- Alluvial soil
- Black soil
- Red soil
- Clay

Example of input/output:
![](../Soil_classificator_base/dist/images/Copy of 2560px-A_red_soil_crop_field.JPG.jpg)
![](../Soil_classificator_base/dist/labeled_images/Copy of 2560px-A_red_soil_crop_field.JPG.jpg)


TODO:
- [ ] add more relevant classes
- [ ] make soil composition prediction (in %)
- [ ] process images in realtime
- [ ] implement the functionality of a standalone mobile application

