<h1 align=center>Mildew Detection</h1>

<img src="assets/images/Mildew Detection Background.png">



[Live View](https://mildew-detection01-7248fb9a8199.herokuapp.com/)

Mildew Detector is an app that can predict whether a cherry leaf is healthy or is infected with powdery mildew. The app is capable of predicting on new image data of a given cherry leaf is healthy or infected.

The project aim is to create a Predictive Analytics Machine Learning Tool that can rapidly and accurately determine whteher an uploaded image of a cherry leaf is a healthy leaf, or one infected with the Powdery Mildew Disease, which is harmful to plants. The prupose of this is to aid the client in limiting their losses as a busienss that relies heavily on cherry leaves as a product for revenue.

The app has been designed using an ML model based on a supervised learning and single-label binary classification. A binary classifer output is used to predict the outcome of data uploaded to the app.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project to all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

### **Project Goal:**

* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.

* 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.



## Hypothesis and Validation

* Infected leaves have clear marks differentiating them from the healthy leaves.We suspect cherry leaves affected by powdery mildew have clear marks, typically the first symptom is a light-green, circular lesion on either leaf surface, then a subtle white cotton-like growth develops in the infected area.

## Rationale to map the business requirements to the Data Visualisations and ML tasks

### Business Requirement 1: Data Visualisation
  
- The client wants to display the mean and variability of healthy cherry leaf images and cherry leaves that contain powdery mildew infection, so that they can visually differentiate between the two.
- The client wants to visually display the difference between an average healthy cherry leaf, and an average powdery mildew infected cherry leaf. This allows detection of distinguishable variations between the two. 
- The client would like an image montage to be available for healthy leaf images, and infected leaf images. This is to allow for a visual differentiation between the two image labels, and to recognise appearance patterns across images of the same label. 

### Business Requirement 2: Classification of Images

- The client requires a tool that accurately predicts whether a given cherry leaf is healthy or infected with powdery mildew disease.
- The client needs a data processing and prediction tool that can be assimilated across the company. This will eliminate need for manual detection of the infection which requires employee time and increased personnel resources.
- The company will save time and labour resources, as well as capital spent on these, by increasing the volume of product they can export and provide to the market. This will in turn increase their revenue and therefore provide the company with greater funds to invest in its own productivity and actvitiy.  
- The client wants an ML model with a binary classification output, and to have the ability to generate and download a report of the results.

## ML Business Case

* As a client I want a ML model to predict if the cherry leaf tree is healthy or has powdery mildew.
* The ideal outcome is provide Farmy & Foods with a faster and reliable mildew detection mechanism that is readily scalable across the multiple farms in the country
* The model success metric are:
  * A study showing how to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
  * The capability to predict if a cherry leaf is healthy or contains powdery mildew.
  

---


---

## Dashboard Design



### Page 1: Quick Project Summary

  * Project Dataset

    * The available dataset contains 2104 healthy leaves and 2104 affected leaves individually photographed against a neutral background.

  * Business requirements
    * A study to visually differentiate a healthy from an infected leaf.
    * An accurate prediction whether a given leaf is infected by powdery mildew or not.
    * Download a prediction report of the examined leaves.
    <hr>
    <img src="assets/images/Project Summary.png">

### Page 2: Cherry leaf visualizer

* It will answer business requirement 1
  * Lists the findings related to the study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
  * Checkbox 1 - Difference between average and variability image
  * Checkbox 2 - Differences between Healthy and Powdery Mildew Cherry Leaves
  * Checkbox 3 - Image Montage

  <hr>

  <img src="assets/images/Leaves Visualiser Page.png">
  

### Page 3: Mildew detector

* It will answer business requirement 2
  * Link to download a set of cherry leaf images for live prediction
  * file upload widget to upload one or more images for prediction
  * Display image and prediction statement indicating whether or not a cherry leaf conatins mildew
  * Display table with image name and prediction result
  * Download button to download table
  <hr>
  <img src="assets/images/Powdery Mildew detector.png">
  <img src="assets/images/Powdery Mildew detector 2.png">
  <img src="assets/images/Powdery Mildew detector 3.png">
  <img src="assets/images/Powdery Mildew detector 4.png">

### Page 4: Project Hypothesis and Validation

* Infected leaves have clear marks differentiating them from the healthy leaves.We suspect cherry leaves affected by powdery mildew have clear marks, typically the first symptom is a light-green, circular lesion on either leaf surface, then a subtle white cotton-like growth develops in the infected area.
<hr>
<img src="assets/images/Project Hypothesis.png">

### Page 5: ML performance metrics

* A technical page displaying the model performance
<hr>
<img src="assets/images/ML Performance Metrics 1.png">
<img src="assets/images/ML Performance Metrics 2.png">

## **Features**

The application is designed using streamlit library. It is has a sidebar menu with five navigation links.

**Navigation** The dashboard developed is a multipage streamlit application with sidebar navigation checkbox links. The navigation links provides quick access to the five pages listed:

* **Page 1: Quick Project Summary**
This page displays a brief overview of the project requirements and the dataset
![](docs/images/page_1_summary.png)

* **Page 2: Cherry leaf visualizer**
This page displays a brief overview of the project requirements and the dataset
![](docs/images/page_2_visualizer_difference.png)

![](docs/images/page_2_visualizer_diff.png)

* **Page 3: Mildew Detector**
This provides the interface for the user to upload test samples and predict wether or not the samples provided are healthy or infested with powdery leaf mildew. It features a *Browse file* button which user can use to upload one or more image files. Prediction is not made until the user clicks on the *Make Prediction* button. The image uploaded as well as the prediction and report is displayed to the user when the prediction is complete

![](docs/images/page_3_detector.png)

 ![](docs/images/page_3_detector_2.png)

* **Page 4: Hypothesis and Visualization**
This page shows the project hypothesis and how it is validated across the project.
![](docs/images/page_4_hypothesis.png)
  
* **Page 5: ML Performance Metric**
Technical information about the model and data are displayed on this page. It shows the:
  * label frequencies of the train, validation and test datasets
  * training model accuracy and loss charts
  * generalised performance on the test sets
  
![](docs/images/page_5_metrics.png)

---

## Bugs and Fixes

* After deploying my project to Heroku, the Image Montage was not displaying since the directory holding the images had been excluded from the GitHub push due to privacy issues, indicating that the data can only be shared with professionals who are formally participating in the project.

## Deployment

Steps I took to setup environment and deploy to Heroku

### Workspace Setup

The repository for this project was created off the [template](https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves) provided by Code Institute and GitPod workspace was used to develop this project.

* Click the `Use This Template` button.
* Add a repository name and brief description.
* Click the `Create Repository from Template` to create your repository.
* Click `Gitpod` to create a Gitpod workspace.
* To return to the current workspace, login to your gitpod acoount and open the workspace created earlier, since clicking on GitPod button on the GitHub page creates a new workpspace each time.

*Cloning the GitHub Repository*

Cloning your repository will enable you to work on a local version of the repository.

1. Locate the [project repository](https://github.com/valerieoni/mildew-detection)
2. Press the arrow on the Code button
3. To clone the repository using HTTPS, copy the [link](https://github.com/valerieoni/mildew-detection.git) that is shown in the drop-down
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned created
6. In the terminal type `git clone` and then paste the link you copied in step 3
	`git clone https://github.com/valerieoni/mildew-detection.git`
7. Press enter and your local clone will be created.

### Creating Heroku App

The Python version in the project is set to 3.8.13, which is not supported by Heroku's current default stack, heroku-22.
As a result of the above, the app was created from Heroku CLI and set to use buildstack heroku-20.

Steps take to create the app is as follows:

1. download and install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) if not already installed
2. Copy API key from heroku
	* sign in and click on the avatar icon and select **Account Settings**
	* Scroll down to the API Key section and click **Reveal** button, and copy key displayed.
3. login to Heroku via the console and enter your details when prompted
	`heroku login -i`
	* enter key copied from step 2 when prompted for password
4. create the app
	`heroku apps:create pp5-mildew-detection --stack heroku-20`

### Deploying to Heroku

1. Sign in to Heroku
2. Select app
3. At the Deploy tab, select GitHub as the deployment method.
4. Select your repository name and click Search. Once it is found, click Connect.
5. Select the branch you want to deploy, then click Deploy Branch.
6. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.

## Technologies Used

### Main Data Analysis and Machine Learning Libraries

* [TensorFlow](https://www.tensorflow.org/overview) - used during image preprocessing to filter out corrupt images.
* [Keras](https://keras.io/) - used for the CNN model
* [joblib](https://pypi.org/project/joblib/) for saving and loading image shape
* [numpy](https://numpy.org/) - used for array manipulation.
* [pandas](https://pandas.pydata.org/) - used to structure the data
* [matplotlib](https://matplotlib.org/) For creating the charts and plots for data visaulization
* [seaborn](https://seaborn.pydata.org/) Used in conjuction with matplotplib for data visualization
* [plotly](https://plotly.com/) - used for ploting charts for data visualization
* [streamlit](https://streamlit.io/) For the dashboard development
* [scikit-learn](https://scikit-learn.org/stable/) - used for data processing
* [jupyter notebook](https://jupyter.org) - used for writing and running the ML pipelines

### OtherFrameworks, Libraries & Programs Used

* [Git](https://git-scm.com/) - used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub:](https://github.com/) - used to store the projects code after being pushed from Git.
* [Balsamiq:](https://balsamiq.com/) - Balsamiq was used to create the Dashboard [wireframes](docs/project_wireframe.pdf) during the design process.
* [Heroku](https://www.heroku.com/) - Deployment platform for the project
* [GitPod](https://www.gitpod.io/) - Workspace used for the project
* [AmIResponsive](http://ami.responsivedesign.is/) - Used to generate responsive image used in README file.

## Credits

I used several internet sources to resolve issues and solve difficulties when constructing this website, as well as modules to add functionality.

### Content

* The codes used to implement the functionalities in the project are from the Code Institute training by GyanShashwat1611 at [Github site](https://github.com/GyanShashwat1611/WalkthroughProject01/)
* Dataset is from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)

### Media

* The images used in the readme and as sample download files on the dashboard are sourced from [pixabay](https://pixabay.com/) and [iStock](https://www.istockphoto.com/)

## Acknowledgements

* I would like to thank my mentor, Marcel Mulders for his support, guidance and feedbacks throughout the course of the project.
