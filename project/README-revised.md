# How do reviews shape our experience on amazon ?

[This document has been reviewed following the first milestone. Last edited 10/11/2017]

# Abstract
How do reviews shape the experience of users on Amazon? As users of this platform we have experienced ourselves how highly influenced we can be when it comes to reviews. We therefore wondered many things concerning those reviews. 

As a general question we wanted to study the [Herding Effect](https://en.wikipedia.org/wiki/Herd_behavior) on reviews : that is how are reviewers influenced by past reviews. In order to do that we decided to first give a sense of the characteristics of reviews to see exactly their taxonomy, how they influence the sales rank and how it correlates with price. Then once this is clearer and we know more about reviews and how they influence buyers we dive deep into the influence of past reviews on future reviews and that on items that we can identify as being similar (e.g. two phone that only differ by their color, two TVs that only differ by their size etc.). All this study will try to highlight results depending on categories of products.

All this work has as goal to emphasize to amazon customers that reviews are not the only way to asses a product and that they should always look for third parties reviews.

For our study, we will use the dataset “Amazon review data”. We will focus on categories of data that offer the most of reviews to be able to provide real insights and not get distracted too much by the size of the data. We will therefore work on Books already at the center of many research, for example [here](https://www.stat.berkeley.edu/~aldous/Research/Ugrad/Timothy.Thesis.pdf)), Electronics, Movies & TV and finally CDs. (Nevertheless for part 2, we might need to drop some categories to focus on the ones where we can find sufficient similar pairs of products to conduct our analysis)


# Research questions
1. _Characteristics of reviews:_
	* Task a : Syntactic analysis of positive and negative reviews (word maps) and could even use previous work of reviews digest creation ([Review Digest @Github](https://github.com/rprajapati1/ReviewDigest))
	* Task b : How do reviews correlate to price : does cheaper means more buyers and hence more reviews, does more expensive means better products ?
	* Task c : How do reviews correlate to sales rank : (depending on the category of objects and the price range)
	* Task d : What is an helpful review made of (length, rating, vocabulary, frequency of the ratings by a user - are frequent users more helpful -)

2. _What factors influence reviews_ : How do external factors that are not defining the product influence the review (e.g. time and previous reviews).
	* Task a : Identify a set of caracteristics from the metadata that can be used in order to identify similar products (same price, different size, different color etc.)
	* Task b : Herding Effect - How does the first couple of reviews of a product influence the following reviews ?
	* Task d : How do review change with time, do we witness a significant drop in reviews over time ?
	* Task c : How does the usefulness of the reviews vary over time (do people rate differently in term of helpfulness the first reviews and last reviews) ?

3. _(Optionnal depending on time) Suspicious reviews_:
	* Task a : Identify the few caracteristics of reviews that can show that they could be fraudulent (same review on multiple products, highly divergent ranking compared to the rest, multiple similar reviews in a short amount of time, name of the reviewer …)
	* Task b : See the evolution of reviews with time, categories etc.

4. _Draft for the report_ : We plan here to make a website to clearly display the result of our data analysis. Nevertheless because we aren't sure yet of what type of interesting results we will have at the end we can only make assumptions and this part will most Certainly be reshaped once we gain a bit of traction on the data exploration.
	* Task a : On the first page display the major findings about the reviews and their caracteristics (being as visual as possible)
	* Task b : We would really like to take a few products as example to extrapolate our finding on the Herding effect to be able to give a visual representation of our findings. 
	* Task c : Then we will try to explain how this happens on the entire dataset we considered.
	* Task d : Try to have a time dependent slider to show the evolution of reviews with time.

# Dataset
We do not plan on using another dataset to enrich this one. But we might want to enrich it using amazon website and links to the product to get location data for our reviews and/or products. 

# A list of internal milestones up until project milestone 2
![](ada-milestones.png)

# Questions for TAs
We wanted to have your insights on a few key points for this project :

* First of all do you think that we are reasonnable enough with this first draft, we are not sure about what we are expected to produce but are satisfied by the subjects that we have carved out of this.
* We really want to do something very visual and have yet to come up with ways to make this interactive to present in our story. Would you have any recommandation In particular for Task 4.a ?
* About task 3.a we do not think yet that we will use machine learning because it is only a subtask of this 3rd part (but also because we do not have labels to train on and here clustering reviews would maybe not be conclusive), is it still enough to consider arbitrary set of rules that we think define a fraudulent review ?
