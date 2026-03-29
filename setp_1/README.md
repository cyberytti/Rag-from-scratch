# Data Collection (Step 1)

RAG systems can process various data sources such as PDFs, Markdown files, text files, Word documents, HTML pages, etc.

Data collection means gathering data from a specific source, such as a text file or a PDF file. This includes extracting content like text or images from those files and storing it in a place (such as a variable or a database) where it can be accessed programmatically.

If the collected data from a specific source is not well formatted or organized for AI to understand, it must be cleaned and formatted first. Poor preprocessing is a common cause of poor RAG performance.

In this step, data is retrieved from a data source. For simplicity, this example uses a text file as the data source.

**DATA SOURCE:** [data_source](https://github.com/cyberytti/Rag-from-scratch/blob/main/setp_1/data_source.txt)  
**DATA COLLECTOR CODE:** [data_collector.py](https://github.com/cyberytti/Rag-from-scratch/blob/main/setp_1/data_collector.py) and [data_collector.go](https://github.com/cyberytti/Rag-from-scratch/blob/main/setp_1/data_collector.go)

**DATA:** We are using "The Adventures of Sherlock Holmes" by Arthur Conan Doyle as our data.