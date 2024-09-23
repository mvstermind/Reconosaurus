package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"
	"sync"
	"time"

	"github.com/mvstermind/tool/cmd"
)

var urls []string

func main() {
	url := cmd.GetUrl()

	file, err := os.Open("./lists/dir-list.txt")
	if err != nil {
		log.Fatalf("Couldn't read file contents: %v", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		// turn directory from file into valid url
		urls = append(urls, url+"/"+strings.TrimSpace(scanner.Text()))
	}

	if err = scanner.Err(); err != nil {
		log.Fatalf("Error reading file: %v", err)
	}

	validUrls, err := checkUrlResp(urls)
	if err != nil {
		log.Fatalf("Error checking URLs: %v", err)
	}
	fmt.Println("valid URLs:", validUrls)
}

func checkUrlResp(urls []string) ([]string, error) {
	if len(urls) == 0 {
		return nil, errors.New("file dir is empty")
	}

	numWorkers := 4
	urlsChan := make(chan string, len(urls))
	resultsChan := make(chan string, len(urls))

	var wg sync.WaitGroup

	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for url := range urlsChan {
				if checkUrl(url) {
					resultsChan <- url
				}
			}
		}()
	}

	for _, url := range urls {
		urlsChan <- url
	}
	close(urlsChan)

	wg.Wait()
	close(resultsChan)

	validUrls := make([]string, 0)
	for result := range resultsChan {
		validUrls = append(validUrls, result)
	}

	return validUrls, nil
}

func checkUrl(url string) bool {
	client := &http.Client{Timeout: 5 * time.Second}
	resp, err := client.Get(url)
	if err != nil {
		return false
	}
	defer resp.Body.Close()

	if resp.StatusCode == http.StatusOK || resp.StatusCode == http.StatusFound {
		return true
	}
	return false
}

