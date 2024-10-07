# Shop-Crawler
> Shop Crawler is an online automation tool that I developed using Angular and Python hosted on a Linux server running Apache Tomcat and Flask.
* The application was designed to step through a list of available sites (10-20 million) and log statistical data about the sites availability and response times.
* When response was recognized as high, the application would step through the site collecting information using automated docker bots running Selenium --
**about 20-30 to avoid DDOS detection**
* Much of the collected data is processed using:
**Pandas
**Beautiful Soup
**Matplotlib
