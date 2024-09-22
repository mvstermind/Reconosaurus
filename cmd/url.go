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

func GetUrl() string {
	if !strings.HasPrefix(url, "http://") && !strings.HasPrefix(url, "https://") {
		resp, err := http.Get("https://" + url)

		if err != nil || resp.StatusCode != http.StatusOK {
			return "http://" + url
		}
		defer resp.Body.Close()

		return "https://" + url
	}
	return url
}
