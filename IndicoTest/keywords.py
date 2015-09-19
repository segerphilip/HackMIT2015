import indicoio
import os

indicoio.config.api_key = os.environ.get('INDICO_KEY')

# single example
indicoio.keywords("Some call it the sunshine state")

# batch example
print indicoio.keywords([
    "Some call it the sunshine state",
    "Some call it the sunshine state, the as hello Donald Trump"
])
