package main

import (
	"gamenews.niracler.com/monitor/service"
	"github.com/gin-gonic/gin"
)

func main() {
	service.ConnectDB()
	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})

	r.Run()
}
