# Transcript Testing Coding Challenge

## Summary

This is a small coding challenge for us to see your approach to testing. The objective of this challenge is to validate if the python script `clean_transcript.py` conforms to the specifications by writing a small test suite.

### Getting started

If you don't have `python` installed on your machine, you can download it [here](https://www.python.org/downloads/).

`clean_transcript.py` is a simple Python script that does a very simple job: it takes text from one file, which contains a transcript from a phone conversation and cleans it up to be more readable. It writes the clean output into a new filename that you provide. You can try it out from the command line with the following command:

###### Linux/Mac

`python clean_transcript.py sample/test1.vtt result.vtt`

###### Windows

`python clean_transcript.py sample\test1.vtt result.vtt`

After you run the command above and everything works, you should have a new file called `result.vtt`. If you open it, you will see the output starts like like this:

```
Steve: Extra experience in here. Oh. Hey.

Jane: Hi. I can hear me.
```

### Objective

You should write a small automated test suite that ensures the `clean_transcript.py` beaves in the correct manner. You tests should check that `clean_transcript.py` handles these cases correctly:

* `clean_transcript` outputs a file with the following characteristics:
    * It removes the `WEBVTT` header that's in the original file.
    * It strips out all of the line numbers that are in the original file. 
    * It doesn't have any timestamps like in the original file (`00:00:20.400 --> 00:00:22.860` is removed)
    * If a person is speaking for multiple lines in the original, it collapses those into one line, and only mentions their name once.

You're welcome to use any programming language or framework to write this test suite. We've provided a small example with a couple of Python tests (called `test.py`) if you want to expand that, otherwise, write tests in whatever language you're comfortable, add some instructions in the comments, and we will try it out.

If you're unable to write all of the tests or run into technical issues, no worries! Write out how you would approach this problem (technologies or techniques you would use) and we will discuss it with you when we speak.

### Submitting Your Work

[Fork this repository](https://guides.github.com/activities/forking/) and do your work on that fork. Push the changes up and send us a link to the fork so that we can review.
