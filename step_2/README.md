## 1. Introduction to Chunking

**Chunking** is the computational process of dividing large datasets into smaller, manageable segments. This procedure is essential for overcoming context window limitations in language models and optimizing data processing, storage, and retrieval.

There are various strategies for chunking, ranging from classic methods to advanced techniques developed between 2025 and 2026. The following sections detail these methodologies, their mechanisms, and their appropriate applications.

---

## 2. Classic Chunking Strategies

### 2.1 Fixed-Size Chunking

**Definition**  
Fixed-size chunking is a strategy wherein large datasets are divided into smaller chunks of a predetermined, uniform length. This approach ensures consistency in chunk size, facilitating easier processing and adherence to strict context limits.

**Mechanism**  
The text is split based on a specific count of characters or tokens, regardless of the semantic content.
*   *Example:* A dataset containing 5,000 characters divided into chunks of 100 characters results in 50 total chunks.

**Advantages**  
*   **Simplicity:** Easy to implement and compute.
*   **Efficiency:** Highly effective for systems with strict input size constraints (e.g., specific API limits).

**Limitations**  
*   **Semantic Disruption:** Does not account for the meaning of the text; crucial information may be fragmented across chunks.

**Reference:** [Fixed-Size Chunking](https://oneuptime.com/blog/post/2026-01-30-rag-fixed-size-chunking/view)

---

### 2.2 Semantic Chunking

**Definition**  
Semantic chunking divides data based on meaning rather than fixed dimensions. This method ensures that each chunk contains logically or contextually related information.

**Mechanism**  
Text is split at natural boundaries, such as sentence endings, paragraph breaks, or topic shifts, ensuring each chunk represents a complete idea.
*   *Example:* In a multi-paragraph article, splits occur at topic changes rather than at a specific character count.

**Advantages**  
*   **Context Preservation:** Maintains the logical flow and meaning of the data.
*   **Retrieval Quality:** Particularly useful for search, question answering, and retrieval systems.

**Limitations**  
*   **Complexity:** More difficult to implement than fixed-size chunking as it requires analysis of text structure or meaning.

**Reference:** [Semantic Chunking](https://oneuptime.com/blog/post/2026-01-30-semantic-chunking/view)

---

### 2.3 Recursive Chunking

**Definition**  
Recursive chunking is a hierarchical text-splitting strategy. It attempts to divide data using larger, natural boundaries first, progressively falling back to smaller delimiters until each chunk fits within the desired size.

**Mechanism**  
The splitting process follows a hierarchy of separators:
1.  Paragraph breaks
2.  Line breaks
3.  Spaces
4.  Character level (if necessary)

*   *Example:* If a paragraph exceeds the size limit, the method attempts to split by paragraph first. If chunks remain too large, it splits by line, then space, and finally by character.

**Advantages**  
*   **Structural Integrity:** Preserves semantic boundaries more effectively than fixed-size chunking.
*   **Versatility:** Works well with structured or semi-structured data (e.g., articles, documents).
*   **Balance:** Offers a middle ground between simple fixed-size and complex semantic methods.

**Limitations**  
*   **Uniformity:** Not ideal when strictly equal-sized chunks are required without regard for text structure.

**Ideal Use Cases**  
Documents where maintaining structure (headings, paragraphs, sentence flow) is critical, such as PDFs, wiki pages, and policy documents.

**Reference:** [Recursive Chunking](https://oneuptime.com/blog/post/2026-01-30-rag-recursive-chunking/view)

---

## 3. Advanced Chunking Strategies (2025–2026)

### 3.1 Late Chunking

**Definition**  
Late chunking is a strategy wherein the entire document (or a significant portion) is processed as a whole to capture full context before being split into smaller chunks. This is commonly utilized in modern retrieval systems to enhance embedding quality.

**Mechanism**  
1.  The full text is passed through an embedding model to encode the document with complete context.
2.  The resulting representations are subsequently divided into smaller chunks.
3.  Each chunk retains awareness of the broader document meaning.

**Advantages**  
*   **Global Context:** Preserves overall context better than early chunking methods.
*   **Embedding Quality:** Improves representation quality, especially for long and complex documents.
*   **Relationship Retention:** Reduces the risk of losing important relationships between distant parts of the text.

**Limitations**  
*   **Resource Intensive:** Requires significant computational resources.
*   **Input Limits:** May not be suitable for systems with strict input size limits during the embedding phase.

**Ideal Use Cases**  
Large, complex documents where understanding the overall context is paramount, such as research papers, technical documentation, or long-form content.

**Reference:** [Late Chunking](https://arxiv.org/pdf/2409.04701)

---

### 3.2 Agentic Chunking

**Definition**  
Agentic chunking is an advanced strategy in which an intelligent agent (typically powered by a language model) dynamically determines how to divide data based on context, structure, and the intended task.

**Mechanism**  
The agent analyzes the document to identify natural boundaries (topics, sections, key ideas) using signals such as headings, semantic meaning, and user intent. The strategy adapts depending on the content type and downstream application (e.g., search vs. question answering).

**Advantages**  
*   **Task Awareness:** Produces highly meaningful chunks tailored to specific tasks.
*   **Adaptability:** Automatically adjusts to different document types.
*   **Performance:** Often outperforms static methods for complex or unstructured data.

**Limitations**  
*   **Cost and Complexity:** More computationally expensive and harder to implement than static approaches.

**Ideal Use Cases**  
Complex, unstructured, or high-value documents where context is critical, such as legal texts, research papers, or multi-topic content.

**Reference:** [Agentic Chunking](https://www.ibm.com/think/topics/agentic-chunking)

---

### 3.3 Max–Min Semantic Chunking

**Definition**  
Max–Min semantic chunking creates chunks by balancing two objectives: maximizing semantic coherence within each chunk and minimizing redundancy or overlap between chunks.

**Mechanism**  
The text is analyzed based on semantic meaning. The algorithm groups sentences or segments that are highly related (maximum similarity) into the same chunk while ensuring different chunks are as distinct as possible (minimum similarity between chunks).
*   **Clustering:** Uses embedding similarity to decide which sentences belong together and where to split.

**Advantages**  
*   **Coherence:** Creates highly meaningful and internally consistent chunks.
*   **Reduced Redundancy:** Minimizes duplication of information across chunks.
*   **Retrieval Precision:** Improves retrieval quality by making each chunk distinct and focused.

**Limitations**  
*   **Computational Cost:** Can be expensive and requires careful tuning of similarity thresholds or clustering methods.

**Ideal Use Cases**  
Multi-topic or complex documents where clear separation of ideas improves search and retrieval performance, particularly in embedding-based systems and RAG pipelines.

**Reference:** [Max–Min Semantic Chunking](https://link.springer.com/article/10.1007/s10791-025-09638-7)

---

## 4. Summary of Strategies

| Strategy | Primary Basis | Complexity | Best Use Case |
| :--- | :--- | :--- | :--- |
| **Fixed-Size** | Character/Token Count | Low | Systems with strict size limits |
| **Semantic** | Meaning/Context | Medium | Search and QA systems |
| **Recursive** | Hierarchical Delimiters | Medium | Structured documents (PDFs, Articles) |
| **Late** | Post-Embedding Split | High | Long, complex documents |
| **Agentic** | AI Agent Decision | High | Unstructured, high-value texts |
| **Max–Min Semantic** | Similarity Optimization | High | Multi-topic documents, RAG pipelines |

## 5. Conclusion

Selecting the appropriate chunking strategy depends on the specific requirements of the system, the nature of the data, and the available computational resources. While classic methods like Fixed-Size and Recursive chunking offer efficiency and simplicity, advanced strategies such as Late, Agentic, and Max–Min Semantic chunking provide superior context preservation and retrieval quality for complex applications.
However, depending on the nature of the data, we can also design custom chunking solutions. For this example, we have implemented our own custom chunking method.

You can find the implementation here: [chunker.py](https://github.com/cyberytti/Rag-from-scratch/blob/main/step_2/chunker.py)
