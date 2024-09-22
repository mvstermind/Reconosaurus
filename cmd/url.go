package cmd

import (
	"flag"
	"fmt"
	"net/http"
	"strings"
)

var url string

func init() {
	flag.StringVar(&url, "url", "", "Url to perform scan on")
	flag.Parse()
	if len(url) == 0 {
		fmt.Println("pass url")
		return
	}
}

func GetUrl() (string, error) {
	url = strings.TrimSpace(url)
	url = "http://" + url

	resp, err := http.Get(url)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	if resp.StatusCode == http.StatusOK {
		return url, nil
	}
	return "", fmt.Errorf("failed to access URL: %s, status code: %d", url, resp.StatusCode)
}
