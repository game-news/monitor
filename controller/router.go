package controller

import (
	"net/http"

	v1 "gamenews.niracler.com/monitor/service/api/v1"
	"gamenews.niracler.com/monitor/setting"
	"github.com/gin-gonic/gin"
)

func MapRoutes() *gin.Engine {
	ret := gin.New()

	ret.Use(gin.Logger())

	ret.Use(gin.Recovery())

	gin.SetMode(setting.RunMode)

	ret.GET("/ping", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "pong",
		})
	})

	apiv1 := ret.Group("/api/vi")
	apiv1.GET("/game", v1.GetGames)
	apiv1.POST("/game", v1.AddGame)
	apiv1.PUT("/game/:id", v1.EditGame)
	apiv1.DELETE("/game/:id", v1.DeleteGame)

	return ret
}
