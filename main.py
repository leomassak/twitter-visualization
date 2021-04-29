import os
from searchtweets import load_credentials, ResultStream, gen_request_parameters
from searchtweets import collect_results

keymap = {
    'SEARCHTWEETS_BEARER_TOKEN': os.path.join('credentials', 'bearertoken'),
    'SEARCHTWEETS_CONSUMER_KEY': os.path.join('credentials', 'apikey'),
    'SEARCHTWEETS_CONSUMER_SECRET': os.path.join('credentials', 'apisecret'),
}

for key, value in keymap.items():
    with open(value, 'r') as credfile:
        os.environ[key] = credfile.read()


stream_args=load_credentials(filename="config.yaml",
                 yaml_key="search_tweets_pgdinamica",
                 env_overwrite=True)

query = gen_request_parameters('python', results_per_call=10)

tweets = collect_results(query, result_stream_args=stream_args)

for tweet in tweets:
    try:
        if tweet['text']:
            print(tweet['text'], end='\n\n')
            print('------------------------')
    except Exception as e:
        print('FIM')
    
        