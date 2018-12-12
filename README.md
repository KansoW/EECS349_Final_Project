# Redefine NBA Player Positions from The Traditional Five to Modern Eight

##### **EECS349 Machine Learning Final Project**
##### Full project and report by: Weilin Ma (wml1890)
##### Email: weilinma2018@u.northwestern.edu

### _Abstract:_
##### This is a very cool task for me because of my enthusiasm in basketball and especially, the NBA (National Basketball Association). I was inspired by several blogs that talk about this idea of re-assigning modern NBA players into 8 categories rather than the traditional 5. I used Weka to try out different classifiers with 10-fold cross-validation. I tried to train the model with _**SMO, Random Forest, Multilayer Perceptron, Naive Bayes**_, and some others. I decided to eliminate some attributes out of a total of _**58 statistics categories**_ that I don't believe to work well based on my experience of basketball and NBA games. But the results showed that it actually doesn't matter too much.


##### I found that _**ZeroR**_ and _**LibSVM**_ gave out a very bad accuracy (19.73% and 38.25% respectively), which is expected with only 664 data groups over 55 attributes. Out of the other four classifiers I mentioned above, Multilayer Perceptron and SMO have the best performance (88.55% and 83.28% respectively with non-related attributes eliminated by me). I found that AST (assists), TRB (true rebounds), BLK (blocks), 3PA(3-pointer attemps) and avg_dist (average shot distances) are the most important attributes, which correlates with my expectation based on experience.

![Average Shot Distances Effectiveness Visualized](https://github.com/KansoW/EECS349_Final_Project/blob/master/images/avg_dist.png)
Figure 1. Average Shot Distances Effectiveness Visualized
This figure shows how influencial that the attribute **_avg_dist_** (average shot distance) is on the results of _**labels**_ (8 positions). The center and forward positions tend to have shorter shot distances while guards and wingmen tend to have longer distances. They are better seperated than other attributes.

---

### _Description:_
##### Nowadays the game of basketball has emerged and differnent players at the same position might have very different playing style. While vast majority of the players in NBA right now are expected to player no fewer than 2 positions in a game. Categorizing players according to their playing style rather than primarily their physical apperance seems like a mroe reasonable option than the traditional 5, which are Point Guard (**PG**), Shooting Guard (**SG**), Small Forward (**SF**), Power Forward (**PF**), and Center (**C**). So the new 8 categories are:

* **3-and-D Wings :** They mostly shoot 3-pointers and play perimeter-to-rim defense. They usually consists of medium height and fast-lateral-moving SG or SF. They tend to have high 3pt shooting percentage and high defensive ratings.
* **Combo Guards :** They are usually PGs or SGs who are elite at both scoring and passing. They can setup for teammates and also score themselves. They usually have higher scores and assists per game, and it's a balance.
* **Floor Generals :** Almost all of them are PGs. And they are passing-first guards. They emphasize organizing the team and assisting other teammates rather than scoring themselves. They mostly will have very high assists numbers and offensive ratings.
* **Scoring Centers :** They are not just centers but also PFs that can play deep in the paint area. These players are big guys on the court who have better scoring skills and can create their own shot. They tend to have very high close-to-rim 2-pointers shot percentage and more offensive rebounds.
* **Scoring Wings :** These players are the most valuable to today's fast-paced. They are usually taller than guards and faster than PFs and Centers. They can score in everyway possible. They can drive to the rim, shooting from outside, and create their own shots with dribble moves. They have high scores in almost every shooting category, including free throws.
* **Shooting Wings :** These wing players are almost the same as scoring wings except that their expertise is shooting. They don't drive to the rim or pull up for a jumpshot very often. They tend to have higher 3-pointer and mid-range jumper shooting percentage.
* **Supporting Centers :** They are usually the big guy in the center of an offense-defense sequence. They don't really have a lot of soft touch that they could score themselves. Rather, they are very athletic and are good at post defense and very-close shot or dunks. During offense, they are the finisher of the pass from their point guard. During defense, they are the perfect rim protector and best help-defender.They will have very high clsoe-up shooting and dunk percentage, very high rebounding and block ratings.
* **Versatile Forwards :** They are today's basketball games' favorite player type. Because they have a post player's height and physics, along with a deep shooting range. They are nightmares to defenders because they can almost score anywhere on the court. Defenders are afraid to leave them out on the perimeter so they have to follow them out. But then the post area is left open for other offense players to drive in easily. They have a fairly higher long distance shooting range than most post players and a much higher defensive rebound rating than offensive rebound rating, due to being on the perimeter for a lot of time during offense.

---

### _Data Preparation:_
##### As for the data, I used a datset with more than 650 players, scraped from [basketball-reference.com](https://www.basketball-reference.com/play-index/), which is the best basketball data analyzing source that are free to public.This dataset contains a total of 67 categories, thus _**67 attributes**_. I did a lot of tries to eliminate somee attributes that I think are not relevant based on my experience (about 11 in total), and I did some comparisons. I'll explain below about this study.

##### Because I decided to use Weka for the model training, I wrote a [python script](https://github.com/KansoW/EECS349_Final_Project/blob/master/convert_arff.py) that can _**eliminate or select**_ the attributes I don't want from the _**csv**_ file and convert into the _**arff**_ file that Weka can use. This way I can try to eliminate differnet "non-relevant" attributes evry time and see if my prediction based on basketball knowledge is accurate. 

##### The attributes I think that are non-relevant and have eliminatedare:
* **Status:** whether the player is active or inactive (retired or not currently playing for any team)
* **g :** career games played 
* **mp :** career games played
* **TOV :** career tornovers total count
* **TOV% :** turnovers per 100 plays
* **OWS :** offensive win share
* **DWS :** defensive win share
* **WS :** total win share
* **WS/48 :** win share per 48 minuts (almost per game)
* **fg3a_heave :** feild goal 3-pointers attempted from beyond half court distance
* **fg3_heave :** field goal 3-pointers made from beyond half court distance

---

### _Results:_
##### _**With all 11 attributes non-relevant eliminated:**_
##### Here are the results from MLP, SMO, RF and NB, all with 10-fold cross-validation:
![MLP_full](https://github.com/KansoW/EECS349_Final_Project/blob/master/images/MLP_full.png)
Figure 2. Multilayer Perceptron
![SMO_full](https://github.com/KansoW/EECS349_Final_Project/blob/master/images/SMO_full.png)
Figure 3. SMO
![RF_full](https://github.com/KansoW/EECS349_Final_Project/blob/master/images/RF_full.png)
Figure 4. Random Forest
![NB_full](https://github.com/KansoW/EECS349_Final_Project/blob/master/images/NaiveBayes_full.png)
Figure 5. Naive Bayes

##### As we can tell from the results that MLP and SMO are clearly has the best accuracy out of the six classifiers I tried. So I did another version with *TOV* and *TOV%* added back to the list to be considered during the training. Here are the results of MLP and SMO:
![MLP_TOV](https://github.com/KansoW/EECS349_Final_Project/blob/master/images/MLP_TOV.png)
Figure 6. Multilayer Perceptron with TOV Considered
![SMO_TOV](https://github.com/KansoW/EECS349_Final_Project/blob/master/images/SMO_TOV.png)
Figure 7. SMO with TOV Considered

---

### _Analyze:_
#####  From the _**Confusion Matrix**_ of almost all results from the classifiers, we can find interesting relationship between these 8 positions. And I would say the relationship is very reasonable.
##### _**Scoring Center**_ and _**Supporting Center**_ can be mixed up during the validation. I think it's because that they both have high points per game and 2-pointer shot percentage. They slight difference is that supporting centers have limited ways to score thus much higher close-up 2-pointer shooting percentage. 
##### Here's similar relationship with _**Shoorting Wing**_ and _**3-and-D Wing**_. They look like the hardest pair to be differentiated. I think it's also because that they have high 3-pointer shooting percentage due to being _**"wings"**_ (that means they usually play at the perimeter area). But 3-and-D wings usually have slightly lower points made per game and higher defensive ratings than shooting wings because they need to play more defense for the team. Perimeter defense is a very exhausting and low-effective job to do in a team so defensive wings usually do not play too much offense other than mostly shooting open 3-pointers, in today's NBA basketball game.
##### I am actually a little surprised that _**Combo Guard**_ and _**Floor General**_ did not seem like a challenge for these training models at all. I expected there would be confusion because they should both have higher assists count and assists percentage than any other positions. But looking back at the visuals for _**AST**_ and _**AST%**_, I understand now:
![ast_pct]()
Figure 8. Assit Percentage Visualized
##### Here in the figure we can tell that these two positions truly are the top 2 in assists stats. But one thing I didn't expect is that floor generals still have much higher even than the No.2 combo guards. The fairly smaller weighting of Floor General might also be a factor of this behavior. 
