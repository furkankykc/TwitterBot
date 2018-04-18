import Myauth
from twitterRest import TwitterClient

tw = TwitterClient(auth=Myauth.default())

print(
    tw.getRateLimit()
)
print(
    tw.api.rate_limit_status()
)
