package step_1

import (
	"os"
)

func collect_data() ([]byte, error) {

	/* Open the data source file in read mode ("r")
	    This file acts as our raw knowledge base (Sherlock Holmes text)
		Read the entire content of the file and store it in a variable
		This is the "collected data" that will later be processed for RAG*/
	collected_data, err := os.ReadFile("step_1/data_source.txt")

	//# If any error occurs (e.g., file not found, wrong path, permission issue)
	if err != nil {
		return nil, err
	}

	// returning data collected data
	return collected_data, nil
}
