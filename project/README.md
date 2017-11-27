# How do reviews shape our experience on amazon ?

[This document has been reviewed following the first milestone. Last edited 27/11/2017]

# Abstract
How do reviews shape the experience of users on Amazon? As users of this platform we have experienced ourselves how highly influenced we can be when it comes to reviews. We therefore wondered many things concerning those reviews. 

As a general question we wanted to study the [Herding Effect](https://en.wikipedia.org/wiki/Herd_behavior) on reviews : that is how are reviewers influenced by past reviews. To achieve such goal, we decided to first study the effects of reviews on multiple parameters but mostly on the sales Rank of the object to see in what measure are users influenced by reviews. Then we decided to study one category of object in particular : books. Those are the most reliable when it comes to finding similar objects. Indeed multiple products can be identified as similar when the text is the same but only the format changes (e.g. ebooks, different editions, ...). Identifiying similar books is the most challenging part of this project as the large dataset isn't easy to work with. Finaly we dive deep in the study of the Herding effect, trying to identify how the first review of a book can influence the following reviews.


All this work has as goal to emphasize to amazon customers that reviews are not the only way to asses a product and that they should always look for third parties reviews.

For our study, we will use the dataset “Amazon review data”. We will focus on categories of data that offer the most of reviews to be able to provide real insights and not get distracted too much by the size of the data. We will therefore work on Books already at the center of many research, for example [here](https://www.stat.berkeley.edu/~aldous/Research/Ugrad/Timothy.Thesis.pdf)), Electronics, Movies & TV and finally CDs.

We would like to emphasize to a potential reader that we have for now decided to focus on 5-core datas. Those are the products and customers that have at least 5 reviews. This allow us to first only consider a subset of the data but also to make sure that we have at least 5 reviews per product to later study the herding effect (which by itself is already not much). In further work we want to extend the amount of data that we consider to be able to observe quantitative results).


# Research questions
1. _Characteristics of reviews:_
	* Task a : How do reviews correlate to price : does cheaper means more buyers and hence more reviews, does more expensive means better products ?
	* Task b : How do reviews correlate to sales rank : (depending on the category of objects and the price range)

2. _How do reviews influence customers_: 

 	* Task a : Identify a category of product that could be used to find similar objects.
	* Task b : Get similar products (e.g. books that only differ by their format or edition)
	* Task b : Herding Effect - How does the first couple of reviews of a product influence the following reviews ?

4. _Draft for the report_ : We plan here to make a website to clearly display the result of our data analysis. Nevertheless because we aren't sure yet of what type of interesting results we will have at the end we can only make assumptions and this part will most Certainly be reshaped once we gain a bit of traction on the data exploration.
	* Task a : On the first page display the major findings about the reviews and their caracteristics (being as visual as possible)
	* Task b : We would really like to take a few products as example to extrapolate our finding on the Herding effect to be able to give a visual representation of our findings. 
	* Task c : Then we will try to explain how this happens on the entire dataset we considered.
	* Task d : Try to have a time dependent slider to show the evolution of reviews with time.

# Dataset
We decided to use first all the data available from the amazon dataset. Then because we lacked some important details we decided to extend this data with amazon API using the ASINs of products that have already been selected as similars (to reduce the number of API requests that are being done)

# A list of internal milestones up until project milestone 2
![](ada-milestones.png)

# Running
Running the notebooks will highlight which import must be perform and display in the body of the ```Import Error``` how those can be installed (using ```pip``` when possible). 

# Architecture
We decided to modularize the code as much as possible to improve readability and further refinement of the ressearch. Here you will find the description of our architecture :

* ```Ressearch.ipynb``` : this contains the step by step explanation of our ressearch protocol for the exploratory phase. From data exploration, to methods used to perform similarity study. Then it will show the Herding Effect analysis.
* ```scripts/```: contains all the files that are used in the notebook, with relevant names 	
	- ```amazon_api_interaction.py```: all the functions used to interact with the API and get the details that are not in the original dataset
	- ```data_import.py```: functions used to read the large JSON of the original dataset and import it in dataframes.
	- ```similarities.py``` : functions used to isolate similar books split in three phases (work on raw data, refining using the authors and finally how we can keep only the similar books using their normalized titles)
	- ```utils.py```: functions used mainly for details purposes (printing time, printing the details of books : titles, description, images and also to display the progress of the code)
	- ```__init.py__```: used to be able to tell to python that this folder contains modules that can be imported (it is actually an empty file)
*  ```report/```: for now it is simply the empty shell of a potential report that could be used to later synthesise our work.