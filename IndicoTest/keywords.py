import indicoio
indicoio.config.api_key = '7b74e295428b8926509939285684621a'

# single example
indicoio.keywords("Some call it the sunshine state")

# batch example
print indicoio.keywords([
    "Some call it the sunshine state",
    "Some call it the sunshine state, the as hello Donald Trump"
])