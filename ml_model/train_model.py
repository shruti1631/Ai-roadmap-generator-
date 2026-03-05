# training script for roadmap AI model
# this duplicates the logic from the main workspace but kept here for model
# development and experimentation.  Run `python train_model.py` to refresh
# the pickled model used by the web app.

import pickle

# copy of the class used by the app
class RoadmapAIModel:
    def __init__(self):
        self.topics = [
            'machine learning', 'web development', 'python', 
            'data science', 'artificial intelligence'
        ]
        self.levels = ['beginner', 'intermediate', 'advanced']
        self.training_data = {
            # ... same training_data dictionary as in app.py ...
        }
        self.resources = {}

    def get_recommendations(self, topic, level, weeks):
        # identical logic as in app.py; left out for brevity
        return {}

if __name__ == '__main__':
    model = RoadmapAIModel()
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Model saved")
