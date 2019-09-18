import pprint
import re
import pymongo, json

pp = pprint.PrettyPrinter(indent=1, width=65)

# Connect to database
client = pymongo.MongoClient(host='da1.eecs.utk.edu')
db = client['fdac19mp2']

# Connect/Create personal netid collection from database
collection = db['mnb512']

# Insert all datasets
collection.insert_one( { 'topic':'Animals', 'title':'Exotic animals as pets 2013', 'license':'NA', 'description':'Which exotic animal would you most like to have as a pet?', 'urls':['https://www.statista.com/statistics/261122/exotic-animals-as-pets/'] } )
collection.insert_one( { 'topic':'Animals', 'title':'Healthy Animals, Healthy People: Zoonosis Risk from Animal Contact in Pet Shops, a Systematic Review of the Literature', 'license':'Creative Commons', 'description':'Animal incidents', 'urls':'https://plos.figshare.com/articles/_Healthy_Animals_Healthy_People_Zoonosis_Risk_from_Animal_Contact_in_Pet_Shops_a_Systematic_Review_of_the_Literature_/944712/1' } )
collection.insert_one( { 'topic':'Animals', 'title':'Italy: distribution of private pets facilities 2005-2018, by type of animal', 'license':'NA', 'description':'Distribution of private operating facilities for pets in Italy', 'urls':'https://www.statista.com/statistics/606953/distribution-of-private-operating-facilities-for-pets-by-type-of-animal-in-italy/' } )
collection.insert_one( { 'topic':'Animals', 'title':'Live exotic animals legally and illegally imported via the main Dutch airport and considerations for public health', 'license':'Creative Commons', 'description':'Trade of live animals', 'urls':'https://plos.figshare.com/articles/Live_exotic_animals_legally_and_illegally_imported_via_the_main_Dutch_airport_and_considerations_for_public_health/9036155/1' } )
collection.insert_one( { 'topic':'Animals', 'title':'Number of pets in Germany 2000-2018, by type of animal', 'license':'NA', 'description':'Number of pets in Germany', 'urls':'https://www.statista.com/statistics/552971/pets-number-by-type-germany/' } )
collection.insert_one( { 'topic':'Animals', 'title':'Captive Reptile Mortality Rates in the Home and Implications for the Wildlife Trade', 'license':'Creative Commons', 'description':'Reptile morality rates', 'urls':'https://plos.figshare.com/articles/_Captive_Reptile_Mortality_Rates_in_the_Home_and_Implications_for_the_Wildlife_Trade_/1598786' } )
collection.insert_one( { 'topic':'Animals', 'title':'Pest animal and Weed Management Survey: National landholder survey results', 'license':'NA', 'description':'Pest and weed management and how it relates to agriculture', 'urls':'https://data.gov.au/data/dataset/pb_pawms9aai20170502' } )
collection.insert_one( { 'topic':'Animals', 'title':'Comparative Host Feeding Patterns of the Asian Tiger Mosquito', 'license':'Creative Commons', 'description':'Host patterns that a specific invasive mosquito feeds on', 'urls':'https://plos.figshare.com/articles/Comparative_Host_Feeding_Patterns_of_the_Asian_Tiger_Mosquito_Aedes_albopictus_in_Urban_and_Suburban_Northeastern_USA_and_Implications_for_Disease_Transmission/1131454' } )
collection.insert_one( { 'topic':'Animals', 'title':'Beehive Metrics', 'license':'NA', 'description':'Sensors metrics of a bee community', 'urls':'https://www.kaggle.com/se18m502/bee-hive-metrics' } )
collection.insert_one( { 'topic':'Animals', 'title':'Zoo Animal Classification', 'license':'Open Database', 'description':'Use Machine Learning Methods to Correctly Classify Animals Based Upon Attributes', 'urls':'https://www.kaggle.com/uciml/zoo-animal-classification' } )
collection.insert_one( { 'topic':'Animals', 'title':'Movebank: Animal Tracking', 'license':'NA', 'description':'Analyzing migratory patterns of animals', 'urls':'https://www.kaggle.com/pulkit8595/movebank-animal-tracking' } )
collection.insert_one( { 'topic':'Animals', 'title':'10 Monkey Species', 'license':'CC0: Public Domain', 'description':'Image dataset for fine-grain classification', 'urls':'https://www.kaggle.com/slothkong/10-monkey-species' } )
collection.insert_one( { 'topic':'Animals', 'title':'Who eats the food we grow?', 'license':'CC0: Public Domain', 'description':'Worldwide food and feed production and distribution, 1961-2013', 'urls':'https://www.kaggle.com/dorbicycle/world-foodfeed-production' } )
collection.insert_one( { 'topic':'Animals', 'title':'Animal Bites', 'license':'CC0: Public Domain', 'description':'Data on over 9,000 bites, including rabies tests', 'urls':'https://www.kaggle.com/rtatman/animal-bites' } )
collection.insert_one( { 'topic':'Animals', 'title':'National Footprint Accounts 2018', 'license':'CC BY-SA 4.0', 'description':'The Ecological Footprint of 196 Countries', 'urls':'https://www.kaggle.com/footprintnetwork/national-footprint-accounts-2018' } )
collection.insert_one( { 'topic':'Animals', 'title':'Cat and Dog', 'license':'CC0: Public Domain', 'description':'Cats and Dogs dataset to train a DL model', 'urls':'https://www.kaggle.com/tongpython/cat-and-dog' } )
collection.insert_one( { 'topic':'Animals', 'title':'Zoo Animals Extended Dataset', 'license':'CC0: Public Domain', 'description':'More than 101 zoo animals to apply classification', 'urls':'https://www.kaggle.com/agajorte/zoo-animals-extended-dataset' } )
collection.insert_one( { 'topic':'Animals', 'title':'Animals-10', 'license':'GPL 2', 'description':'Animal pictures of 10 different categories taken from google images', 'urls':'https://www.kaggle.com/alessiocorrado99/animals10' } )
collection.insert_one( { 'topic':'Animals', 'title':'Stanford Dogs Dataset', 'license':'Other', 'description':'Over 20,000 images of 120 dog breeds', 'urls':'https://www.kaggle.com/jessicali9530/stanford-dogs-dataset' } )
collection.insert_one( { 'topic':'Animals', 'title':'Austin Animal Center Shelter Outcomes', 'license':'Database: Open Database', 'description':'30,000 shelter animals', 'urls':'https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-outcomes-and' } )
