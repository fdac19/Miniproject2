import pymongo, json, pprint
client = pymongo.MongoClient (host="da1.eecs.utk.edu")
db = client ['fdac19mp2']
coll = db ['apoole13']
# for each dataset
coll.insert ( { 'topic':'YourTopic', 'Weightlifting': 'Jumpshot', 'license': 'license', 'description': 'Industry Overview', 'urls': [ 'https://www.jumpshot.com/category/sports-fitness-outdoors/strength-weight-training' ] } )
coll.insert ( { 'topic':'YourTopic', 'Weightlifting': 'Kaggle - Weight lifting', 'license': 'license', 'description': '721 Weight LIfting Workouts', 'urls': [ 'https://www.kaggle.com/joep89/weightlifting' ] } )
coll.insert ( { 'topic':'YourTopic', 'Weightlifting': 'Kaggle - Power lifting', 'license': 'license', 'description': 'Power Lifting Database', 'urls': [ 'https://www.kaggle.com/open-powerlifting/powerlifting-database' ] } )
coll.insert ( { 'topic':'YourTopic', 'Weightlifting': 'Statista', 'license': 'license', 'description': 'Crossfit Workouts', 'urls': [ 'https://www.statista.com/statistics/252539/affluent-americans-who-do-weightlifting-or-bodybuilding/' ] } )
coll.insert ( { 'topic':'Weightlifting', 'title': 'Kaggle - Human Activity', 'license': 'license', 'description': 'Human Activity', 'urls': [ 'https://www.kaggle.com/singhpraveen/weight%20lifting%20exercises%20dataset' ] } )
coll.insert ( { 'topic':'Weightlifting', 'title': 'Datahub - Bench', 'license': 'license', 'description': 'Bench Weightlifting Exercises', 'urls': [ 'https://old.datahub.io/dataset/49df4ff7-e578-4a87-a664-61d9144a3445' ] } )
coll.insert ( { 'topic':'Weightlifting', 'title': 'Datahub - Exercises', 'license': 'license', 'description': 'Changing Weightlifting Exercises', 'urls': [ 'https://old.datahub.io/dataset/28a434be-259f-4eaf-a101-60cd72cf7d7b' ] } )
coll.insert ( { 'topic':'Weightlifting', 'title': 'Datahub - Equipment', 'license': 'license', 'description': 'Fitness Equipment', 'urls': [ 'https://old.datahub.io/dataset/97435bcf-97ed-443b-8fa4-a6907abf45e5' ] } )
coll.insert ( { 'topic':'Weightlifting', 'title': 'Kaggle - Measurements', 'license': 'license', 'description': 'Workout Measurements', 'urls': [ 'https://www.kaggle.com/fsiamp/workout-measurements' ] } )
coll.insert ( { 'topic':'Weightlifting', 'title': 'Kaggle - Supplements', 'license': 'license', 'description': 'Workout Supplements', 'urls': [ 'https://www.kaggle.com/afsaja/workout-supplements-and-nutrition-products' ] } )
coll.insert ( { 'topic':'Weightlifting', 'title': 'Research Gate', 'license': 'license', 'description': 'Change for Weightlifting', 'urls': [ 'https://www.researchgate.net/publication/262449383_Changes_in_exercises_are_more_effective_than_in_loading_schemes_to_improve_muscle_strength' ] } )
coll.insert ( { 'topic':'Weightlifting', 'title': 'Datahub - Suggestions', 'license': 'license', 'description': 'Workout Suggestions', 'urls': [ 'https://old.datahub.io/dataset/63498718-3a39-4189-86a5-c57ae5747325' ] } )
coll.insert ( { 'topic':'Weightlifting', 'title': 'DataHub - Muscle Growth', 'license': 'license', 'description': 'Muscle Gain and Hormones', 'urls': [ 'https://old.datahub.io/dataset/celik' ] } )
coll.insert ( { 'topic':'Weightlifting', 'title': 'Bodybuilding', 'license': 'license', 'description': 'Full list of Exercises', 'urls': [ 'https://www.bodybuilding.com/exercises/finder' ] } )
coll.insert ( { 'topic':'Weightlifting', 'title': 'DataHub - Overtraining', 'license': 'license', 'description': 'What is overtraining in exercising', 'urls': [ 'https://old.datahub.io/dataset/52aba27b-d37f-4c84-bd89-62133d88d41a' ] } )
coll.insert ( { 'topic':'Weightlifting', 'title': 'Victoria', 'license': 'license', 'description': 'Exercise Equipment', 'urls': [ 'http://opendata.victoria.ca/datasets/663a527673774550b4777f984dfc7237_18/data' ] } )
coll.insert ( { 'topic':'Weightlifting', 'title': 'Bodybuilding - Workout Plans', 'license': 'license', 'description': 'Set of workout plans', 'urls': [ '/' ] } )
coll.insert ( { 'topic':'Weightlifting', 'title': 'Kaggle - Power Lifting Exercises', 'license': 'license', 'description': 'Power Lifting', 'urls': [ 'https://www.kaggle.com/dansbecker/powerlifting-database' ] } )
coll.insert ( { 'topic':'Weightlifting', 'title': 'Kaggle - Muscle Nutrition', 'license': 'license', 'description': 'Nutrition Products for Fitness', 'urls': [ 'https://www.kaggle.com/afsaja/workout-supplements-and-nutrition-products' ] } )
coll.insert ( { 'topic':'Weightlifting', 'title': 'Kaggle - Workout Schedule', 'license': 'license', 'description': 'Graph of Common Workout Times', 'urls': [ 'https://www.kaggle.com/nsrose7224/crowdedness-at-the-campus-gym' ] } )





pp = pprint.PrettyPrinter(indent=1,width=65)
for r in coll. find():
      print(pp .pformat (r))
