def collect_data():
    try:
        # Open the data source file in read mode ("r")
        # This file acts as our raw knowledge base (Sherlock Holmes text)
        with open("setp_1/data_source.txt", "r") as file:
            
            # Read the entire content of the file and store it in a variable
            # This is the "collected data" that will later be processed for RAG
            collected_data = file.read()

            return collected_data

    # If any error occurs (e.g., file not found, wrong path, permission issue)
    except Exception as error:
        
        # Print a user-friendly message indicating failure in data loading
        print("Data is not loaded properly!")
        
        # Print the actual error for debugging purposes
        print(error)




print (collect_data())