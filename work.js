// This file contains description about some of the projects I have worked upon 
// and some competitions I have participated in during college.

class Projects {
    constructor() {
        this.info = 'List of Projects';
    }

    getProjects(projectId) {
        let projects = [
// Alignment Hack for Mobiles, anyways indentation in Javascript is the least of the concerns.
{
    'projectId': 1,
    'name': 'Question Answering System using Seq2Seq Model',
    'desc': 'Worked on implementing a Natural Language Generation Model using encoder-decoder architecture with attention, with contextual Glove embeddings, and benchmarked the QA System on Stanford QnA Dataset.'
},
{
    'projectId': 2,
    'name': 'Image Segmentation using Conditional Random Fields',
    'desc': 'A study project to learn about the different Image Segmentation techniques to improve the post CNN output, using the Probabilistic graphical models such as CRFs.'
},
{
    'projectId': 3,
    'name': 'Decoding Brain EEG Signals using hybrid LSTM-CNN Model',
    'desc': 'Build a time-frequency representation of EEG Data using Mel-Spectogram, and built a hybrid architecture of CNNs and LSTMs to classify the brain-state of the signals into alpha, beta and delta waves of sleep cycle.'
}
        ];
        
        return projects[projectId - 1];
    }
}

class Competitions {
    constructor() {
        this.info = 'List of Competitions';
    }

    getCompetitions(compId) {
        let competitions = [
{
    'compId': 1,
    'name': 'Smart India Hackathon',
    'year': 2019,
    'position': 'National Winner',
    'info': 'Finalist among the Top 10 teams under the Ministry of Railways, Govt. of India, across the 6000+ teams registered from top engineering colleges in India, winning 50,000/- for our NLP project on "Deduplication of Price List Numbers"'
},
{
    'compId': 2,
    'name': 'ETH India',
    'year': 2018,
    'position': 'Finalist',
    'info': 'Finalist among the Top 20 teams across 15 countries and 3,000+ participants, who pitched their ideas to implement a secure blockchain application for incentivising the users on contributing to the blockchain community.'
},
{
    'compId': 3,
    'name': 'Microsoft CodeFunDo++',
    'year': 2018,
    'position': 'Campus Finalist',
    'info': 'Finalist among the Top 50 teams on campus to build a computer vision based application for disaster management.'
}
        ];

        return competitions[compId - 1];
    }
}


