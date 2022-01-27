import tweepy
import time
from Covid19_ByState import *

ApiKey = 'gHKxDgSdrwoCGhtNbzjsoze5b'
ApiSecretKey = 'LeIBhRsuowqtj6uJBYizgwguGfCMC9gfeyEKG5uW9GRipYwDm4'
AccessToken = '1301149386437734400-nr3WywLGaBjt0VdRSPSCY5GepZydkX'
AccessSecretToken = '1L3JIZxcZqjm3E2uyfsBjYE6FcGW14C3JoyDrkoWslStp'

auth = tweepy.OAuthHandler(ApiKey, ApiSecretKey)
auth.set_access_token(AccessToken, AccessSecretToken)
api = tweepy.API(auth)


fileName = "AlreadyReplied_TweetID.txt"
def RepliedID():
    fRead = open(fileName, 'r')
    repliedId = fRead.readline().strip()
    fRead.close()
    return repliedId

def ReplyTweets():
    since_id = int(RepliedID())
    mentions = api.mentions_timeline(since_id)
    fn = open(fileName, 'w')
    for m in mentions:
        ment = m.id
        status = api.get_status(ment)
        st = status.text
        statustext = [i for i in st.upper().split()]
        if statustext[1] in statesList:
            statustxt = str(statustext[1])
            status = f'@{m.user.screen_name} {GetCasesPerState(statustxt)}'
            print(status)
            username = m.id
            api.update_status(status, username)
        else:
            print("it's not there")
        print(ment)
        fn.writelines(str(f'{ment}\n'))
    fn.close()

#ReplyTweets()
#time.sleep(15)
# = api.get_status(1303204392968093696)
b = api.get_status(1303202572904345601)
#print(a.text)
mentions = api.mentions_timeline()
print(mentions)
print(b.text)
