#!/usr/bin/python3
def multiple_returns(sentence):
    tuple = ()
    sent = list(sentence)
    if sentence == "":
        tuple = (len(sent), None)
    else:
        tuple = (len(sent), sent[0])
    return tup
