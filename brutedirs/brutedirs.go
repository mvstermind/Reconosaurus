package brutedirs

import (
	"errors"
	"net/http"
	"sync"
	"time"
)

func CheckUrlResp(urls []string) ([]string, error) {
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
