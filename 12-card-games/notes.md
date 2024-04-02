# Notes

- This chapter introduced the 'testing with main' object
- For a Blackjack deck, can make it

```python
blackJackDict = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8': 8, '9':9, '10':10, 'Jack':10, 'Queen': 10, 'King': 10}
oBlackjackDeck = Deck(window, rankValueDict=blackJactDict)
```

But still have to deal with Ace being either 1 or 11 in game implementation! (Shouldn't be hard. Just if at 10 and draw an ace, win.)