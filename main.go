package main

import (
	"net/http"

	"gamenews.niracler.com/monitor/controller"
	"gamenews.niracler.com/monitor/service"
)

func main() {
	service.ConnectDB()

	router := controller.MapRoutes()

	server := &http.Server{
		Addr:    "0.0.0.0:8001",
		Handler: router,
	}
	server.ListenAndServe()
}
