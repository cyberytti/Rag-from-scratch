# Retrieval-Augmented Generation (RAG) from scratch

We have all used tools like ChatGPT, Claude, Perplexity, and Gemini. Even if we haven’t used them, we have at least heard about them. 

We often call them AI (Artificial Intelligence), but they are actually LLMs (Large Language Models).

These models are trained on massive amounts of data collected from the internet, textbooks, chats, social media, and other platforms.

They are essentially statistical models that predict the next word or output based on patterns in the data.

These models can perform many different tasks. They can chat with you, write code, create presentations, and do many other things.

However, there are three main limitations or disadvantages of these models.

## 1. Knowledge Cutoff

Suppose the company behind ChatGPT, OpenAI, trained their model on March 28. This means the model has knowledge of everything that happened before that date.

However, it does not know anything about events after March 28 (such as March 29 and beyond).

These models are designed to always generate a response when given an input. So, even if they don’t have information about something, they will still try to produce an answer.

Because of this, if you ask about events that happened after March 28, the model may still respond, but in many cases, the answer could be incorrect.

This limitation is called the knowledge cutoff. When the model gives incorrect or made-up answers due to missing or outdated information, it is known as hallucination.

## 2. Context Limit

LLMs have a limit on how much text they can process at once. In this context, we use the term tokens instead of words. These models do not understand words directly; they break text into smaller units called tokens.

Every model has a maximum number of tokens it can handle at a time. This is called the context limit.

Now, suppose you try to solve the knowledge cutoff problem by giving the model a large amount of new data (after March 28) along with your query. You might expect the model to read all the data and give an accurate answer.

However, there is a problem: the model can only process a limited number of tokens.

- If your data is within this limit, the model can use it effectively.
- But if your data exceeds the limit, the model cannot process all of it properly.

As a result, you cannot directly provide a huge amount of data to the model. This limitation is known as the context limit problem.

## 3. Lack of Domain-Specific or Private Knowledge

Now, suppose you are building an AI chatbot or system for a company. The model will need access to the company’s internal information.

However, general LLMs like ChatGPT, Perplexity, or Gemini do not have access to such private or internal data.

For example, if you want to build an AI system for a telecom company, it should know details like plan prices, services, and policies. But standard chatbots like ChatGPT or Gemini do not have this specific information.


## Solution

To solve all of these problems, a technique called **Retrieval-Augmented Generation (RAG)** is used.

RAG was introduced by researchers at Meta (Facebook AI) in 2020 in the paper Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.

📄 Official research paper:
[https://arxiv.org/pdf/2005.11401](https://arxiv.org/pdf/2005.11401)

RAG works by combining two things:

* A **language model** (which generates answers)
* A **retrieval system** (which fetches relevant information from external data sources)

Instead of relying only on its training data, the model first retrieves relevant information (from documents, databases, or the internet) and then uses that information to generate a more accurate answer.


## Retrieval-Augmented Generation (RAG) System Workflow

![Simple RAG pipeline](https://i.ibb.co/HfnnNYk0/Gemini-Generated-Image-adnwa4adnwa4adnw.png)


Retrieval-Augmented Generation (RAG) system works in mainly eight steps:

1. **[Data Collection:](https://github.com/cyberytti/Rag-from-scratch/tree/main/step_1)**
   Gather data from various sources such as documents, PDFs, databases, or websites.

2. Data Chunking  
   Break the collected data into smaller chunks to avoid context limit problem.

3. Embedding Generation  
   Convert each chunk into vector representations ([embeddings](https://www.geeksforgeeks.org/machine-learning/what-are-embeddings-in-machine-learning/)) using an embedding model.

4. Vector Storage  
   Store these embeddings in a vector database for efficient retrieval.

5. User Query Input  
   The user provides a query or question to the system.

6. Query Embedding  
   Convert the user query into an embedding using the same embedding model.

7. Retrieval  
   Search the vector database to find the most relevant data chunks based on similarity.

8. Response Generation  
   Provide the retrieved information to the language model with the user asked query, to generate the final answer.


