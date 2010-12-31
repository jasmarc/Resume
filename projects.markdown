Raycasting and Wirefram Polygon
-------------------------------
During the mid-nineties, I was very interested in game programming. Working with the book Tricks of the Game Programming Gurus, I was able to implement a few of the concepts that I read about such as ray-casting and wireframe polygons. Some of that work involved writing lower-level assembly code for speed, such as an implementation of Bresenham's line drawing algorithm for approximating arbitrary straight lines in a grid.

Checkers Program
----------------
Around the same time, I wrote a small implementation of the game of checkers for two players in Pascal. My initial implementation was text-based, but was capable of preventing illegal moves and able to detect the end of the game and which player was the winner. My subsequent version was completely graphical, using the mouse to select moves. Some of the graphics and mouse handling were done through lower-level hardware interrupts.

NROTC Website
-------------
During my undergraduate, I was part of the Naval ROTC. One of my roles was webmaster. We had a basic Linux, Apache, MySQL, and PHP system that I oversaw. I implemented several new features in this system to help automate the semesterly data collection process. Based upon the data collected by the system, I was able to automate the generation of email lists and automatically produce RTF documents used as roster sheets for each of the subunits within the NROTC. I also created a database-driven organizational chart complete with profile pictures and contact information.

HCCL Website
------------
Shortly after I graduated, I was contacted by the Hispanic Chamber of Commerce to implement a full contact and mailing list system. I installed a Linux, Apache, MySQL, and PHP system that was used by a small team to input the names of business owners and benefactors associated with the HCCL. The system had basic lookup functionality with paginated results. New contacts could be added with a variety of fields, some were freeform but some were drop-down lists associated with foreign tables.

Program to Scrape Bank Data
---------------------------
I wrote a small Ruby script that does user agent spoofing and other hacks to simulate logging into my own bank account to scrape my financial data for financial reconciliation. That same script used Google's GCal API's to reconcile billing data with paid bills in order to balance my checking account. The system would then email me a small snippet of formatted data that I would append into a master spreadsheet to help keep track of my finances.

Program to Provision Handhelds
------------------------------
At my first job, one of the more tedious tasks for our deployment team was to provision hundreds of handheld devices for specific clients. This typically involved loading specific software, setting specific registry settings, renaming certain files, etc. I wrote a small utility in C++ that could read a text-based configuration script to do this task automatically.

Program to Parse Signature Data
-------------------------------
At this same company, we collected customer signatures on the handheld devices previously mentioned. The signatures were stored in a proprietary format that was unintelligible in its stored form. I found the specification for the storage of this data and was able to write a small program to extract the customer signatures as a bitmap. This utility was extremely useful for development, testing, debugging, and investigative research into production issues.

Program to Tag
--------------
At my next job, I wrote a ruby script that did automatic subversion tagging with dependency checking. Given a particular branch, the script would look for dependencies via the svn:externals metadata, find the latest tag of dependencies, set the externals accordingly, then look for the latest tag of the specified branch, increment the revision number, set the tag number in the AssmeblyInfo.cs files, then tag the project, then set all externals back to their respective branch URL's. This process was an otherwise manual process that was greatly simplified because of this script.

Hudson
------
At this same company, I took the initiative to instate a continuous integration server. I chose to use Hudson because of its ease of deployment. The program ran on a server and would receive notifications from the central subversion server when developers changed code. It would then check the code out, perform builds, and run all unit tests. Then Hudson would email the appropriate parties if anything was broken.

Subversion Talk
---------------
At Georgia State University, I was invited by the Math Department's Software Interest Group to give a talk on Subversion. The audience was  composed of undergraduates, graduate students, and some professors of the math department, most of whom were of a technical background but were not, at the time, familiar with the concept of revision control. The purpose of the talk was to introduce the idea of revision control for the application of storing, backing up, branching, tagging, and working collaboratively with academic source code such as LaTeX, Matlab code, etc.

Python Robot Project
--------------------
I worked with Dr. King at Georgia State, Dr. Summet at Georgia Tech, and Dr. Blank at Bryn Mawr, helping with the IPRE robotics program. I worked on the library code for python-based robots that are used for introductory Computer Science classes.

Arduino + TTL Chips
-------------------
I occasionally tinker with an Arduino microcontroller, TTL logic gates, and 555 IC Timer circuits. My projects are usually small hacks and usually involve experimental tone generation or lighting up seven-segment displays.

MythTV
------
Over the years I've occasionally tinkered with MythTV and other home-brew DVR projects, including some Apple TV hacks.

Small Computers
---------------
I recently purchased two small computers: a FitPC and a wallwart computer for experimenting with ultra small-scale linux servers. This is closely related to my home theater experiments, as the FitPC was purchased with intention of being a front-end video server.

Information Retrieval Class
---------------------------
http://www.infosci.cornell.edu/Courses/info4300/2010fa/
https://github.com/jasmarc/kmeans
https://github.com/jasmarc/Singular-Value-Decomposition
https://github.com/jasmarc/PageRank
https://github.com/jasmarc/Search-Engine

Software Engineering Class
--------------------------
http://www.cs.cornell.edu/courses/CS5150/2010fa/projects.html
http://textmed.net/

Machine Learning for ICS
------------------------
http://jasmarc.posterous.com/tag/cornellmeng
http://blogs.cornell.edu/ml4ics/
https://github.com/jasmarc/mRVM