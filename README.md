# Overview


I have decided to create a program that uses data from a SQL database I created.  This database collects information from renters and sellers to be able to show each other what they are selling or wanting to rent.

I have some family members who run a business that allows users to rent recreational vehicles from each other, but they seemed to have issues with connecting the renters to the sellers, as well as the other way around.  I wanted to quickly code up a working prototype for a system that would allow renters to request vehicles for their area and allow the sellers to view that data and act accordingly.  It just helps each individual party to see the supply and demand of what is being sold on the app/website.

[Software Demo Video](https://youtu.be/Y0l0h-UTqJ4)

# Relational Database

I decided to use mySQL as well as the IED workbench to create my database.  I have a very basic understanding of SQL so I wanted to be able to grow in my understanding of the subject even more.

I created four tables within the database.  I created the Sellers and Renters tables to be able to save user data and allow them to "sign in" to the system.  Sellers is joined to a table called Listings, which allows them to post up and save listings to their profile.  The Renters table is linked to a table called Requests, which allows a user to put out a request for a specific vehicle, which a Seller can view if they are in their same State.

# Development Environment

I used Visual Studio Code to connect the database to python and code.  I used mySQL workbench to help me create a model, which I was able to forward engineer relatively quickly into a working database.

I used python to program a majority of the software, but I used the mysql connector package in order to use SQL commands within python.  I of course used SQL to query, update, create, and delete my data as well.

# Useful Websites

- [Youtube Tutorial](https://www.youtube.com/watch?v=3vsC05rxZ8c&list=PLzMcBGfZo4-l5kVSNVKGO60V6RkXAVtp-)
- [W3 Schools - MySQL](https://www.w3schools.com/mysql/default.asp)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- I want to allow users to filter their searches more, which is easy to do, but just takes a lot of time.
- I want to try and build a similar system to work in JavaScript, allowing me easier access to setting it up on a website
- I need to research how to better keep user data safe while saved in a database.  I have already begun researching encryption for user passwords.