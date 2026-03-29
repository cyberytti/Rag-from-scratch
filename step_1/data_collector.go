package step_1

import (
	"os"
)

func collect_data() ([]byte, error) {
	b, err := os.ReadFile("step_1/data_source.txt")
	if err != nil {
		return nil, err
	}
	return b, nil
}
