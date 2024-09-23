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

	"github.com/mvstermind/tool/cmd"
)

var urls []string

func main() {
	url := cmd.GetUrl()

	file, err := os.Open("./lists/dir-list.txt")
	if err != nil {
		log.Println("couldn't read file contents!")
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		// turn directory from file into valid url
		urls = append(urls, url+"/"+strings.TrimSpace(scanner.Text()))
	}

	valid, err := checkUrlResp(urls)
	if err != nil {
		return
	}
	fmt.Println(valid)

}

func checkUrlResp(urls []string) ([]string, error) {
	if len(urls) == 0 {
		return nil, errors.New("url list is empty")

	}
	okUrls := make([]string, len(urls))
	urlsChunk1 := urls[:int(len(urls)/2)+1]
	urlsChunk2 := urls[int(len(urls)/2)+1:]

	var wg sync.WaitGroup
	for i := 0; i < len(urlsChunk1); i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			resp, err := http.Get(urlsChunk1[i])
			if err != nil {
				return
			}
			if resp.StatusCode == http.StatusOK {
				okUrls = append(okUrls, urlsChunk1[i])
			}
			resp.Body.Close()
		}()
	}

	for i := 0; i < len(urlsChunk2); i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			resp, err := http.Get(urlsChunk2[i])
			if err != nil {
				return
			}
			if resp.StatusCode == http.StatusOK {
				okUrls = append(okUrls, urlsChunk2[i])
			}
			resp.Body.Close()
		}()
	}
	wg.Wait()

	return okUrls, nil

}
