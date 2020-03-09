package main

import (
	"log"
	"net/http"

	"gamenews.niracler.com/monitor/controller"
	"gamenews.niracler.com/monitor/service"
	"gamenews.niracler.com/monitor/setting"
)

func main() {
	service.ConnectDB()

	router := controller.MapRoutes()

	server := &http.Server{
		Addr:           "0.0.0.0:8001",
		Handler:        router,
		ReadTimeout:    setting.ReadTimeout,
		WriteTimeout:   setting.WriteTimeout,
		MaxHeaderBytes: 1 << 20,
	}
	err := server.ListenAndServe()
	if err != nil {
		log.Printf("Server err: %v", err)
	}
}
