
import re
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text) # Remove punctuation
    return text

def calculate_keyword_relevance(section_content, persona_keywords, job_keywords):
    score = 0
    preprocessed_content = preprocess_text(section_content)
    words = preprocessed_content.split()
    word_counts = Counter(words)

    for keyword in persona_keywords:
        score += word_counts[preprocess_text(keyword)] * 2 # Persona keywords are more important
    for keyword in job_keywords:
        score += word_counts[preprocess_text(keyword)]
    return score

def calculate_semantic_relevance(section_content, persona_text, job_text):
    # For CPU-only and small model size, we avoid large pre-trained models.
    # Using TF-IDF and cosine similarity as a lightweight alternative for semantic relevance.
    # This is a simplified approach and can be improved with more sophisticated (but still lightweight) methods.
    
    corpus = [preprocess_text(section_content), preprocess_text(persona_text), preprocess_text(job_text)]
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    section_vector = tfidf_matrix[0:1]
    persona_vector = tfidf_matrix[1:2]
    job_vector = tfidf_matrix[2:3]
    
    persona_similarity = cosine_similarity(section_vector, persona_vector)[0][0]
    job_similarity = cosine_similarity(section_vector, job_vector)[0][0]
    
    return (persona_similarity * 0.6) + (job_similarity * 0.4) # Weighted average

def rank_sections(sections, persona_role, job_task):
    ranked_sections = []
    
    # Extract keywords from persona and job_to_be_done
    persona_keywords = persona_role.lower().split()
    job_keywords = job_task.lower().split()

    for section in sections:
        keyword_score = calculate_keyword_relevance(section["content"], persona_keywords, job_keywords)
        semantic_score = calculate_semantic_relevance(section["content"], persona_role, job_task)
        
        # Combine scores (weights can be tuned)
        total_score = (keyword_score * 0.5) + (semantic_score * 10) # Semantic score is typically small, so scale it
        
        ranked_sections.append({
            "document": section["document_filename"], # Assuming document_filename is added to section dict
            "section_title": section["section_title"],
            "page_number": section["page_number"],
            "content": section["content"],
            "score": total_score
        })
    
    # Sort by score in descending order
    ranked_sections.sort(key=lambda x: x["score"], reverse=True)
    
    # Assign importance rank
    for i, section in enumerate(ranked_sections):
        section["importance_rank"] = i + 1
        del section["score"] # Remove score from final output
        
    return ranked_sections

def analyze_subsections(sections, persona_role, job_task, num_snippets=1):
    subsection_analysis = []
    
    # Combine persona and job task for overall relevance
    query_text = preprocess_text(persona_role + " " + job_task)
    query_words = query_text.split()

    for section in sections:
        content = section["content"]
        sentences = re.split(r'(?<=[.!?])\s+', content) # Split into sentences
        
        sentence_scores = []
        for sentence in sentences:
            # Simple scoring: count query words in sentence
            score = sum(1 for word in preprocess_text(sentence).split() if word in query_words)
            sentence_scores.append((sentence, score))
        
        # Sort sentences by score and take top N
        sentence_scores.sort(key=lambda x: x[1], reverse=True)
        
        for i in range(min(num_snippets, len(sentence_scores))):
            if sentence_scores[i][1] > 0: # Only include if there's some relevance
                subsection_analysis.append({
                    "document": section["document"],
                    "refined_text": sentence_scores[i][0],
                    "page_number": section["page_number"]
                })
    return subsection_analysis

if __name__ == '__main__':
    # Dummy data for testing
    sample_sections = [
        {
            "document_filename": "doc1.pdf",
            "section_title": "Introduction to Machine Learning",
            "page_number": 1,
            "content": "Machine learning is a field of artificial intelligence that uses statistical techniques to give computer systems the ability to \"learn\" from data, without being explicitly programmed. It is a very important topic for researchers."
        },
        {
            "document_filename": "doc1.pdf",
            "section_title": "Deep Learning Architectures",
            "page_number": 5,
            "content": "Deep learning is a subset of machine learning based on artificial neural networks. Architectures like CNNs and RNNs are widely used in various applications."
        },
        {
            "document_filename": "doc2.pdf",
            "section_title": "History of Organic Chemistry",
            "page_number": 10,
            "content": "Organic chemistry is a scientific discipline within chemistry involving the study of the structure, properties, composition, reactions, and preparation of carbon-containing compounds."
        }
    ]
    
    persona_role = "PhD Researcher in Computational Biology"
    job_task = "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks"

    # Test section ranking
    ranked_sections = rank_sections(sample_sections, persona_role, job_task)
    print("\nRanked Sections:")
    for section in ranked_sections:
        print(f"  Rank: {section['importance_rank']}, Doc: {section['document']}, Title: {section['section_title']}, Page: {section['page_number']}")

    # Test subsection analysis
    subsections = analyze_subsections(ranked_sections, persona_role, job_task)
    print("\nSubsection Analysis:")
    for sub in subsections:
        print(f"  Doc: {sub['document']}, Page: {sub['page_number']}, Text: {sub['refined_text'][:100]}...")




