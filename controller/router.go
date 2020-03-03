package controller

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func MapRoutes() *gin.Engine {
	ret := gin.New()

	ret.Use(gin.Logger())

	ret.Use(gin.Recovery())

	gin.SetMode("debug")

	ret.GET("/ping", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "pong",
		})
	})

	return ret
}
