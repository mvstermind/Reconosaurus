package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"

	"github.com/mvstermind/tool/brutedirs"
	"github.com/mvstermind/tool/cmd"
)

var urls []string

const dirsFile = "./lists/dir-list.txt"

func main() {
	urls = readFromFile(dirsFile)
	validUrls, err := brutedirs.CheckUrlResp(urls)
	if err != nil {
		log.Fatalf("error checking URLs: %v", err)
	}
	fmt.Println("valid URLs:", validUrls)
}

func readFromFile(dirs string) []string {
	url := cmd.GetUrl()
	file, err := os.Open(dirs)
	if err != nil {
		log.Fatalf("couldn't read file contents: %v", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		// turn directory from file into valid url
		urls = append(urls, url+"/"+strings.TrimSpace(scanner.Text()))
	}

	if err = scanner.Err(); err != nil {
		log.Fatalf("error reading file: %v", err)
	}

	return urls
}
