# Redefine NBA Player Positions from The Traditional Five to Modern Eight

##### **EECS349 Machine Learning Final Project**
##### Full project and report by: Weilin Ma (wml1890)
##### Email: weilinma2018@u.northwestern.edu

### _Abstract:_
##### This is a very cool task for me because of my enthusiasm in basketball and especially, the NBA (National Basketball Association). I was inspired by several blogs that talk about this idea of re-assigning modern NBA players into 8 categories rather than the traditional 5. I used Weka to try out different classifiers with 10-fold cross-validation. I tried to train the model with **SMO, Random Forest, Multilayer Perceptron, Naive Bayes**, and some others. I decided to eliminate some attributes out of a total of _**58 statistics categories**_ that I don't believe to work well based on my experience of basketball and NBA games. But the results showed that it actually doesn't matter too much.


##### I found that **ZeroR** and **LibSVM** gave out a very bad accuracy (19.73% and 38.25% respectively), which is expected with only 664 data groups over 55 attributes. Out of the other four classifiers I mentioned above, Multilayer Perceptron and SMO have the best performance (88.55% and 83.28% respectively with non-related attributes eliminated by me). I found that AST (assists), TRB (true rebounds), BLK (blocks), 3PA(3-pointer attemps) and avg_dist (average shot distances) are the most important attributes, which correlates with my expectation based on experience.

---

##### 5, which are Point Guard (**PG**), Shooting Guard (**SG**), Small Forward (**SF**), Power Forward (**PF**), and Center (**C**). 


##### Nowadays the game of basketball has emerged and differnent players at the same position might have very different playing style. While vast majority of the players in NBA right now are expected to player no fewer than 2 positions in a game. Categorizing players according to their playing style rather than primarily their physical apperance seems like a mroe reasonable option. So the new 8 categories are:
##### _3-and-D Wing_ , _Combo Guard_ , _Floor Genral_ , _Scoring Center_ , _Scoring Wing_ , _Shoorting Wing_ , _Supporting Center_ , and _Versatile Forward_ 



* **3-and-D Wings :** They mostly shoot 3-pointers and play perimeter-to-rim defense. They usually consists of medium height and fast-lateral-moving SG or SF. They tend to have high 3pt shooting percentage and high defensive ratings.
* **Combo Guards :** They are usually PGs or SGs who are elite at both scoring and passing. They can setup for teammates and also score themselves. They usually have higher scores and assists per game, and it's a balance.
* **Floor Generals :** Almost all of them are PGs. And they are passing-first guards. They emphasize organizing the team and assisting other teammates rather than scoring themselves. They mostly will have very high assists numbers and offensive ratings.
* **Scoring Centers :** They are not just centers but also PFs that can play deep in the paint area. These players are big guys on the court who have better scoring skills and can create their own shot. They tend to have very high close-to-rim 2-pointers shot percentage and more offensive rebounds.
* **Scoring Wings :** These players are the most valuable to today's fast-paced. They are usually taller than guards and faster than PFs and Centers. They can score in everyway possible. They can drive to the rim, shooting from outside, and create their own shots with dribble moves. They have high scores in almost every shooting category, including free throws.
* **Shooting Wings :** These wing players are almost the same as scoring wings except that their expertise is shooting. They don't drive to the rim or pull up for a jumpshot very often. They tend to have higher 3-pointer and mid-range jumper shooting percentage.
* **Supporting Centers :** They are usually the big guy in the center of an offense-defense sequence. They don't really have a lot of soft touch that they could score themselves. Rather, they are very athletic and are good at post defense and very-close shot or dunks. During offense, they are the finisher of the pass from their point guard. During defense, they are the perfect rim protector and best help-defender.They will have very high clsoe-up shooting and dunk percentage, very high rebounding and block ratings.
* **Versatile Forwards :** They are today's basketball games' favorite player type. Because they have a post player's height and physics, along with a deep shooting range. They are nightmares to defenders because they can almost score anywhere on the court. Defenders are afraid to leave them out on the perimeter so they have to follow them out. But then the post area is left open for other offense players to drive in easily. They have a fairly higher long distance shooting range than most post players and a much higher defensive rebound rating than offensive rebound rating, due to being on the perimeter for a lot of time during offense.

### Data Preparation
##### As for the data, I used a datset with more than 650 players, scraped from [basketball-reference.com](https://www.basketball-reference.com/play-index/), which is the best basketball data analyzing source that are free to public.This dataset contains a total of 56 categories, thus 56 attributes. I did a lot of tries to eliminate somee attributes that I think are not relevant based on my experience, and I did some comparisons. I'll explain later about this study.
##### Because I decided to use Weka for the model training, I wrote a python code that can **eliminate or choose** the attributes I don't want from the **csv** file and convert into the **arff** file that Weka can use.

