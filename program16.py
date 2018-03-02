import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "uzLP2ezlKslJJpyd7C5GMJF5j",
    "consumer_secret"     : "2WiY6msdUuPCz6TXfTlVaUHHaDrp8Dm7TJizqXxQhfj8LGyx3R",
    "access_token"        : "969414937327042563-Mhfyia2FMLQBW54w2wgSvSZ5Q7EeCLP",
    "access_token_secret" : "8O95WmQTtcmCJizy1sEsxb3wi0JwgbNDtJeZqR0BGpzrQ" 
    }

  api = get_api(cfg)
  tweet = "Hello, world!................"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()

