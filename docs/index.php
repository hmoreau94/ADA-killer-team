<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>ADA | How do reviews shape our experience on Amazon?</title>

	<!--pageMeta-->

	<!-- Lib CSS -->
	<link href="//fonts.googleapis.com/css?family=Rancho|Open+Sans:400,300,300italic,400italic,600,600italic,700,800italic,700italic,800" rel="stylesheet">
	<link href="minify/rgen_min.css" rel="stylesheet">
	<link href="css/custom.css" rel="stylesheet">

	<!-- Favicons -->
	<link rel="icon" href="images/favicon.png">
	<link rel="apple-touch-icon" href="images/favicon.png">
	<link rel="apple-touch-icon" sizes="72x72" href="images/favicon.png">
	<link rel="apple-touch-icon" sizes="114x114" href="images/favicon.png">

	<!-- HTML5 shim, for IE6-8 support of HTML5 elements. All other JS at the end of file. -->
	<!--[if lt IE 9]>
	<script src="js/html5shiv.js"></script>
	<script src="js/respond.min.js"></script>
	<![endif]-->
	<!--[if IE 9 ]><script src="js/ie-matchmedia.js"></script><![endif]-->

	<style type="text/css">
		.text-ada {
/*			color: #304d70;
*/			background: linear-gradient(45deg, #576B84 40%, #23314D 100%);
			  -webkit-background-clip: text;
			  -webkit-text-fill-color: transparent;
		}

		.other-section-1 ol>li.active {
    		background-color: white;
    		border-radius: 5px;
		}
		.other-section-1 ol>li.active .iconwrp {
    		color: #304d70;
		}
		.other-section-1 ol>li>i, .other-section-1 ol>li>.iconwrp {
			color: #304d70;
		}
		.other-section-1 ol>li .info {
			color: #1f2229;
		}
		.title-sub {
			font-size: 17px;
		}
		.footer-section-6 img:hover {
			opacity: 1;
		}
		.panel-hover:hover {
			background-color: #eee;
		}
		@media (min-width: 992px) {
			.equal, .equal > div[class*='col-'], .equal > div[class*='col-'] > .panel-default {  
				display: -webkit-box;
				display: -moz-box;
				display: -ms-flexbox;
				display: -webkit-flex;
				display: flex;
				flex: 1 1 auto;
			}
			.equal > div[class*='col-'] > .panel-default > .panel-body {
				width:100%;
			}
		}
	</style>
</head>
<body>
<div id="page">
	
	<!-- Navigation -->
	<nav class="nav-wrp nav-1 dark" data-glass="y" data-sticky="y">
		<div class="container">
			
			<div class="nav-header">
				<a class="navbar-brand" href="#"><img src="images/dlab.png" alt="Brand logo"></a>
				<a class="nav-handle" data-nav=".nav"><i class="fa fa-bars"></i></a>	
			</div>
			
			<div class="nav vm-item">
				<ul class="nav-links">
					<li><a href="#detecting">Detecting similar books</a></li>
					<li><a href="#correlation">Correlation analysis</a></li>
					<li><a href="#herding">Herding Effect analysis</a></li>
					<li><a href="#recommendations">Recommendations</a></li>
				</ul>
			</div><!-- /.nav --> 
			
		</div><!-- /.container --> 
	</nav><!-- /.nav-wrp -->

	<section id="home" class="intro-section intro-section-14" style="border: none">
        <div class="info-wrp vm-item">
            <div class="carousel-widget owl0" id="owl0" data-items="1" data-itemrange="false" data-tdrag="false" data-mdrag="false" data-pdrag="false" data-autoplay="true" data-in="flipInX" data-loop="true" style="opacity: 1;">

                <div class="">
                    <div class="item">
                        <h2 class="main-text">How do reviews shape our experience on Amazon?</h2>
                        <p class="sub-text">
                            <i class="fa fa-star" aria-hidden="true"></i>
    						<i class="fa fa-star" aria-hidden="true"></i>
    						<i class="fa fa-star" aria-hidden="true"></i>
    						<i class="fa fa-star" aria-hidden="true"></i>
    						<i class="fa fa-star" aria-hidden="true"></i>
    						<br>
    						<br>
                        	<i>Applied Data Analysis @ EPFL</i>
                        </p>
                    </div>
                </div>
            </div>
            <!-- <a href="#concept" class="btn btn-lg mr-t-40 btn-line light">Concept</a> -->
        </div><!-- /.container -->
        <div class="bg-section bg-cover bg-cc full-wh" data-bg="images/nyc3.jpg" style="background-image: url(&quot;images/nyc3.jpg&quot;);">
            <b class="full-wh" style="background-color: rgba(255, 255, 255, 0);" id="particles-js"><canvas class="particles-js-canvas-el" style="width: 100%; height: 100%;" width="3360" height="1798"></canvas></b>
            <!-- BACKGROUND VIDEO -->
            <!-- <a class="videobg" data-property="{videoURL:'dorZ3vag5PI',containment:'.intro-section-14 .bg-section',showControls:true, autoPlay:true, loop:true, vol:50, mute:true, startAt:10, opacity:1, addRaster:true, quality:'default', optimizeDisplay:true}"></a> -->
        </div>
    </section>

	<section style="border:none; padding-bottom: 0px;">
		<div class="container">
			<div class="row">	
				<div class="col-md-12">
					<h2 class="title edit-item edit-content" data-sandboxid="tmp-rgnxL0">Introduction</h2>
					<div class="spacer s2"></div>
					<div class="spacer s0" id="trigger1"></div>
					<p class="title-sub text-justify">
						&emsp;&emsp; Amazon has become one of the most important players when it comes to online shopping. Starting from a book online marketplace it now proposes many categories of products ranging from electronics to clothes. Given this high diversity of products and most importantly the very wide offering of the website, Amazon has been particularly popular thanks to its community of users. This community provides a human-powered recommender system.
					</p>

					<div class="text-center" style="margin-bottom: 60px;margin-top: 60px;">

						<div id="imagesequence" class="text-center">
							<img id="review"/ style="width: 70%; border-radius: 10px;box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;" data-toggle="tooltip">
						</div>
						<div class="spacer s2"></div>
                	</div>
						<p class="title-sub edit-item edit-content text-justify" data-sandboxid="tmp-rgIVa0">
							Thanks to the many reviews that each product receives, customers can have a better feeling of the items that they are trying to buy. This is essential as they can’t physically interact with those. 
						</p>

						<div class="row">
							<div class="col-sm-6">
								<div class="info-box info-box5 edit-item text-center" data-sandboxid="tmp-rgeIE0" data-selector=".edit-item">
									<div class="info edit-item text-center" data-sandboxid="tmp-rgyvA0" data-selector=".edit-item">
										<h2 style="margin-bottom: 10px;"><i class="fa fa-book edit-item text-ada" data-sandboxid="tmp-rgGwg0" data-selector=".edit-item" rgen-id="rg49o"></i> 2'370'585</h2>
										<p class="sub-txt edit-item edit-content" data-sandboxid="tmp-rg4u31" data-selector=".edit-content" rgen-id="rghwi">Books</p>
									</div>
								</div><!-- /.info-box -->		
							</div>

					
							<div class="col-sm-6">
								<div class="info-box info-box5 edit-item text-center" data-sandboxid="tmp-rgeIE0" data-selector=".edit-item">
									<div class="info edit-item text-center" data-sandboxid="tmp-rgyvA0" data-selector=".edit-item">
										<h2 style="margin-bottom: 10px;"><i class="fa fa-commenting-o edit-item text-ada" data-sandboxid="tmp-rgGwg0" data-selector=".edit-item" rgen-id="rg49o"></i> 22'507'155</h2>
										<p class="sub-txt edit-item edit-content" data-sandboxid="tmp-rg4u31" data-selector=".edit-content" rgen-id="rghwi">Reviews</p>
									</div>
								</div><!-- /.info-box -->		
							</div>		
						</div>		

						<p class="title-sub edit-item edit-content text-justify">
							As users we have experienced how influenced we are by such reviews. They are in a way the only filter that help us assess the quality of a product. How many times have we decided to buy a product rather than another because many people judged the first one to be inherently better than the second? That’s why we came to wonder how reliable were those reviews. 
						</p>

				</div>
			</div>
		</div>
	</section>

	<!-- Features -->
	<section class="feature-section feature-section-4 edit-item" data-sandboxid="tmp-rgxAj0" style="margin-top: 0px;padding-top: 50px;">
		<div class="full-wh w-50 bg-section edit-item" data-sandboxid="tmp-rge8G0"><img src="images/amazon.jpg" class="img-responsive edit-item" alt="Screen image" data-sandboxid="tmp-rg4sa0"></div>
		<div class="container">
			<div class="row">
				<div class="col-md-6">
					<div class="content edit-item" data-sandboxid="tmp-rgmj10">

						<p class="title-sub edit-item edit-content text-justify">
							&emsp;&emsp; By reliable we do not plan on detecting fake reviews. We are trying to detect what is called the Herding Effect. This effect is exactly what makes us choose a product according to what our peers have chosen. But also it means that when the previous buyers have reviewed a product it is likely that our review will be influenced by this latter. This is what we will try to investigate in this project by looking at how the first review of a book influences the following ones. 
						</p>

						<p class="title-sub edit-item edit-content text-justify" style="margin-bottom: 0px;">
							We have decided to focus on Amazon books as those make a great product to study the Herding effect as they are often available in different editions which do not modify the content (or very slightly). Therefore as we will see in the "Natural Experiment" section, we will be able to find pairs of identical books with different first review to see how the following ones relate.
						</p>

					</div><!-- /.content -->
				</div><!-- /.col-lg-6 -->
				<div class="col-md-6"></div>
			</div><!-- /.row -->
		</div><!-- /.container -->
	</section><!-- /.feature-section -->

    <section class="bg-gray content-section content-section-common" id="concept">
        <div class="container">
            <div class="flex-row">
                <div class="flex-col-md-12">
                	<h2>A Natural Experiment</h2>
                	<p class="title-sub text-justify">
                		&emsp;&emsp; Fortunately for us, in this study we have encountered what we call a “Natural Experiment”. A Natural Experiment in our case, refers simply to the fact that each subject/element concerned by this analysis (the pair of similar books for instance) have a specific first rating and that this first rating is <strong>determined by nature</strong> or by other factors outside the control of this study. We have indeed for each pair of similar books a pseudo-random chance that each of their rating is either good, bad or average. The process governing the assignment of a first rating being good, medium or bad can be arguably considered as a random assignment.
                	</p>

                	<p class="title-sub text-justify">
						&emsp;&emsp; Now to understand its importance and why it is such a great news that our study could be considered as a “Natural Experiment”, let’s take a counter example: <strong>A famous tobacco company</strong>, after selling for many years deadly products, felt bad about what they did and developed a new chewing gum solution that could help people to quit smoking. They wanted to try their new solution to be able to show to the world its great results. For that they designed an experiment in which they compared their new chewing gum with a competitor’s patch solution. In order to do so, they gathered 200 smokers: sampled such that 100 consumers want to quit and therefore will try the chewing gum solution while the hundred others didn't show any interest in stopping and were chosen to try the competitor's solution and to later compare to the first group. For a few weeks the 100 first participants took the chewing gum while the other 100 took the patch solution. 
					</p>
					<div class="row" style="margin-bottom: 30px;margin-top: 60px;">
						<div class="col-md-6">
							<div class="info-box info-box4 edit-item" data-sandboxid="tmp-rgM9y1">
								<div class="img edit-item" data-sandboxid="tmp-rgoZY1" style="background-color: white;">
									<i class="fa fa-users text-ada"></i>
								</div>
								<div class="info edit-item" data-sandboxid="tmp-rg4x41">
									<h2 class="hd edit-item edit-content" data-sandboxid="tmp-rgh6p2">Group 1 - Wants to quit smoking</h2>
									<p class="sub-txt edit-item edit-content" data-sandboxid="tmp-rgsM32">
										Trying out the chewing gum
										<br>
										Results: 10% smoking
									</p>
								</div>
							</div><!-- /.info-box -->
						</div>
						<div class="col-md-6">
							<div class="info-box info-box4 edit-item" data-sandboxid="tmp-rgM9y1">
								<div class="img edit-item" data-sandboxid="tmp-rgoZY1" style="background-color: white">
									<i class="fa fa-users text-ada"></i>
								</div>
								<div class="info edit-item" data-sandboxid="tmp-rg4x41">
									<h2 class="hd edit-item edit-content" data-sandboxid="tmp-rgh6p2">Group 2 - Didn’t show any interest in quitting smoking</h2>
									<p class="sub-txt edit-item edit-content" data-sandboxid="tmp-rgsM32">
										Trying the patch solution from the competitor
										<br>
										Results: 90% smoking
									</p>
								</div>
							</div><!-- /.info-box -->
						</div>
					</div>
                	<p class="title-sub text-justify">
					At the end of the experiment, the tobacco company comes with their results. They found out that only 10 participants out of 100 in the first group smoke one or more cigarettes during the whole experiment while in the second group 90 participants out of 100 smoked. By comparing the 2 groups they declared to have obtained outstanding results proving that their product is 9 times more effective than what the competition proposes. Now if we think about it, are those results really trustworthy or did the design of the experiment completely bias its results ? 
					</p>

                	<p class="title-sub text-justify">
						Well as you may have already guessed, the <strong>results are completely biased</strong> by the subject selection process in this case. The smoking company chose, for testing its product, participants that already wanted to quit smoking. Those had from the beginning a higher probability of quitting than those that showed zero interest in doing so. In a “natural experiment”, the selection of participants would have been determined by nature hence be randomised or at least outside the control of the experiment. So a “natural experiment” would have led to more meaningful results and would have guaranteed that the study has not been influenced by subject selection or category assignment. This is what we are happy to have here in this study.
                	</p>

                	<p class="title-sub text-justify">
                		It might still be unclear to you how do we plan to have a natural experiment in our investigation. Well as explained previously, books come in different formats. For example think about a book that is proposed in both paperback, hardcover and e-book or even the same book that was published by different companies. Then we will have the same content but different reviews. If we succeed to find two books that are similar then nature will have decided on which reviews each of them will have received and this independently of our project. We will have in such setup two identical book (at least in term of content) and different initial reviews, which is exactly what we need.
                	</p>

                	<div class="row">
                		<div class="col-md-2"></div>
						<div class="col-md-4">
							<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;background-color: white;">
								<div class="panel-body" style="padding: 15px;">
									<h3 class="text-ada" style="margin-bottom: 0px;">Book A</h3>
		        					<span class="title-sub"><i>
		        						<i class="fa fa-star" aria-hidden="true" style="color:#F6B940"></i>
		        						<i class="fa fa-star" aria-hidden="true" style="color:#F6B940"></i>
		        						<i class="fa fa-star" aria-hidden="true" style="color:#F6B940"></i>
		        						<i class="fa fa-star" aria-hidden="true" style="color:#F6B940"></i>
		        						<i class="fa fa-star" aria-hidden="true" style="color:#F6B940"></i>
		        						<br>
		        						Reviews
		        					</i></span>
								</div>
							</div>
						</div>
						<div class="col-md-4">
							<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;background-color: white;">
								<div class="panel-body" style="padding: 15px;">
									<h3 class="text-ada" style="margin-bottom: 0px;">Book B</h3>
		        					<span class="title-sub"><i>
		        						<i class="fa fa-star" aria-hidden="true" style="color:#F6B940"></i>
		        						<i class="fa fa-star" aria-hidden="true" style="color:#F6B940"></i>
		        						<i class="fa fa-star" aria-hidden="true" style="color:#F6B940"></i>
		        						<i class="fa fa-star-o" aria-hidden="true" style="color:#F6B940"></i>
		        						<i class="fa fa-star-o" aria-hidden="true" style="color:#F6B940"></i>
		        						<br>
		        						Reviews
		        					</i></span>
								</div>
							</div>
						</div>
                		<div class="col-md-2"></div>
					</div>

                </div>
            </div>
        </div>
    </section>
	
	<!-- Counter section -->
	<section class="counter-section counter-section-2 edit-item" data-sandboxid="tmp-rg4nd0">
		<div class="container z1">
			<div class="rw eq3 gt30 dark">

				<div class="cl">
					<div class="count-box count-box2 edit-item" data-sandboxid="tmp-rgZ601">
						<div class="icon edit-item" data-sandboxid="tmp-rgdnY1"><i class="fa fa-book" data-sandboxid="tmp-rg0ss1"></i></div>
						<div class="count-wrp"><b class="count">2370585</b></div>
						<h3 class="edit-item edit-content" data-sandboxid="tmp-rgLDl1">Books</h3>
					</div><!-- /.count-box -->
				</div>

				<div class="cl">
					<div class="count-box count-box2 edit-item" data-sandboxid="tmp-rgZ601">
						<div class="icon edit-item" data-sandboxid="tmp-rgdnY1"><i class="fa fa-clone" data-sandboxid="tmp-rg0ss1"></i></div>
						<div class="count-wrp">?</div>
						<h3 class="edit-item edit-content" data-sandboxid="tmp-rgLDl1">Similars books</h3>
					</div><!-- /.count-box -->
				</div>

				<div class="cl">
					<div class="count-box count-box2 edit-item" data-sandboxid="tmp-rgZ602">
						<div class="icon edit-item" data-sandboxid="tmp-rgdnY2"><i class="fa fa-commenting-o" data-sandboxid="tmp-rg0ss2"></i></div>
						<div class="count-wrp"><b class="count">22507155</b></div>
						<h3 class="edit-item edit-content" data-sandboxid="tmp-rgLDl2">Reviews</h3>
					</div><!-- /.count-box -->
				</div>

			</div><!-- /.row -->
		</div><!-- /.container -->
		<div class="full-wh bg-cover bg-cc edit-item" data-bg="images/books.jpg" style="background-image: url(&quot;images/books.jpg&quot;);" data-sandboxid="tmp-rgMbx0"><b class="full-wh overlay edit-item" data-sandboxid="tmp-rgxF60"></b></div>
	</section><!-- /.counter-section -->

	<section style="margin-top: 0px; padding-top: 0px;" id="detecting">
		<div class="container">
			<div class="row">
				<div class="col-md-12">
					<h2 style="padding-top: 100px;">Detecting similar books</h2>
				</div>	
			</div>

			<div class="row">
				<div class="col-md-8">
						<h3>1. Too many books</h3>
	                	<p class="title-sub text-justify">
	                		&emsp;&emsp; Unfortunately, we are working on a very large dataset. We started our project by discarding the books for which we didn’t have enough reviews to study the Herding Effect later on. But this step left us with approximately 625’682 books. And this is quite problematic, let’s consider that we would like to match books based only on their titles. We would need to compare them pairwisely and to check how similar they are. 
	                	</p>
	                	<p class="title-sub text-justify">
							A popular way to compare the similarity of two strings is to use a Mathematical measure called Jaccard Similarity, to put it simply it represents the number of words that are common between the two strings divided by the size of the dictionary used by the two strings. If we had to compute this similarity over all those books we would need to compute it <strong>195,738,669,721 times</strong>. While this number might not be very tangible, the time it takes to compute clearly is : it represents more than <strong>655 days, that is a bit less than 2 years</strong> to run on a consumer grade computer. 
	                	</p>
	                	<p class="title-sub text-justify">
							The goal of the project was to be done in less than a month and therefore this was (slightly) concerning.
	                	</p>
				</div>
				<div class="col-md-4 text-center">
					<video autoplay loop style="width: 100%;margin-top: 120px;" name="Books" src="videos/books1.m4v"></video>

<!-- 					<div class="spacer s2"></div>
					<div class="spacer s0" id="trigger"></div>
					<div id="imagesequence" class="text-center">
						<img id="myimg"/ style="border: 1px solid black;width: 100%"><br>
					</div>
					<div class="spacer s2"></div> -->
				</div>
			</div>
			<hr>
			<div class="row" style="margin-top: 50px;">
				<div class="col-md-12">
					<h3>2. The power of Hashing</h3>
                	<p class="title-sub text-justify">
                		&emsp;&emsp; We needed to derive a strategy to be able to compare so many books. We used a technique called <strong>Locality sensitive hashing</strong>. The scope of this article isn’t to example the fascinating maths behind the tools used for the analysis but more to give a high level understanding of our experimental protocol, therefore we will try to highly vulgarize it. 
                	</p>
                	<p class="title-sub text-justify">
                		Suppose that we could color a title based only on the words it contains. Each letter would be associated with a color, a word would have the same color than the mix of colors from its characters, and then a sentence would be itself associated with the mix of colors from the words it contains. Then it would be very likely that two titles with the same color would be similar. 
                	</p>
                	<p class="title-sub text-justify" style="margin-bottom: 0px;">
                		Locality sensitive hashing works like a coloring scheme. It assigns to each title a given value, the probability that this value is the same for two titles is very high if the titles are similar. Therefore we only need to compute this value for each title and to then compare using any method we want only the titles that have the same value. 
                	</p>
                </div>
				<div class="col-md-6 col-md-offset-3 text-center">
					<video autoplay loop style="width: 100%;" name="Books" src="videos/books2.m4v"></video>
				</div>
				<div class="col-md-12">
                	<p class="title-sub text-justify">
                		Now let’s talk running time, in order to compute this value for each title it takes about <strong>1 minute and 30 seconds</strong> and it yields 14,524 groups of books that are possibly similars. Those groups span over less than 35,742 books. We have successfully reduced the size of our dataset while keeping all the books that have at least one similar product.
                	</p>
				</div>
				<div class="col-md-4">
				</div>
			</div>
			<hr>
			<div class="row" style="margin-top: 50px;">
				<div class="col-md-12">
					<h3>3. Refining our results using an external API</h3>
                	<p class="title-sub text-justify">
                		&emsp;&emsp; Once we have significantly reduced the number of books that we work on it is time to check whether or not those candidate similars are indeed similar or not. In order to achieve such goal we needed to obtain more details concerning each book. The original dataset was particularly poor regarding products metadatas. We didn’t have much information on the books and we therefore decided to use Amazon Product advertising API to obtain such information. Once this was done we obtained strategic details : authors, publisher, ISBN, binding and edition.
                	</p>

				</div>
			</div>
			<div class="row">
				<div class="col-md-6">
                	<p class="title-sub text-justify">
                		Using those we compared each book in the similar books from last step using the authors list of the books. We didn’t want to be too restrictive on the authors because two similar books A and B might not have the exact same authors list for numerous reasons:
	                	<br>
	                	<br>
						&emsp;&emsp;  <i class="fa fa-question text-ada"></i> one of the authors was forgotten in one of the authors’ list
						<br>
						&emsp;&emsp;  <i class="fa fa-pencil text-ada"></i> an authors name contained a typo
						<br>
						<br>
						Hence we had to again think of a strategy. The two lists of authors might have different lengths. We started to “clean” those lists by removing the accents and putting the name to lower cases.
						<br>
						<br>
						Then we used what is called the relative <strong>Levenstein distance</strong>. This metric compute the proportion of the longuest string’s charachters that we have to modify (or delete) in order to obtain the shortest one.
					</p>
				</div>
				<div class="col-md-6">
					<div class="row equal">
						<div class="col-md-6">
							<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
								<div class="panel-body" style="padding: 15px;">
									<h3 class="text-ada">Book A</h3>
		        					<span class="title-sub"><i>
		        						(John) Doe - Robert West - Martin Vetterli
		        						<hr>
		        						<span data-toggle="tooltip" title="Authors normalised">john doe - robert west - martin vetterli</span>
		        					</i></span>
								</div>
							</div>
						</div>
						<div class="col-md-6">
							<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
								<div class="panel-body" style="padding: 15px;">
									<h3 class="text-ada">Book B</h3>
		        					<span class="title-sub"><i>
		        						Bob West - John D. Doe
		        						<hr>
		        						<span data-toggle="tooltip" title="Authors normalised">bob west - john d doe</span>
		        					</i></span>
								</div>
							</div>
						</div>
					</div>
					<div class="row">
						<div class="col-md-12">
							<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
								<div class="panel-body" style="padding: 15px;">
		        					<span class="title-sub"><i>
		        						<strong data-toggle="tooltip" title="Levenstein distance">0.28</strong> john doe | john d doe
		        						<hr>
		        						<strong data-toggle="tooltip" title="Levenstein distance">0.35</strong> robert west | bob west 
		        					</i></span>
								</div>
							</div>
						</div>
					</div>
				</div>
            </div>
			<div class="row">
				<div class="col-md-12">
                	<p class="title-sub text-justify">
						Then it will compute the distance between the two lists as the mean of the distance between the matched authors : <strong>0.315</strong> and will decide that the two are identical if this distance is lower than a threshold that we optimised empirically.
						Using this method we <strong>reduced the number of groups of candidate similars to 5,882</strong>. 
                	</p>

				</div>
				<div class="col-md-4">
					
				</div>
			</div>

			<hr>
			<div class="row" style="margin-top: 50px;">
				<div class="col-md-12">
					<h3>4. Final Filtering, coming back to titles</h3>
                	<p class="title-sub text-justify">
                		&emsp;&emsp; The last step allowed us to get rid of books with similar titles but that came from different authors. Finally we wish to apply a final filter in order to reduce as much as possible de number of false positive (i.e. books that we declare as matching but are indeed different). In order to be very restrictive, we will consider the titles of the books inside the same similarity bin. The problem that might remain is that even though the book titles are now very similars they might differ by even a small proportion and still be completely different:

                	</p>
                </div>

				<div class="col-md-3">
					<div class="info-box info-box7 edit-item" data-sandboxid="tmp-rgH721">
						<div class="img edit-item" data-sandboxid="tmp-rg0zK1"><i class="fa fa-copy edit-item text-ada" data-sandboxid="tmp-rgobv1"></i></div>
						<div class="info edit-item" data-sandboxid="tmp-rg4km1">
							<span class="title-sub" data-sandboxid="tmp-rgevG1">Different Tomes</span>
						</div>
					</div>	
				</div>

				<div class="col-md-3">
					<div class="info-box info-box7 edit-item" data-sandboxid="tmp-rgH721">
						<div class="img edit-item" data-sandboxid="tmp-rg0zK1"><i class="fa fa-graduation-cap edit-item text-ada" data-sandboxid="tmp-rgobv1"></i></div>
						<div class="info edit-item" data-sandboxid="tmp-rg4km1">
							<span class="title-sub" data-sandboxid="tmp-rgevG1">Similar educational books</span>
						</div>
					</div>	
				</div>

				<div class="col-md-3">
					<div class="info-box info-box7 edit-item" data-sandboxid="tmp-rgH722">
						<div class="img edit-item" data-sandboxid="tmp-rg0zK2"><i class="fa fa-pencil edit-item text-ada" data-sandboxid="tmp-rgobv2"></i></div>
						<div class="info edit-item" data-sandboxid="tmp-rg4km2">
							<span class="title-sub" data-sandboxid="tmp-rgevG1">Typos & Small differences</span>
						</div>
					</div>	
				</div>

				<div class="col-md-3">
					<div class="info-box info-box7 edit-item" data-sandboxid="tmp-rgH723">
						<div class="img edit-item" data-sandboxid="tmp-rg0zK3"><i class="fa fa-database edit-item text-ada" data-sandboxid="tmp-rgobv3"></i></div>
						<div class="info edit-item" data-sandboxid="tmp-rg4km3">
							<span class="title-sub" data-sandboxid="tmp-rgevG1">Others</span>
						</div>
					</div>	
				</div>

				<div class="col-md-12">
                	<p class="title-sub text-justify">
						Suppose that we have the following similarity bin :
					</p>
				</div>

				<div class="col-md-4">
					<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
						<div class="panel-body" style="padding: 15px;">
							<h4 class="text-ada">The Walking Dead: The Fall of the Governor: Part One</h4>
        					<span class="title-sub"><i>
        						Robert Kirkman - Jay Bonansinga
        					</i></span>
        				</div>
        			</div>
				</div>
				<div class="col-md-4">
					<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
						<div class="panel-body" style="padding: 15px;">
							<h4 class="text-ada">The Walking Dead: The Fall of the Governor: Part Two</h4>
        					<span class="title-sub"><i>
        						Robert Kirkman - Jay Bonansinga
        					</i></span>
        				</div>
        			</div>
				</div>
				<div class="col-md-4">
					<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
						<div class="panel-body" style="padding: 15px;">
							<h4 class="text-ada">The Walking Dead: The Fall of the Governor: Part One</h4>
        					<span class="title-sub"><i>
        						Robert Kirkman
        					</i></span>
        				</div>
        			</div>
				</div>
				<div class="col-md-12" style="margin-top: 20px;">
                	<p class="title-sub text-justify">
						The algorithm will again normalize the titles by getting rid of the symbols it contains as well as putting them in lower case:
					</p>
				</div>
				<div class="col-md-6 col-md-offset-3">
					<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
						<div class="panel-body" style="padding: 15px;">
							<p class="title-sub" style="margin-bottom: 0px;">the walking dead the fall of the governor part one</h4>
							<hr>
							<p class="title-sub" style="margin-bottom: 0px;">the walking dead the fall of the governor part two</h4>
							<hr>
							<p class="title-sub" style="margin-bottom: 0px;">the walking dead the fall of the governor part one</h4>
        				</div>
        			</div>
				</div>
				<div class="col-md-12" style="margin-top: 20px;">
                	<p class="title-sub text-justify">
						Then it will consider the set of words of each title and consider two titles to be identical if the symetric difference of such set if empty (meaning that one of the set is entirely contained in the other).
					</p>

					<p class="title-sub text-justify">
						&emsp;&emsp; Thanks to all these steps we have now reduced our number of similarity bins down to <strong>3,173</strong>. With more time to do the matching we think that we could have applied more filters in order to match books with much more confidence. We have decided to be very restrictive here because of the time constraints but once we obtained the ISBN of different books it would be possible to access a database where titles and author names would be consistent and could therefore match much more efficiently.
					</p>
				</div>				
            </div>
		</div>
	</section>

	<section class="bg-gray other-section other-section-1 edit-item" data-sandboxid="tmp-rgfCv0" id="correlationr">
		<div class="container text-left">
			<h2 style="color: #1f2229">How influenced are we regarding reviews when it comes to buying products</h2>
	        <p class="title-sub text-justify" style="color: #1f2229; text-align: justify;">
	    		From these plot we can hardly deduce anything, nevertheless we can go a bit further by trying to guess a ranking based on the review average. Then plot it against the deduced rank to see how it correlates to it. If the sales rank is depending heavily on the review grade then it should have a pearson correlation close to 1.
	    	</p>
			<div class="row eqh">
				<div class="col-md-5 l">
					<ol>
						<li class="active edit-item" data-img="images/correlations/correlation1.png" data-sandboxid="tmp-rgoSe0">
							<div class="iconwrp edit-item" data-sandboxid="tmp-rgHXd0"><i class="fa fa-trophy edit-item text-ada" data-sandboxid="tmp-rgGnR0"></i></div>
							<p class="info edit-item edit-content" data-sandboxid="tmp-rgBuU1">Sales Rank</p>
						</li>
						<li data-img="images/correlations/correlation2.png" class="edit-item" data-sandboxid="tmp-rgoSe1">
							<div class="iconwrp edit-item" data-sandboxid="tmp-rgHXd1"><i class="fa fa-line-chart edit-item text-ada" data-sandboxid="tmp-rgGnR1"></i></div>
							<p class="info edit-item edit-content" data-sandboxid="tmp-rgBuU2">Continuous Sales Rank</p>
						</li>
					</ol>
				</div><!-- /.col-md-5 -->
				<div class="col-md-6 col-md-offset-1 r">
					<img src="images/correlations/correlation1.png" alt="Image" class="img-responsive vm-item edit-item">
				</div><!-- /.col-md-6 -->
			</div>
		</div><!-- /.container -->
	</section><!-- /.other-section -->

    <section class="content-section content-section-common" id="herding" style="border: none">>
        <div class="container">
        	<h2>Preparing the data</h2>
        	<p class="title-sub text-justify">
        		&emsp;&emsp; After matching and gathering many pairs of very similar books and in order to study the effect of a first review over the next ones, a step we had to realise was to find out what was the rating of the first review for each book (Amazon possible ratings are 1, 2, 3, 4 and 5). From that first rating we had to determine a way to be able to put each book into a specific category. Having categories such has high first review or low first review allows us to <strong>separate our data into different groups</strong> that, we will then be able to compare throughout the study. Two decisions were made  establish the different categories we were willing to use. First we had to decide how many categories we wanted. Deciding the number of categories was simply a trade-off between high number of categories to confirm our results with low numbers of books inside them (low reliability of each category) and low number of categories to confirm our results but high number of books inside each (high reliability of each category). We settled for three categories as follows: 
        	</p>

        	<div class="row equal">
        		<div class="col-md-4 text-center">
        			<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
						<div class="panel-body" style="padding: 15px;">
							<h3 class="text-success">H</h3>
        					<span class="title-sub"><i>Books with high first review</i></span>
						</div>
					</div>
        		</div>
        		<div class="col-md-4 text-center">
        			<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
						<div class="panel-body" style="padding: 15px;">
							<h3 class="text-warning">M</h3>
        					<span class="title-sub"><i>Books with medium first review</i></span>
						</div>
					</div>
        		</div>
        		<div class="col-md-4 text-center">
        			<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
						<div class="panel-body" style="padding: 15px;">
							<h3 class="text-danger">L</h3>
        					<span class="title-sub"><i>Books with low first review</i></span>
						</div>
					</div>	
        		</div>
        	</div>

        	<p class="title-sub text-justify" style="margin-top: 20px;">
        		Now it is good to know which categories we want but the second decision we had to face was: which books are we going to put into which category. To answer that question we simply looked at the repartition of the first ratings we had among all the books. 
        	</p>

        	<div class="row">
        	    <div class="col-md-6" style="padding-right: 40px;">
        			<canvas id="myChart" style="width: 100%;"></canvas>
        		</div>
        		<div class="col-md-6">
        			<p class="title-sub text-justify" style="margin-top: 20px;">
        				We saw that it was not going to be easy to have balanced categories as an important part of the books received 5 star ratings. Nevertheless the most balanced we could come up with was to consider low ratings to be ratings with at most 3 stars and medium ratings those with 4 stars. And therefore obtained:
		        	</p>
        		</div>
        	</div>

        	<div class="row equal" style="margin-top: 20px;">
        		<div class="col-md-4 text-center">
        			<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
						<div class="panel-body" style="padding: 15px;">
							<h3 class="text-success">H</h3>
        					<span class="title-sub"><i>Books with a 5 star first review</i></span>
        					<br>
        					<i class="fa fa-star" aria-hidden="true" style="color: #FAC546"></i>
        					<i class="fa fa-star" aria-hidden="true" style="color: #FAC546"></i>
        					<i class="fa fa-star" aria-hidden="true" style="color: #FAC546"></i>
        					<i class="fa fa-star" aria-hidden="true" style="color: #FAC546"></i>
        					<i class="fa fa-star" aria-hidden="true" style="color: #FAC546"></i>
						</div>
					</div>
        		</div>
        		<div class="col-md-4 text-center">
        			<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
						<div class="panel-body" style="padding: 15px;">
							<h3 class="text-warning">M</h3>
        					<span class="title-sub"><i>Books with a 4 star first review</i></span>
        					<br>
        					<i class="fa fa-star" aria-hidden="true" style="color: #FAC546"></i>
        					<i class="fa fa-star" aria-hidden="true" style="color: #FAC546"></i>
        					<i class="fa fa-star" aria-hidden="true" style="color: #FAC546"></i>
        					<i class="fa fa-star" aria-hidden="true" style="color: #FAC546"></i>
        					<i class="fa fa-star-o" aria-hidden="true"></i>        					
						</div>
					</div>
        		</div>
        		<div class="col-md-4 text-center">
        			<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
						<div class="panel-body" style="padding: 15px;">
							<h3 class="text-danger">L</h3>
        					<span class="title-sub"><i>Books with a 3, 2 or 1 star first review</i></span>
        					<br>
        					<i class="fa fa-star" aria-hidden="true" style="color: #FAC546"></i>
        					<i class="fa fa-star" aria-hidden="true" style="color: #FAC546"></i>
        					<i class="fa fa-star" aria-hidden="true" style="color: #FAC546"></i>
        					<i class="fa fa-star-o" aria-hidden="true"></i>
        					<i class="fa fa-star-o" aria-hidden="true"></i>        					
						</div>
					</div>	
        		</div>
        	</div>

        	<p class="title-sub text-justify" style="margin-top: 20px;">
				&emsp;&emsp; What is interesting in our analysis is to study a pair of very similar books and compare for that specific pair of books what are the ratings after a high first rating compared to the ratings after a low first rating. To do so and once we were able to categorise each book according to their first rating among our 3 categories (high, medium or low), we wanted to spot which pair of books had a book starting with a high first review with another starting with a low first review to be able to compare the following ratings. That is where we created 6 groups of pairs of similar books and then compared each group. The groups were as follows: 
			</p>

        	<div class="row equal">
        		<div class="col-md-2 text-center">
        			<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
						<div class="panel-body" style="padding: 15px;">
							<h3 class="text-success">HH</h3>
        					<span class="title-sub"><i>both starting with high first rating</i></span>
						</div>
					</div>
        		</div>
        		<div class="col-md-2 text-center">
        			<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
						<div class="panel-body" style="padding: 15px;">
							<h3 class="text-warning">MM</h3>
        					<span class="title-sub"><i>both starting with medium first rating</i></span>
						</div>
					</div>
        		</div>
        		<div class="col-md-2 text-center">
        			<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
						<div class="panel-body" style="padding: 15px;">
							<h3 class="text-danger">LL</h3>
        					<span class="title-sub"><i>both starting with low first rating</i></span>
						</div>
					</div>	
        		</div>
        		<div class="col-md-2 text-center">
        			<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;border: 1px solid grey">
						<div class="panel-body" style="padding: 15px;">
							<h3><span class="text-success">H</span><span class="text-danger">L</span></h3>
        					<span class="title-sub"><i>starting with high and low first rating</i></span>
						</div>
					</div>	
        		</div>
        		<div class="col-md-2 text-center">
        			<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
						<div class="panel-body" style="padding: 15px;">
							<h3 class="text-danger"><span class="text-success">H</span><span class="text-warning">M</span></h3>
        					<span class="title-sub"><i>starting with high and medium rating</i></span>
						</div>
					</div>	
        		</div>
        		<div class="col-md-2 text-center">
        			<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
						<div class="panel-body" style="padding: 15px;">
							<h3 class="text-danger"><span class="text-warning">M</span><span class="text-danger">L</span></h3>
        					<span class="title-sub"><i>starting with medium and low first rating</i></span>
						</div>
					</div>	
        		</div>
        	</div>

        	<p class="title-sub text-justify" style="margin-top: 20px;">
				&emsp;&emsp; All these different groups allowed us to study and confirm the effect of a first review on a book being high, low or medium. The most interesting and promising group is probably the HL group as it is the one where we are supposed to observe a lot of difference between successive ratings as the first rating is very different for each pair of similar books. Other groups such as HH, MM, LL are more here just to confirm our results from the HL group as there is supposed to be no difference in the following ratings on these groups since they start with already a very similar rating. Let’s see if we can confirm these hypotheses with our results in the next part of this study.
        	</p>
        </div>
    </section>

	<section class="bg-gray">
		<div class="container">
			<div class="row">
				<div class="col-md-12">
					<h2>Results</h2>
					<div class="panel panel-default" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;background-color: white">
						<div class="panel-body" style="padding: 15px;">
						<div id="container" style="min-width: 310px; height: 600px; margin: 0 auto"></div>
						</div>
					</div>
				</div>	
			</div>
		</div>
	</section>

	<section class="" id="recommendations">
		<div class="container">
			<div class="row">
				<div class="col-md-12">

					<div class="row">
						 <div class="col-md-9">
							<h2>Recommendations</h2>

							<p class="title-sub text-justify">
								&emsp;&emsp; We have seen that the effect is actually quite noticeable at least on the short term, a single first rating can influence the following ones and therefore customers could base their choices on biased indicators. When we tried to look at the way Amazon manages such reviews we witnessed how careful they are with this sensible data. 
							</p>
							<p class="title-sub text-justify">
								First of all, the platform doesn’t display directly on the product page all the reviews that have been submitted for this given product. It choses to only display "Top Customer reviews" that are made of at most 8 reviews (depending on the length of such reviews). We tried to identify a pattern to understand how the website chose such reviews but time only allowed us to conduct an empirical ressearch. The only pattern that was identified is that first reviews to be displayed are those of the Verified purchaser, that is the reviews that have been sent after a purchase of the product at a price that is available for a majority of the community.  
							</p>
							<p class="title-sub text-justify">
								This might seem a bit strange … But indeed, Amazon has elaborated a strategy to ensure that reviews are unbiased and trustful. It has created in 2016 the <a class="btn-link" target="_blank" href="https://www.amazon.com/gp/vine/help">Vine Program</a>. This program proposes to trusted reviewers (based on their reviewer ranks) to receive free products (or important discounts) in exchange for their honest review. In fact, before the creation of this program, many vendors used incentivized reviewers in order to kickstart the sales of their product but after an article from <a class="btn-link" target="_blank" href="https://reviewmeta.com/blog/analysis-of-7-million-amazon-reviews-customers-who-receive-free-or-discounted-item-much-more-likely-to-write-positive-review/">Reviewmeta</a>  showing how those reviews were highly biased, the platform decided to severelly punish vendors that used such method.
							</p>	 	
						 </div>
						 <div class="col-md-3">
						 	<img src="images/reviews.png" style="margin-top:25px; width: 100%; border: 1px solid #ddd;border-radius: 5px;box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
						 </div>
					</div>
        			
					<p class="title-sub text-justify">
						Another example of Amazon’s protection against biased reviews is the way they compute their average review grade on the product. The firm doesn’t use the raw average of the past reviews but instead it uses  a machine learned formula that assigns different weights to each reviews depending on many factors such as: the number of reviews of the reviewer, the helpfulness of the review etc.
					</p>

					<div class="row">
						<div class="col-md-6">
							<a target="_blank" href="https://www.amazon.com/Enfants-terribles-Cocteau-Jean/product-reviews/B00E9WMZSU/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&filterByStar=one_star&reviewerType=all_reviews&pageNumber=1#reviews-filter-bar">
								<div class="panel panel-default panel-hover" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
									<div class="panel-body" style="padding: 15px;">
										<h3 class="text-ada">Les Enfants terribles</h3>
			        					<span class="title-sub"><i>Displayed: 3.3</i></span>
			        					<br>
			        					<span class="title-sub"><i>Computed: 3.71</i></span>
									</div>
								</div>	
							</a>
						</div>
						<div class="col-md-6">
							<a target="_blank" href="https://www.amazon.com/Shakespeare-French-Hamlet-Othello-Macbeth/dp/B00P022SWQ/ref=sr_1_13?s=books&ie=UTF8&qid=1513329797&sr=1-13&keywords=livre&refinements=p_n_feature_nine_browse-bin%3A3291438011%2Cp_72%3A1250224011">
								<div class="panel panel-default panel-hover" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 2px 10px 0px;">
									<div class="panel-body" style="padding: 15px;">
										<h3 class="text-ada">Shakespeare "French Edition"</h3>
			        					<span class="title-sub"><i>Displayed: 4.4</i></span>
			        					<br>
			        					<span class="title-sub"><i>Computed: 4.34</i></span>
									</div>
								</div>	
							</a>
						</div>
					</div>

					<p class="title-sub text-justify" style="margin-top: 20px;">
						A simple counter measure that we could think off would be to hide the reviews when there are not enough of them. Nevertheless, it is easy to understand that Amazon has commercial incentive to not follow this advice. Intuitively, reviews are very helpful to users and without reviews it becomes difficult for them to get an idea of the quality of the product. As the effect seem to last only for a few reviews, then we can see that amazon’s effort to provide the best assessment of the quality of a product is efficient but customers should however be careful not to rely exclusively on this indicator. Nowadays there exist a plethora of articles online that propose reviews of products and that are written by domain experts and/or journalists that can also be taken into consideration.
					</p>
				</div>	
			</div>
		</div>
	</section>

	<!-- Footer section -->
	<section class="footer-section footer-section-6">
		<div class="container">
			<div class="row" style="margin-bottom: 40px;">
				<div class="col-md-4 text-center">
					<a href="https://www.linkedin.com/in/hugomoreau/" target="_blank">
						<img src="images/team/hugo.png" class="img-circle" style="width: 100px; height: auto;">
						<br>
						Hugo Moreau	
					</a>
				</div>
				<div class="col-md-4 text-center">
					<a href="https://www.linkedin.com/in/guillaumeraille/" target="_blank">
						<img src="images/team/guillaume.jpg" class="img-circle" style="width: 100px; height: auto;">
						<br>
						Guillaume Raille
					</a>
				</div>
				<div class="col-md-4 text-center">
					<a href="https://www.linkedin.com/in/simonfavre/" target="_blank">
						<img src="images/team/simon.png" class="img-circle" style="width: 100px; height: auto;">
						<br>
						Simon Favre
					</a>
				</div>
			</div>
			<hr>
			<p class="copyright">Applied Data Analysis - Course project - December 2017</p>
			
		</div>
	</section>

</div>

<!-- Template -->
<script async src="js/Chart.min.js"></script>
<script src="minify/rgen_min.js"></script>
<script async src="js/rgen.js"></script>

<!-- Particules -->
<script src="js/particles/particles.js"></script>
<script src="js/particles/app.js"></script>

<!-- ScrollMagic -->
<script type="text/javascript" src="js/lib/highlight.pack.js"></script>
<script type="text/javascript" src="js/lib/modernizr.custom.min.js"></script>
<script type="text/javascript" src="js/examples.js"></script>
<script type="text/javascript" src="js/lib/greensock/TweenMax.min.js"></script>
<script type="text/javascript" src="scrollmagic/uncompressed/ScrollMagic.js"></script>
<script type="text/javascript" src="scrollmagic/uncompressed/plugins/animation.gsap.js"></script>
<script type="text/javascript" src="scrollmagic/uncompressed/plugins/debug.addIndicators.js"></script>
<script type="text/javascript" src="js/tracking.js"></script>


<!-- HighCharts -->
<script src="https://code.highcharts.com/highcharts.js"></script>
<script src="https://code.highcharts.com/highcharts-more.js"></script>
<script src="https://code.highcharts.com/modules/exporting.js"></script>

<!-- Format the data -->
<?php 
	$H_in_HL = json_decode(file_get_contents('json/H_in_HL_stats.json'), true); 
	$L_in_HL = json_decode(file_get_contents('json/L_in_HL_stats.json'), true); 
	foreach ($H_in_HL as $key => $value) {
		$H_in_HL_mean[$key] = [$key, round($H_in_HL[$key]['mean'], 2)];
		$H_in_HL_interval[$key] = [$key, round($H_in_HL[$key]['mean']-0.5*$H_in_HL[$key]['interval95'], 2), round($H_in_HL[$key]['mean']+0.5*$H_in_HL[$key]['interval95'], 2)];

		$L_in_HL_mean[$key] = [$key, round($L_in_HL[$key]['mean'], 2)];
		$L_in_HL_interval[$key] = [$key, round($L_in_HL[$key]['mean']-0.5*$L_in_HL[$key]['interval95'], 2), round($L_in_HL[$key]['mean']+0.5*$L_in_HL[$key]['interval95'], 2)];
	}
?>
<script type="text/javascript">
	
var H_in_HL_interval = <?php echo json_encode($H_in_HL_interval) ?>,
    H_in_HL_mean = <?php echo json_encode($H_in_HL_mean) ?>,
    L_in_HL_interval = <?php echo json_encode($L_in_HL_interval) ?>,
    L_in_HL_mean = <?php echo json_encode($L_in_HL_mean) ?>;

Highcharts.chart('container', {
	title: {
        text: 'Average Rating following H/L first rating (only 5 and 1 star)'
    },
	xAxis: {
		tickInterval: 1,
	},
    yAxis: {
        title: {
            text: null
        },
		tickInterval: 1,
		min: 1,
		max: 5,
    },
    plotOptions: {
    	series: {
    		marker: {
    			enabled: false,
    		}
    	}
    },
    tooltip: {
        crosshairs: true,
        shared: true
    },

    series: [{
        name: 'Mean H_in_HL',
        data: H_in_HL_mean,
        color: '#28B463',
    },{
        name: 'Interval H_in_HL',
        data: H_in_HL_interval,
        type: 'arearange',
        lineWidth: 0,
        linkedTo: ':previous',
        color: '#28B463',
        fillOpacity: 0.3,
        zIndex: 0,
        marker: {
            enabled: false
        }
    },
    {
        name: 'Mean L_in_HL',
        data: L_in_HL_mean,
        color: '#E74C3C'
    },{
        name: 'Interval L_in_HL',
        data: L_in_HL_interval,
        type: 'arearange',
        lineWidth: 0,
        linkedTo: ':previous',
        color: '#E74C3C',
        fillOpacity: 0.3,
        zIndex: 0,
        marker: {
            enabled: false
        }
    }]
});
</script>

<!-- ScrollMagic -->
<script>
	// define images
	var images1 = [
		"images/reviews/review1.png",
		"images/reviews/review2.png",
		"images/reviews/review3.png",
		"images/reviews/review4.png",
		"images/reviews/review5.png"
	];

	// TweenMax can tween any property of any object. We use this object to cycle through the array
	var obj1 = {curImg1: 0};

	// create tween
	var tween1 = TweenMax.to(obj1, 0.5,
		{
				curImg1: images1.length - 1,	// animate propery curImg to number of images
							roundProps: "curImg1",				// only integers so it can be used as an array index
							repeat: 0,									// repeat 3 times
							immediateRender: true,			// load first image automatically
							ease: Linear.easeNone,			// show every image the same ammount of time
			onUpdate: function () {
			$("#review").attr("src", images1[obj1.curImg1]); // set the image source
			}
		}
	);

	// init controller
	var controller = new ScrollMagic.Controller();

	// build scene
	var scene = new ScrollMagic.Scene({triggerElement: "#trigger1", duration: 400})
					.setTween(tween1)
					// .addIndicators() // add indicators (requires plugin)
					.addTo(controller);
</script>

<!-- Distribution plot -->
<script type="text/javascript">
	var canvas = document.getElementById('myChart');
var data = {
    labels: ["1/5", "2/5", "3/5", "4/5", "5/5"],
    datasets: [
        {
            label: "Distribution of reviews",
            backgroundColor: "rgba(48,77,112,0.2)",
            borderColor: "rgba(48,77,112,1)",
            borderWidth: 2,
            hoverBackgroundColor: "rgba(48,77,112,0.4)",
            hoverBorderColor: "rgba(48,77,112,1)",
            data: [5.29, 3.77, 7.08, 17.70, 66.15],
        }
    ]
};
var option = {
	scales: {
  	yAxes:[{
    	scaleLabel: {
        display: true,
        labelString: 'Percentage'
      	}
    }],
    xAxes:[{
    	scaleLabel: {
        display: true,
        labelString: 'Grade'
      	}
    }]
  }
};

var myBarChart = Chart.Bar(canvas,{
	data:data,
  options:option
});
</script>
</body>
</html>