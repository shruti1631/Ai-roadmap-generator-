from flask import Flask, render_template, request, jsonify
import pickle
import os

app = Flask(__name__, template_folder='templets', static_folder='static')

# AI Model Class
class RoadmapAIModel:
    def __init__(self):
        self.topics = [
            'machine learning', 'web development', 'python', 
            'data science', 'artificial intelligence'
        ]
        self.levels = ['beginner', 'intermediate', 'advanced']
        
        # Training data
        self.training_data = {
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
                    'Computer vision models',
                    'Reinforcement learning agents',
                    'Multi-agent systems',
                    'Ethical AI',
                    'AGI concepts'
                ]
            }
        }
        
        # Resources for each topic/level
        self.resources = {
            'machine learning': {
                'beginner': [
                    ('Intro to ML', 'https://www.coursera.org/learn/machine-learning'),
                    ('ML Crash Course', 'https://developers.google.com/ml-crash-course')
                ],
                'intermediate': [
                    ('Hands-On ML', 'https://www.oreilly.com/library/view/hands-on-machine-learning/'),
                    ('Fast.ai Course', 'https://www.fast.ai/')
                ],
                'advanced': [
                    ('Deep Learning Book', 'http://www.deeplearningbook.org/'),
                    ('Stanford CS231n', 'http://cs231n.stanford.edu/')
                ]
            },
            'web development': {
                'beginner': [
                    ('freeCodeCamp', 'https://www.freecodecamp.org/'),
                    ('MDN Web Docs', 'https://developer.mozilla.org/')
                ],
                'intermediate': [
                    ('React Docs', 'https://reactjs.org/docs/getting-started.html'),
                    ('Express Guide', 'https://expressjs.com/')
                ],
                'advanced': [
                    ('Fullstack Open', 'https://fullstackopen.com/en/'),
                    ('Modern Web Architecture', 'https://www.pluralsight.com/')
                ]
            },
            'python': {
                'beginner': [
                    ('Python.org Tutorials', 'https://docs.python.org/3/tutorial/'),
                    ('Automate the Boring Stuff', 'https://automatetheboringstuff.com/')
                ],
                'intermediate': [
                    ('Real Python', 'https://realpython.com/'),
                    ('Effective Python', 'https://effectivepython.com/')
                ],
                'advanced': [
                    ('Fluent Python', 'https://www.oreilly.com/library/view/fluent-python/'),
                    ('Advanced Python', 'https://realpython.com/advanced-python/')
                ]
            },
            'data science': {
                'beginner': [
                    ('DataCamp', 'https://www.datacamp.com/'),
                    ('Intro to Data Science', 'https://www.coursera.org/specializations/introduction-data-science')
                ],
                'intermediate': [
                    ('Kaggle', 'https://www.kaggle.com/learn'),
                    ('Data Science Handbook', 'https://www.datasciencehandbook.org/')
                ],
                'advanced': [
                    ('Spark Tutorials', 'https://spark.apache.org/tutorials.html'),
                    ('Advanced Data Science', 'https://www.edx.org/')
                ]
            },
            'artificial intelligence': {
                'beginner': [
                    ('AI for Everyone', 'https://www.coursera.org/learn/ai-for-everyone'),
                    ('Intro to AI', 'https://www.edx.org/course/artificial-intelligence-ai')
                ],
                'intermediate': [
                    ('NLP with Deep Learning', 'https://web.stanford.edu/class/cs224n/'),
                    ('AI Ethics', 'https://www.coursera.org/learn/ai-ethics')
                ],
                'advanced': [
                    ('AGI Papers', 'https://agi.ai/'),
                    ('Advanced AI Research', 'https://arxiv.org/')
                ]
            }
        }
        
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
        recommendations = self.training_data.get(best_topic, self.training_data['python'])
        tasks = recommendations.get(level, [])
        
        # Adjust tasks based on duration
        weeks_per_task = max(1, weeks // len(tasks))
        
        phases = []
        emojis = ['📚', '🔍', '💻', '🎯', '🚀']
        
        for i, task in enumerate(tasks):
            week_start = (i * weeks_per_task) + 1
            week_end = ((i + 1) * weeks_per_task)
            
            phases.append({
                'title': f"{emojis[i % 5]} {task}",
                'duration_weeks': weeks_per_task,
                'week_range': f"{week_start}-{week_end}",
                'difficulty': level,
                'topics': [task]
            })
        
        resources = self.resources.get(best_topic, {}).get(level, [])
        return {
            'topic': best_topic,
            'level': level,
            'weeks': weeks,
            'phases': phases,
            'resources': resources,
            'ai_generated': True
        }

# Load the AI Model
try:
    with open('model.pkl', 'rb') as f:
        ai_model = pickle.load(f)
    print("✅ AI Model loaded successfully!")
except Exception as e:
    print(f"⚠️ Could not load AI model from file: {e}")
    print("🤖 Creating new AI model instance...")
    ai_model = RoadmapAIModel()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Get form data
        topic = request.form.get('topic', '').strip()
        level = request.form.get('level', '').strip()
        duration = request.form.get('duration', '')
        
        # Validation
        if not topic or len(topic) < 2:
            error = "Topic must be at least 2 characters long"
            return render_template('index.html', error=error)
        
        if level not in ['beginner', 'intermediate', 'advanced']:
            error = "Please select a valid difficulty level"
            return render_template('index.html', error=error)
        
        try:
            duration = int(duration)
            if duration < 1 or duration > 52:
                error = "Duration must be between 1 and 52 weeks"
                return render_template('index.html', error=error)
        except (ValueError, TypeError):
            error = "Duration must be a valid number"
            return render_template('index.html', error=error)
        
        # Generate roadmap (html,text)
        roadmap_html, roadmap_text = generate_roadmap(topic, level, duration)
        
        # store text in session for download
        request.environ['roadmap_text'] = roadmap_text
        return render_template('index.html', roadmap=roadmap_html, topic=topic, level=level, duration=duration)
    
    except Exception as e:
        error = f"Error generating roadmap: {str(e)}"
        return render_template('index.html', error=error)

def generate_roadmap(topic, level, duration):
    """Generate roadmap using AI model; return html and text"""
    
    if ai_model:
        try:
            ai_result = ai_model.get_recommendations(topic, level, duration)
            phases = ai_result.get('phases', [])
            resources = ai_result.get('resources', [])
            matched_topic = ai_result.get('topic', topic)
            ai_used = True
        except Exception as e:
            print(f"AI Model error: {e}")
            phases = []
            resources = []
            matched_topic = topic
            ai_used = False
    else:
        phases = []
        resources = []
        matched_topic = topic
        ai_used = False
    
    badge = '🤖' if ai_used else '📋'
    html = f'''
    <div class="roadmap-header">
        <h3>{badge} {matched_topic.title()} - {level.capitalize()} Level</h3>
        <p><strong>Total Duration:</strong> {duration} weeks | <strong>Generated:</strong> {"AI Powered ✨" if ai_used else "Standard"}</p>
    </div>
    <div class="roadmap-phases">
    '''
    text = f"{matched_topic.title()} - {level.capitalize()} Level ({duration} weeks)\n"
    for phase in phases:
        html += f'''
        <div class="phase">
            <h4>{phase['title']}</h4>
            <p class="week-range">📅 Week {phase.get('week_range', '1-1')}</p>
            <ul class="tasks">
        '''
        text += f"- {phase['title']} (Week {phase.get('week_range','1-1')})\n"
        topics = phase.get('topics', [])
        if isinstance(topics, list):
            for topic_item in topics:
                html += f'<li>✓ {topic_item}</li>'
                text += f"    * {topic_item}\n"
        else:
            html += f'<li>✓ {topics}</li>'
            text += f"    * {topics}\n"
        html += '''
            </ul>
        </div>
        '''
    if resources:
        html += '<div class="resources"><h4>📚 Useful Resources</h4><ul>'
        text += "\nResources:\n"
        for name, link in resources:
            html += f'<li><a href="{link}" target="_blank">{name}</a></li>'
            text += f"- {name}: {link}\n"
        html += '</ul></div>'
    html += '</div>'
    return html, text

@app.route('/api/generate', methods=['POST'])
def api_generate():
    """API endpoint for roadmap generation (returns JSON)"""
    try:
        data = request.get_json()
        
        topic = data.get('topic', '').strip()
        level = data.get('level', '').strip()
        duration = data.get('duration', '')
        
        # Validation
        if not topic or len(topic) < 2:
            return jsonify({'error': 'Topic must be at least 2 characters long'}), 400
        
        if level not in ['beginner', 'intermediate', 'advanced']:
            return jsonify({'error': 'Invalid difficulty level'}), 400
        
        try:
            duration = int(duration)
            if duration < 1 or duration > 52:
                return jsonify({'error': 'Duration must be between 1 and 52 weeks'}), 400
        except (ValueError, TypeError):
            return jsonify({'error': 'Duration must be a number'}), 400
        
        roadmap_html, roadmap_text = generate_roadmap(topic, level, duration)
        return jsonify({
            'success': True,
            'topic': topic,
            'level': level,
            'duration': duration,
            'roadmap': roadmap_html,
            'text': roadmap_text
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/roadmap/<topic>/<level>/<int:weeks>')
def get_roadmap_by_params(topic, level, weeks):
    """Get roadmap by URL parameters"""
    if level not in ['beginner', 'intermediate', 'advanced']:
        return jsonify({'error': 'Invalid level'}), 400
    
    if weeks < 1 or weeks > 52:
        return jsonify({'error': 'Weeks must be between 1 and 52'}), 400
    
    roadmap_html, roadmap_text = generate_roadmap(topic, level, weeks)
    return jsonify({
        'topic': topic,
        'level': level,
        'weeks': weeks,
        'roadmap': roadmap_html,
        'text': roadmap_text
    })

@app.route('/download')
def download():
    """Download plain-text roadmap using query parameters"""
    topic = request.args.get('topic', '')
    level = request.args.get('level', '')
    weeks = request.args.get('weeks', '')
    try:
        weeks = int(weeks)
    except (ValueError, TypeError):
        weeks = 0
    if not topic or not level or weeks < 1:
        return "Invalid download parameters", 400
    _, roadmap_text = generate_roadmap(topic, level, weeks)
    return (
        roadmap_text,
        200,
        {
            'Content-Type': 'text/plain; charset=utf-8',
            'Content-Disposition': f'attachment; filename="{topic}_{level}_{weeks}_roadmap.txt"'
        }
    )

if __name__ == '__main__':
    app.run(debug=True)
