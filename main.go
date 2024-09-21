package main

import (
	"fmt"

	"github.com/mvstermind/tool/cmd"
)

func main() {
	url, err := cmd.GetUrl()
	if err != nil {
		fmt.Println(err)
		return
	}

}
