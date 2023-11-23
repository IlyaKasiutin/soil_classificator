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
![](./readme_files/Copy%20of%202560px-A_red_soil_crop_field.JPG.jpg)
![](./readme_files/Copy%20of%202560px-A_red_soil_crop_field%20(labeled).JPG.jpg)

Already done:
- [X] trained CNN model
- [X] 4 classes for classification
- [X] sufficient accuracy
- [X] windows version

TODO:
- [ ] add more relevant classes
- [ ] make soil composition prediction (in %)
- [ ] add good UI
- [ ] process images in realtime
- [ ] implement the functionality of a standalone mobile application

