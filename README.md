# Socijack (steal followers)

## Principle
1. From a list of massively followed accounts on Instagram, look at each posts
2. In each posts, look at description, see if there's someone tagged (@xxx)
3. If the account doesn't exist, BINGO.


## Set-up
```python
pip install -r requirements.txt

## add custom account in accounts.txt
python main.py
```


## Issues

Chromedriver: There might be some issue with the *chromedriver*. [Download the correct](https://chromedriver.chromium.org/downloads) *chromedriver* relative to your Chrome version and your OS, and replace the file in the project.

Slow: Avoiding to be noisy without using proxies is difficult, to avoid being too "spammy", requested are slowed.