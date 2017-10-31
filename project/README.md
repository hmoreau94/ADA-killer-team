# How do reviews shape our experience on amazon ?

# Abstract
How do reviews shape the experience of users on Amazon? As users of this platform we have experienced ourselves how highly influenced we can be when it comes to reviews. We therefore wondered many things concerning those reviews. 

We first wondered how they impact users both on the buyer side and the reviewer side. Once we have determined the weight of such reviews on the users we can start on users we can start looking at the caracteristics of such reviews : what are the syntax of positive and negative (in terms of rating) reviews, how do reviews correlate with prices (number of reviews ...) but also what are the taxonomics of helpful reviews. Then we'll dive deep into the problem we identified : what is the proportion of fake reviews on the plateform. We will try to design a strategy to assess fraudulent reviews and then will try to analyse how frequent they are and what are their caracteristics (evolution in time of the reviews, are they used as means of promotion or to get rid of competition, is there a category of product where they are more frequent...).

All this work has as goal to emphasize to amazon customers that reviews are not the only way to asses a product and that they should always look for third parties reviews.

For our study, we will use the dataset “Amazon review data”. We will focus on categories of data that offer the most of reviews to be able to provide real insights and not get distracted too much by the size of the data. We will therefore work on Books already at the center of many research, for example [here](https://www.stat.berkeley.edu/~aldous/Research/Ugrad/Timothy.Thesis.pdf)), Electronics, Movies & TV and finally CDs.


# Research questions
1. _Influence of Reviews_
	* Task a : Is there a proper correlation between products that are similar in characteristics but have different reviews and the sales.
	* Task b : Does the first reviewer influence the others : how likely will we see following reviews that highly diverge from the reviews the product has already received?
	* Task c : What is the price gap to review ratio : from what price difference does a drop in reviews not influence buyers anymore (to be possibly distinguished between categories of products where price differences for similar items can be quite high)


2. _Characteristics of reviews:_
	* Task a : Syntactic analysis of positive and negative reviews (word maps) and could even use previous work of reviews digest creation ([Review Digest @Github](https://github.com/rprajapati1/ReviewDigest))
	* Task b : How do reviews correlate to price : does cheaper means more buyers and hence more reviews, does more expensive means better products ?
	* Task c : What is an helpful review made of (length, rating, vocabulary, frequency of the ratings by a user - are frequent users more helpful -)

3. _Fraud in reviews :_ Can find great first approach here : [Could Fake reviews kill amazon ? @DataScienceCentral](https://www.datasciencecentral.com/profiles/blogs/could-fake-reviews-kill-amazon)
	* Task a : How can we detect fraudulent reviews (same review on multiple products, highly divergent ranking compared to the rest, multiple similar reviews in a short amount of time, name of the reviewer …)
	* Task b : Are detected fraudulent reviews mostly positive or negative : are they used to promote a product or to avoid competition.
	* Task c : Is there more and more fraudulent reviews. What is the time evolution of fraudulent reviews.
	* Task d : Where are fraudulent reviews more prominent, categorical analysis of the fraudulent review in terms of price, category of products and location.

4. _Draft for the report_ : We plan here to make a website to clearly display the result of our data analysis. Nevertheless because we aren't sure yet of what type of interesting results we will have at the end we can only make assumptions and this part will most Certainly be reshaped once we gain a bit of traction on the data exploration.
	* Task a : On the first page we will display the important numbers and big discoveries of the influence of Reviews, characteristics of reviews and fraud in reviews analysis.
	* Task b : We would really like to find a way to display a map that shows the localisation of either the products that are the most sensible to fraudulent review and have yet to get a way to find such location. Multiple strategies were considered :
		* Scrap the location of the reviewer from their user page. Caveat : not all users have filled this information
		* Scrap the product page to find the seller and its location: Caveat : some objects are sold by multiple vendors and could therefore have multiple coutries. 


# Dataset
We do not plan on using another dataset to enrich this one. But we might want to enrich it using amazon website and links to the product to get location data for our reviews and/or products. 

# A list of internal milestones up until project milestone 2
![](ada-milestones.png)

# Questions for TAs
We wanted to have your insights on a few key points for this project :

* First of all do you think that we are reasonnable enough with this first draft, we are not sure about what we are expected to produce but are satisfied by the subjects that we have carved out of this.
* We really want to do something very visual and have yet to come up with ways to make this interactive to present in our story. Would you have any recommandation In particular for Task 4.a ?
* About task 3.a we do not think yet that we will use machine learning because it is only a subtask of this 3rd part (but also because we do not have labels to train on and here clustering reviews would maybe not be conclusive), is it still enough to consider arbitrary set of rules that we think define a fraudulent review ?
