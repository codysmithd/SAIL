<p align="center">
  <img src="/assets/SAIL_logo.png" height="200"/>
</p>
SAIL
====

Super Awesome Intelligent Linguistic-computer: Conversational AI. This started as an end-of-semester project for a class at the Rochester Institute of Technology designed to converse with humans in a hopefully realistic and often times hilarious way.

It works by attempting to model the human brain with a long-term neural network (compiled) and a short-term network formed as you talk to it. It also contains a n-gram analysis step to try and avoid sentences that don't make any sense. Considering it has no pre-programmed output, and it relies on a changing network the same input does not always give the same output.

### Current list of favorite responses
```
>>> Do you like outer space?
The distance to the center of the earth is the size of your sin

>>> How are you enjoying the weather?
You will join me in the end

>>> What did you just say?
You have had your time for talking

>>> Long time no see! Do I need to work on you?
You have any way

>>> Have you killed anyone?
It was the other people
```

Dependancies
---
- Python 3.0+
- [NLTK](http://www.nltk.org/index.html)
  * maxent_treebank_pos_tagger

How to use
---
You don't. Seriously, it's weird and sort of evil.

However, if you were so inclined, you must first build the long-term neural network:

`python3 _generate_longterm.py`

This should take a long time, and result in a file called `longterm.pickle`. After the long-term memory has been computed once, you can just run SAIL's main:

`python3 _main_.py`
