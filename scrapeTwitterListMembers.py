'''
Uses the Tweepy library (http://www.tweepy.org/) to pull the name, 
screenname, and bio/url for all users in a list.

Make sure you've installed Tweepy:
$ pip install tweepy

You will can generate a consumer key/secret and access token/secret
by creating a Twitter app (https://apps.twitter.com/).
'''


'''
API.list_members(owner, slug, cursor)
Returns the members of the specified list.

Parameters: 
owner – the screen name of the owner of the list
slug – the slug name or numerical ID of the list
cursor – Breaks the results into pages. Provide a value of -1 to
         begin paging. Provide values as returned to in the response 
         body’s next_cursor and previous_cursor attributes to page 
         back and forth in the list.

Return type:  
list of User objects
'''

import tweepy 

consumer_key = input("Enter consumer key: ")
consumer_secret = input("Enter consumer secret: ")
access_token = input("Enter access token: ")
access_token_secret = input("Enter access token secret: ")
owner = input("Enter screen name of the owner of the list: ")
slug = input("Enter slug name or numerical ID of the list: ")

filename = slug + '_members.csv'
f = open(filename, 'w')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

list_members = tweepy.Cursor(api.list_members, owner, slug, -1).items()
for user in list_members:
    name = user.name
    screen_name = user.screen_name
    description = user.description
    url = user.url

    str = ''
    if name is not None:
      str = str + name + ','
    else:
      str = str + ','

    if screen_name is not None:
      str = str + screen_name + ','
    else:
      str = str + ','

    if description is not None:
      str = str + description + ','
    else:
      str = str + ','

    if url is not None:
      str = str + url + '\n'
    else:
      str = str + '\n'

    f.write(str)

f.close()
print("All done! Contents written to " + filename + ".")