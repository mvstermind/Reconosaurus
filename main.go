package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/mvstermind/tool/cmd"
)

var urls []string

func main() {
	url, err := cmd.GetUrl()
	if err != nil {
		fmt.Println(err)
		return
	}

	file, err := os.Open("./lists/dir-list.txt")
	if err != nil {
		log.Println("couldn't read file contents!")
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		urls = append(urls, url+scanner.Text())
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
		} else {
			okUrls = append(okUrls, urls[i])
		}
		resp.Body.Close()
	}
	return okUrls, nil

}
