package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"

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
	var okUrls []string

	for i := 0; i < len(urls); i++ {
		resp, err := http.Get(urls[i])
		if err != nil {
			return nil, err
		}
		if resp.StatusCode == http.StatusOK {
			okUrls = append(okUrls, urls[i])
		}

		resp.Body.Close()
	}
	return okUrls, nil

}
