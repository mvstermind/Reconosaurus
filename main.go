package main

import (
	"fmt"
	"log"
	"os"

	"github.com/mvstermind/tool/cmd"
)

func main() {
	url, err := cmd.GetUrl()
	if err != nil {
		fmt.Println(err)
		return
	}

	dir, err := os.ReadFile("./lists/dir-list.txt")
	if err != nil {
		log.Println("couldn't read file contents!")
	}

	_ = formUrls(url, dir)

}

func formUrls(baseUrl string, dirNames []byte) []string {
	var stringified []string
	var lc int
	for i := 0; i < len(dirNames); i++ {
		if dirNames[i] == '\n' {
			if lc > 0 {
				stringified = append(stringified, string(dirNames[i-lc:i]))
			}
			lc = 0
		} else {
			lc++
		}
	}
	if lc > 0 {
		stringified = append(stringified, string(dirNames[len(dirNames)-lc:]))
	}
	fmt.Println(stringified)

	return nil
}
