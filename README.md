# Estimate data science salaries: Project overview
* Created a tool that can estimate data science salaries with a mean absolute error of $11k.  
* Scraped data of 1000 companies from Glassdoor using selenium and python.  
* Performed data cleaning on the data by extracting specific features from existing features.  
* Performed explanatory data analysis to provide an insight on why a particular state pays less/more and why.  
* Used and optimized Linear, Lasso, Random Forest Regressor, GridSearchCV to obtain the best model.  
* Built a basic flask api for the client.  

(Currently only for US. I'll try to do the same for India as well)  
For the Indian version I'll have to search an other method to scrape data from Glassdoor since the websites for both the countries are different and I've configured Selenium to work with only the US website using the article mentioned below.  

## **Code and resources used**
*Python version:* 3.7.7  
*Packages:* pandas, numpy, selenium, wordcloud, matplotlib, seaborn, json, pickle, flask  
*Scraper link:* https://github.com/arapfaik/scraping-glassdoor-selenium  
*Scraper Article:* https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905  
*Youtube tutorial:* https://www.youtube.com/channel/UCiT9RITQ9PW6BhXK0y2jaeg (Ken Jee)  
*Word cloud article:* https://www.geeksforgeeks.org/generating-word-cloud-python/  
*Flask productionization article:* https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2  
*Install all the requirements:* ```pip install -r requirements.txt```
## **Steps involved**
* Web scraping  
* Data cleaning  
* Explanatory Data Analysis  
* Model building  
* Flask productionization

## Highlights and performance of the models
The Random Forest Regressor tends to perform the best among the chosen ones.
*  *Random Forest Regressor:* MAE: 11.11507
*  *Linear Regression:* MAE: 18.85362
*  *Lasso Regression:* MAE: 19.66525

**Word cloud on the description of job provided by the company**  
![alt text](https://github.com/shashanks33/ds_salary_project/blob/master/datacloud2.png "Word cloud on the description of job provided by the company")
