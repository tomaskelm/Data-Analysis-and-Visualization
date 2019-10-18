# Data-Analysis-and-Visualization
List
- collect data programmatically (scrapping) from website
- analyze this data 
- output in a HTML format
- output in a PNG image ready to be shared in social networks
## Introduction
Two important things that arise during the implementation of a web scrapping are the following:
1. what is the structure of the web pages that contain relevant data ?
2. how can we get to those web pages ?
In order to answer those questions, we need to understand a little how websites work.
Websites are created using HTML (Hypertext Markup Language), along with CSS (Cascading Style Sheets) and JavaScript.
On a real website, we need to find out between which tags the relevant data is and tell it to our scraper. We also need to specify which links should be explored and where they can be found among the HTML file. With all this information, our scraper should be able to gather the required data.
### What Tools Are We Going to Use ?
In this project we are going to use the Python libraries requests and BeautifulSoup. Link to requests documentation: http://docs.python-requests.org/en/mster Link to BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc
Requests will allow to send HTTP requets to get the HTML files.
BeautifulSoup will be used to parse the HTML files. It is one of the most used library for web scraping. It is quite simple to use and has many features that help gathering websites data efficiently.
### Prerequisites
- python 3.7.4
- requests
- beautifulsoup4
- pandas
### Installing the Required Libraries
Easiest way to install external libraries in python is to use pip. Pip is a package management system used to install and manage software packages written in Python. All you need to do is: 
- pip install requests
- pip install beautifulsoup4
