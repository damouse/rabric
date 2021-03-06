package main

import (
    "log"
    "net/http"

    "github.com/damouse/rabric"
)

var client *rabric.Client

func main() {
    log.Println("Starting Node.")
    rabric.Debug()

    s := rabric.NewBasicWebsocketServer("pd.damouse")

    server := &http.Server{
        Handler: s,
        Addr:    ":8000",
    }

    log.Println("rabric server starting on port 8000")
    log.Fatal(server.ListenAndServe())
}