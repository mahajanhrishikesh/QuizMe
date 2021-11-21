# QuizMe
The Quiz Generator is an NLP based end to end system which can create quizzes based upon any text or topic that you provide it. 

This website can accept text from the user and create fill in the blank & Wh-? type questions on that text with the following steps:
## Blank Type Question Generation Steps:
<ol>
  <li>Use sentences inside the text, summarize the text if too long.</li>
  <li>Choose word to remove from the sentence</li>
  <li>Use word2vec or NER Knowledge Base for getting similar options.</li>
</ol>
## Wh-? Question (What/Why/Where) Generation Steps:
<ol>
  <li>Parts of Speech Identification</li>
  <li>Pass data from above step to rule based algorithm</li>
  <li>Rephrase sentence into a “What” question using reverse sentence indexing.</li>
</ol>
Alternatively the website can simply accept a topic from the user, scrape wikipedia for the topic and use the steps above to generate the questions.
<img src="https://github.com/mahajanhrishikesh/QuizMe/blob/main/imgs/proj1.PNG?raw=true">
After question generation the users can now edit the questions and answers to their liking.
<img src="https://github.com/mahajanhrishikesh/QuizMe/blob/main/imgs/proj2.PNG?raw=true">
Finally the quiz is generated.
<img src="https://github.com/mahajanhrishikesh/QuizMe/blob/main/imgs/proj3.PNG?raw=true">

UI Template Used: https://codepen.io/geertjanhendriks/pen/nztgv
