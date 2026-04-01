import sys
import os
from typing import Optional

# Add the parent directory to the system path to allow importing from step_1
# This enables modular architecture where each step can access previous step utilities
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from step_1.data_collector import collect_data


def fixed_size_chunk(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 200,
) -> list[str]:
    """
    Split text into fixed-size overlapping chunks.
    
    ============================================================================
    FIXED-SIZE CHUNKING STRATEGY (Classic Method)
    ============================================================================
    
    Definition:
        Fixed-size chunking divides large datasets into smaller chunks of a 
        predetermined, uniform length. This approach ensures consistency in 
        chunk size, facilitating easier processing and adherence to strict 
        context limits.
    
    Mechanism:
        The text is split based on a specific count of characters or tokens,
        regardless of the semantic content. This is the simplest and most 
        straightforward approach to chunking.
    
    Advantages:
        - Simplicity: Easy to implement and compute (Complexity: Low 1/5)
        - Efficiency: Highly effective for systems with strict input size 
          constraints (e.g., specific API limits)
        - Predictability: Provides consistent, predictable RAG performance
        - Fast processing with minimal computational overhead
    
    Limitations:
        - Semantic Disruption: Does not account for the meaning of the text;
          crucial information may be fragmented across chunks
        - Natural Flow Disruption: Splitting text into arbitrary chunks 
          destroys the natural flow of content
        - Context Breaking: Risks breaking context, which can reduce the 
          quality of retrieved information
        - Reduced Deduplication: Generally achieves lower deduplication ratio 
          than variable-sized methods
    
    Best Use Cases:
        - Systems with strict size limits
        - Baseline approach before implementing more complex strategies
        - General data processing tasks where simplicity is prioritized
    
    Reference:
        https://oneuptime.com/blog/post/2026-01-30-rag-fixed-size-chunking/view
    
    ============================================================================
    
    Args:
        text: The input text to chunk.
        chunk_size: Maximum number of characters per chunk.
                    Common range: 200-1000 tokens depending on use case.
                    Default: 1000 characters
        overlap: Number of characters to overlap between consecutive chunks.
                 Typical range: 100-200 tokens
                 Default: 200 characters
                 Purpose: Prevents context loss at chunk boundaries by 
                         retaining some content from previous chunk

    Returns:
        A list of text chunks.
        Example: 5,000 characters with chunk_size=100 results in 50 total chunks

    Raises:
        ValueError: If chunk_size <= 0, overlap < 0, or overlap >= chunk_size.
    
    Implementation Notes:
        - Uses sliding window approach where each new chunk slides forward
          while retaining overlap from previous chunk
        - Step size = chunk_size - overlap
        - Continues until entire text is processed
    """
    # Validate chunk_size parameter
    # Must be positive to ensure meaningful chunk creation
    if chunk_size <= 0:
        raise ValueError(f"chunk_size must be positive, got {chunk_size}")
    
    # Validate overlap parameter
    # Must be non-negative; negative overlap would create gaps between chunks
    if overlap < 0:
        raise ValueError(f"overlap must be non-negative, got {overlap}")
    
    # Validate overlap does not exceed chunk_size
    # Overlap >= chunk_size would create infinite loop or redundant chunks
    if overlap >= chunk_size:
        raise ValueError(
            f"overlap ({overlap}) must be less than chunk_size ({chunk_size})"
        )
    
    # Handle empty text edge case
    # Return empty list rather than processing unnecessary iterations
    if not text:
        return []

    chunks: list[str] = []
    
    # Calculate step size for sliding window
    # Step determines how far to move forward for each new chunk
    # Formula: step = chunk_size - overlap
    # Example: chunk_size=1000, overlap=200 → step=800 characters
    step = chunk_size - overlap
    start = 0

    # Iterate through text using sliding window approach
    # Continue until start position exceeds text length
    while start < len(text):
        # Extract chunk from current start position to start + chunk_size
        # Python slicing handles end-of-text automatically (no index error)
        chunks.append(text[start : start + chunk_size])
        
        # Move start position forward by step size
        # This creates the overlapping effect between consecutive chunks
        start += step

    return chunks


def get_chunks(chunk_size: int = 1000, overlap: int = 200) -> list[str]:
    """
    Collect raw data and return it as fixed-size overlapping chunks.
    
    ============================================================================
    DATA PIPELINE INTEGRATION
    ============================================================================
    
    This function serves as the integration point between:
        1. Data Collection (step_1.data_collector.collect_data)
        2. Chunking Processing (fixed_size_chunk)
    
    Workflow:
        Raw Data → Collection → Fixed-Size Chunking → Chunk List
    
    Purpose in RAG Systems:
        This is Step 2 in the RAG (Retrieval-Augmented Generation) pipeline.
        Chunking is essential for:
        - Overcoming context window limitations in language models
        - Optimizing data processing, storage, and retrieval
        - Preparing data for embedding and vector storage
    
    Comparison with Other Strategies:
        | Strategy          | Complexity | Best Use Case                    |
        |-------------------|------------|----------------------------------|
        | Fixed-Size (This) | Low        | Systems with strict size limits  |
        | Semantic          | Medium     | Search and QA systems            |
        | Recursive         | Medium     | Structured documents (PDFs)      |
        | Late              | High       | Long, complex documents          |
        | Agentic           | High       | Unstructured, high-value texts   |
        | Max-Min Semantic  | High       | Multi-topic documents, RAG       |
    
    Note: Fixed-size chunking was chosen for this implementation due to:
        - Simplicity and ease of implementation
        - Low computational cost
        - Suitable as a baseline approach
    
    For more context-aware chunking, consider:
        - Semantic Chunking: Splits at natural boundaries (paragraphs, topics)
        - Recursive Chunking: Hierarchical splitting with fallback delimiters
        - Late Chunking: Process full document before splitting for embeddings
        - Agentic Chunking: AI agent dynamically determines split points
    
    Reference Implementation:
        https://github.com/cyberytti/Rag-from-scratch/blob/main/step_2/chunker.py
    
    ============================================================================
    
    Args:
        chunk_size: Maximum number of characters per chunk.
                    Default: 1000 characters
                    Adjust based on your embedding model's context window
        overlap: Number of characters to overlap between consecutive chunks.
                 Default: 200 characters
                 Helps preserve context at chunk boundaries

    Returns:
        A list of text chunks derived from the collected data.
        Each chunk is a string of maximum chunk_size characters.
        Consecutive chunks overlap by 'overlap' number of characters.
    
    Dependencies:
        - step_1.data_collector.collect_data(): Retrieves raw text data
        - fixed_size_chunk(): Performs the actual chunking operation
    
    Example Usage:
        >>> chunks = get_chunks(chunk_size=500, overlap=100)
        >>> len(chunks)  # Number of chunks created
        >>> len(chunks[0])  # Size of first chunk (≤ 500 characters)
    """
    # Collect raw text data from step_1 data collector
    # This retrieves the source documents that need to be chunked
    raw_text = collect_data()
    
    # Apply fixed-size chunking strategy to the collected data
    # Returns list of chunks ready for embedding and vector storage
    return fixed_size_chunk(raw_text, chunk_size=chunk_size, overlap=overlap)