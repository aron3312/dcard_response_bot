# Dcard_response_Bot

- ## Inroduction
It's a project trying to use bm25 model recommanding the dcard article similar to which we input .Then we can pick one of the comments of the article which the bot recommand to reply automatically.
---
- ## Version
Dcard_response_Bot v1
>python2.7

---

- ## Tutorial
  1. __first,__ Use Crawler.py to crawl dcard posts
      ```python
      python Crawler.py boardname
      ```  

  2. __second,__ Run startchat.py to start chat, It will take some time to create corpus from the articles crawl by Crawler.py first time you run.(The time it takes depend on the amounts of articles)
    ```python
  python startchat.py boardname
    ```  

---
- ## To-do List
  - Better way to pick comments
