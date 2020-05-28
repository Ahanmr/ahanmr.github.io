'''
Hi there, I'm Ahan M R. I'm a Data Science Researcher currently living in Bangalore, India. 

Currently, I'm a Data Science Intern at American Express- Big Data Labs in the Unstructed Data Analytics Team.

I'm really interested in working on implementing and building various Recommendation Systems, Natural Language Models ranging from Seq2Seq to projects involving Code-switched language. I also have worked on Temporal Classification and Image Segmentation in Computer Vision. Beyond which, I love Quizzing and Debating as part of various competitions. I've won the Smart India Hackathon 2019, Swiggy CodeIn Hackathon 2018, and also have been contributing to various Research Organisations and Open Source Libraries.  
'''
class AhanMR:
    def __init__(self):
        self.name = 'Ahan M R'
        self.phoneNumber = 7888014619
        self.email = 'ahanmr@gmail.com'
    
    def workExperience(self):
        return {
            'May 2019 - Aug 2019': 'Data Science Intern @ American Express- Big Data labs, Bangalore',
            'Dec 2018 - Jan 2019': 'Deep Learning Intern @ MarsView.ai',
            'May 2018 - July 2018': 'Summer Intern @ UST Global, Trivandrum',
            'Oct 2017 - Present': 'Software Innovator @ Intel Labs, India'
        }

    def education(self):
        return [
            { '2016 - 21': 'M.Sc. in Mathematics at Birla Institute of Technology and Science, Pilani' },
            { '2016 - 21': 'B.E. in Electronics and Electrical Engineering at Birla Institute of Technology and Science, Pilani' }
        ]

    def projects(self):
        return [
            {'Question Answering System using Seq2Seq Model': 'Worked on implementing a Natural Language Generation Model using encoder-decoder architecture with attention, with contextual Glove embeddings, and benchmarked the QA System on Stanford QnA Dataset'},
            {'Image Segmentation using Conditional Random Fields': 'A study project to learn about the different Image Segmentation techniques to improve the post CNN output, using the Probabilistic graphical models such as CRFs.'},
            {'Decoding Brain EEG Signals using Hybrid CNN-LSTM architecture': 'Build a time-frequency representation of EEG Data using Mel-Spectogram, and built a hybrid architecture of CNNs and LSTMs to classify the brain-state of the signals into alpha, beta and delta waves of sleep cycle.'}
        ]

    def responsibilities(self):
        return {
            'Neural Networks and Fuzzy Logic': 'Teaching Assistant',
            'Optimisation': 'Teaching Assistant',
            'BITS Genesis': 'Sub-Coordinator',
        }

    def getResume(self):
        return 'https://ahanmr.me/resume.pdf'


