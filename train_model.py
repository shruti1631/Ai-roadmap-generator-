import pickle
import json

# Training data for different topics and levels
training_data = {
    'machine learning': {
        'beginner': [
            'Learn linear algebra basics',
            'Understand probability and statistics',
            'Python fundamentals',
            'NumPy and Pandas basics',
            'Introduction to ML concepts',
            'Implement simple algorithms'
        ],
        'intermediate': [
            'Study supervised learning',
            'Learn unsupervised learning',
            'Regression and classification',
            'Feature engineering',
            'Model evaluation and validation',
            'Hyperparameter tuning'
        ],
        'advanced': [
            'Deep learning fundamentals',
            'Neural networks architecture',
            'CNNs and RNNs',
            'Natural language processing',
            'Reinforcement learning',
            'Production ML systems'
        ]
    },
    'web development': {
        'beginner': [
            'HTML fundamentals',
            'CSS styling basics',
            'JavaScript essentials',
            'DOM manipulation',
            'Basic responsive design',
            'Build your first website'
        ],
        'intermediate': [
            'Learn a framework (React/Vue)',
            'Backend fundamentals',
            'REST APIs',
            'Database basics (SQL)',
            'Authentication & authorization',
            'Deploy applications'
        ],
        'advanced': [
            'Advanced JavaScript patterns',
            'Microservices architecture',
            'GraphQL and advanced APIs',
            'Cloud deployment (AWS/GCP)',
            'Performance optimization',
            'Security best practices'
        ]
    },
    'python': {
        'beginner': [
            'Python syntax and basics',
            'Data types and variables',
            'Control flow (if, loops)',
            'Functions and modules',
            'File handling',
            'Build small projects'
        ],
        'intermediate': [
            'Object-oriented programming',
            'Exception handling',
            'Working with libraries',
            'Data structures optimization',
            'Testing and debugging',
            'Advanced functions'
        ],
        'advanced': [
            'Metaprogramming',
            'Decorators and generators',
            'Performance optimization',
            'Concurrency and async',
            'Building packages',
            'Contributing to open source'
        ]
    },
    'data science': {
        'beginner': [
            'Statistics fundamentals',
            'Data exploration',
            'Data visualization with Matplotlib',
            'Basic data cleaning',
            'Introduction to Pandas',
            'Simple analysis projects'
        ],
        'intermediate': [
            'Advanced statistics',
            'Exploratory data analysis',
            'Data visualization with Plotly/Seaborn',
            'SQL for data analysis',
            'Data preprocessing',
            'Statistical testing'
        ],
        'advanced': [
            'Big data technologies (Spark)',
            'Advanced visualization techniques',
            'Time series analysis',
            'Causal inference',
            'Data engineering',
            'Cloud data solutions'
        ]
    },
    'artificial intelligence': {
        'beginner': [
            'AI fundamentals and concepts',
            'Search algorithms',
            'Problem solving approaches',
            'Knowledge representation',
            'Logic and reasoning',
            'Building simple AI agents'
        ],
        'intermediate': [
            'Machine learning integration',
            'Natural language processing basics',
            'Computer vision introduction',
            'Knowledge graphs',
            'Expert systems',
            'Game AI'
        ],
        'advanced': [
            'Advanced NLP (Transformers)',
            'computer vision models',
            'Reinforcement learning agents',
            'Multi-agent systems',
            'Ethical AI',
            'AGI concepts'
        ]
    }
}

class RoadmapAIModel:
    def __init__(self):
        self.topics = list(training_data.keys())
        self.levels = ['beginner', 'intermediate', 'advanced']
        
    def get_recommendations(self, topic, level, weeks):
        """Generate AI-based recommendations"""
        
        topic_lower = topic.lower().strip()
        
        # Find best matching topic
        best_topic = None
        for t in self.topics:
            if t in topic_lower or topic_lower in t:
                best_topic = t
                break
        
        if not best_topic:
            best_topic = self.topics[0]
        
        # Ensure level is valid
        if level not in self.levels:
            level = 'beginner'
        
        # Get recommendations from training data
        recommendations = training_data.get(best_topic, training_data['python'])
        tasks = recommendations.get(level, [])
        
        # Adjust tasks based on duration
        weeks_per_task = max(1, weeks // len(tasks))
        
        phases = []
        for i, task in enumerate(tasks):
            week_start = (i * weeks_per_task) + 1
            week_end = ((i + 1) * weeks_per_task)
            
            phases.append({
                'title': f"{'📚🔍💻🎯🚀'[i % 5]} {task}",
                'duration_weeks': weeks_per_task,
                'week_range': f"{week_start}-{week_end}",
                'difficulty': level,
                'topics': [task]
            })
        
        return {
            'topic': best_topic,
            'level': level,
            'weeks': weeks,
            'phases': phases,
            'ai_generated': True
        }

# Create and save the model
if __name__ == '__main__':
    model = RoadmapAIModel()
    
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("✅ AI Model saved to model.pkl")
    
    # Test the model
    result = model.get_recommendations('python', 'beginner', 8)
    print(f"\n📊 Test Result: {json.dumps(result, indent=2, default=str)}")
